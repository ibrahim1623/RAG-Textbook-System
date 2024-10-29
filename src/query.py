from openai import OpenAI
import yaml 

with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
    API_KEY = config['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

query  = "what is the PDF of the normal distribution?"

xq = client.embeddings.create(input=query, model="text-embedding-3-small").data[0].embedding