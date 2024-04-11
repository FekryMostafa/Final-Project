with open('data.jsonl', 'r') as f:
    lines = f.readlines()
print(len(lines))
    #content = f.read()

#lines = [line for line in lines if line.strip() != '']
#with open('data.jsonl', 'w') as f:
#    f.writelines(lines)

#content = content.replace('}{', '}\n{')

#lines = [line for line in lines if 'author' not in line.lower()]

lines = [line for line in lines if 'text' not in line.lower()]

with open('data.jsonl', 'w') as f:
    #f.write(content)
    #lines = f.readlines()
    f.writelines(lines)
print(len(lines))