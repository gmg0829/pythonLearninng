import json
with open('config.json','r') as f:
    config=json.load(f)
a=config['gmg']['a']
c=config['yr']['c']
print(a)