from openai import OpenAI
import yaml

with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
    API_KEY = config['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

with open("./final_query/query.md", "r") as file:
    full_text = file.read()

def api_call(text: str) -> str:

    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": text
            }
        ]
    )
    response_text = completion.choices[0].message.content

    with open("./final_query/response.md", "w") as file:
        file.write(response_text)

api_call(full_text)