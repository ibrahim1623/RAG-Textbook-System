from pinecone import Pinecone, ServerlessSpec
import yaml
import embeddings
import time

embeds = embeddings.create_embeddings()

index_name = "textbook-rag"

with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
    API_KEY = config["PINECONE_API_KEY"]

pinecone = Pinecone(api_key = API_KEY)


index_name = "textbook-rag"

if index_name not in pinecone.list_indexes().names():
    pinecone.create_index(
        name = index_name,
        dimension=1536,
        metric="cosine",
        spec = ServerlessSpec(cloud="aws", region="us-east-1")
    )

    while not pinecone.describe_index(index_name).status['ready']:
        time.sleep(1)

index = pinecone.Index(index_name)
time.sleep(1)
print(index.describe_index_stats())

# print(embeds)
# for i, embedding in enumerate(embeds):
#     index.upsert([(str(i), embedding)])

print(index.describe_index_stats())

from openai import OpenAI
import yaml 

with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
    API_KEY = config['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

query  = '''Suppose we obtain n independent observations, Y1,...,Yn, from a Poisson probability
model to estimate the Poisson parameter μ. Consider the estimator  ̃μ =  ̄Y .
1. Show  ̃μ is unbiased.
2. Find Var( ̃μ) (an exact formula for the variance).
3. Is  ̃μ a consistent estimator of μ?
4. Consider  ̃Var( ̃μ) =  ̃μ/n as an estimator of Var( ̃μ).
(a) Show that  ̃Var( ̃μ) is an unbiased estimator of Var( ̃μ).
(b) What is the variance of  ̃Var( ̃μ)?
(c) Is  ̃Var( ̃μ) a consistent estimator of Var( ̃μ)?'''

xq = client.embeddings.create(input=query, model="text-embedding-3-small").data[0].embedding

max_length = 100

res = index.query(
    vector=xq, 
    top_k=1,
    include_metadata=True
)

# for match in res['matches']:
#     # Get the score and text metadata
#     score = match['score']
#     text = match['metadata']['text']
    
#     # Print the score and the first few lines of the text
#     print(f"{score:.2f}: {text[:max_length]}...")

#     with open(f"top_chunks/{score}.md", "w") as file:
#         file.write(text)

for match in res['matches']:
    text = match['metadata']['text']

augmented_query = f'''
question: {query} 





context{text}'''

with open("final_query/query.md", "w") as file:
    file.write(augmented_query)