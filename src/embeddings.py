from openai import OpenAI
import os
import yaml

with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
    API_KEY = config['OPENAI_API_KEY']

# returns embeddings
def create_embeddings():

    embeddings = []

    path_to_output = "./output_LLM"

    client = OpenAI(api_key=API_KEY)

    for filename in sorted(os.listdir(path_to_output)):
        filepath = os.path.join(path_to_output, filename)
        with open(filepath, 'r') as file:
            text = file.read()
            response = client.embeddings.create(input = [text], model = "text-embedding-3-small").data[0].embedding
            print(f"the length of the emnbedding created is : {len(response)}")
            embeddings.append(response)

    
    return embeddings
create_embeddings()