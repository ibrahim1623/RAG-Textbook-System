from chunker import count_tokens
import os 
path_to_chunks = "./chunks"
for index, filename in enumerate(os.listdir(path_to_chunks)):
    file_path = os.path.join(path_to_chunks, filename)

    with open(file_path, encoding='utf-8') as file:
        text = file.read()
    print(f"{index} - {count_tokens(text)}")

print("___________________________________")

path_to_output = "./output_LLM"
for index, filename in enumerate(os.listdir(path_to_output)):
    file_path = os.path.join(path_to_output, filename)
    with open(file_path, encoding='utf-8') as file:
        text = file.read()
    print(f"{index} - {count_tokens(text)}")