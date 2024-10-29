import tiktoken
import spacy
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
from embedding import SentenceTransformerEmbeddings

max_token_limit = 8000

tokenizer = tiktoken.encoding_for_model("gpt-4o")

nlp = spacy.load("en_core_web_sm")

model = SentenceTransformerEmbeddings('all-MiniLM-L6-v2')

#initialize text splitter
text_splitter = SemanticChunker(
    model, breakpoint_threshold_type="gradient"
)

def chunker(text):
    # converting text to docs object
    docs = text_splitter.create_documents([text])

    # convert to list of strings
    docs_list = []
    for doc in docs:
        docs_list.append(doc.page_content)

    chunks = []
    current_chunk = ''
    for chunk in docs_list:
        token_count = count_tokens(current_chunk) + count_tokens(chunk)

        if token_count < max_token_limit:
            current_chunk += chunk
        else:
            if current_chunk:
                if count_tokens(current_chunk) >= max_token_limit:
                    chunks.extend(chunker(current_chunk)) 
                else:
                    chunks.append(current_chunk)
            current_chunk = chunk


    if current_chunk:
        if count_tokens(current_chunk) >= max_token_limit:
            chunks.extend(chunker(current_chunk))  
        else:
            chunks.append(current_chunk)

    return chunks

# number of tokens in text
def count_tokens(text):
    return len(tokenizer.encode(text))

# read text from file
with open("./outputs/stat305_course_pack.txt") as file:
    text = file.read()

chunks = chunker(text)

for index, chunk in enumerate(chunks):
    with open(f"./chunks/chunk-{index}.txt", "w") as file:
        file.write(chunk)