import json
json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])

teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))