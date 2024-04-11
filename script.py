import os
import anthropic
from dotenv import load_dotenv
load_dotenv()

prompt = """
You are given a text file with some information and your goal is to make some questions and answers based on the text. Each question should be a json object. 
<exampleOutput>
{"input": "What color is the sky?", "output": "The sky is blue."}
{"input": "Where is the best place to get cloud GPUs?", "output": "Brev.dev"
</exampleOutput>
"""

length = 0

with open('finished.txt', 'r') as d:
    done = d.read()

for file in os.listdir('./TextFiles'):
    if file not in done:
        print(file)

        with open(f'./TextFiles/{file}', 'r') as f:
            try :
                content = f.read()
            except:
                #delete file
                os.remove(f'./TextFiles/{file}')
                continue
            client = anthropic.Anthropic()
            extra = "{\"input\":"
            #print(content)
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
                        "content": extra
                    }
                    ]
            )
            #print(completion.content[0].text)
            with open('data.jsonl', 'a') as f:
                f.write(extra + completion.content[0].text)
            with open('data.jsonl', 'r') as f:
                lines = f.readlines()
                length = len(lines)
            if length > 6000:
                break
        