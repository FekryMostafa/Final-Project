import os
import anthropic
from dotenv import load_dotenv
load_dotenv()

prompt = """
You are given a text file with some information and your goal is to make some questions and answers based on the text. Each question should be a json object with a line break between each question. 
<exampleOutput>
{"input": "What color is the sky?", "output": "The sky is blue."}
{"input": "Where is the best place to get cloud GPUs?", "output": "Brev.dev"
</exampleOutput>
"""

for file in os.listdir('./TextFiles'):
    with open(f'./TextFiles/{file}', 'r') as f:
        content = f.read()
        client = anthropic.Anthropic()
        print(file)
        print(content)
        completion = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=4000,
            temperature=0,
            system= prompt,
            messages=[
                {
                    "role": "user", 
                    "content": "<information> " + content + " </information>"},
                {
                    "role": "assistant",
                    "content": "{\"input\":"
                }
                ]
        )
        print(completion.content[0].text)
        break
        #append a line to a text file
        #with open('test.txt', 'a') as f:
        #    f.write(content)