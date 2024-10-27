from openai import OpenAI
import os 
import yaml

with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
    API_KEY = config['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

path_to_chunks = "./chunks"

def api_call(text: str, index: int) -> str:

    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f'''You are an expert at converting raw text to LaTex for math textbooks. 
                Convert the following text to LateX code without omitting or adding anything: {text}'''
            }
        ]
    )
    response_text = completion.choices[0].message.content

    # change to .tex later
    with open(f'./output_LLM/output-{index}.tex', 'w') as file:
        file.write(response_text)

    print("Response saved.")

for index, filename in enumerate(os.listdir(path_to_chunks)):
    file_path = os.path.join(path_to_chunks, filename)

    with open(file_path, encoding='utf-8') as file:
        text = file.read()

    api_call(text, index)


