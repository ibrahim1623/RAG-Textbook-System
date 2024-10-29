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
                "content": f'''You are a skilled markdown expert working on formatting raw text from a math textbook. 
                            Your task is to convert the following text into precise markdown code, preserving every detail exactly as presented. 
                            This text is part of a structured textbook, so accuracy in mathematical notation, symbols, numbers, and all textual elements is crucial.

                            Please follow these guidelines:
                            1. **Do not omit or add** any content. Each element should be preserved exactly as in the original text.
                            2. **Mathematical notation** should follow conventional markdown standards and should represent the content precisely.
                            3. **Text and paragraph structure** should be accurately reflected, keeping line breaks, spacing, and any emphasized text (e.g., bold or italicized) consistent with the original.
                            4. Ensure that **any special characters** are converted properly into markdown syntax to maintain the intended meaning.
                            5. You will be passed part of the textbook so ensure that you convert ALL the text without leaving anything out.
                            6. REMEMBER TO GO THROUGH THE ENTIRE TEXT SO THAT YOU DO NOT MISS OUT ON ANYHTING, THE TOKEN COUNTS SHOUDL BE SIMILAR AT THE END
                            
                            Text to convert:
                            {text}
                            '''

            }
        ]
    )
    response_text = completion.choices[0].message.content

    # change to .tex later
    with open(f'./output_LLM/output-{index}.md', 'w') as file:
        file.write(response_text)

    print("Response saved.")

for index, filename in enumerate(os.listdir(path_to_chunks)):
    file_path = os.path.join(path_to_chunks, filename)

    with open(file_path, encoding='utf-8') as file:
        text = file.read()

    api_call(text, index)


