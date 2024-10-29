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

print(embeds)
# for i, embedding in enumerate(embeds):
#     index.upsert([(str(i), embedding)])

print(index.describe_index_stats())

from openai import OpenAI
import yaml 

with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
    API_KEY = config['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

query  = "what is the PDF of the normal distribution?"

xq = client.embeddings.create(input=query, model="text-embedding-3-small").data[0].embedding

max_length = 200

res = index.query(
    vector=xq, 
    top_k=5,
    include_metadata=True
)

for match in res['matches']:
    # Get the score and text metadata
    score = match['score']
    text = match['metadata']['text']
    
    # Print the score and the first few lines of the text
    print(f"{score:.2f}: {text[:max_length]}...")