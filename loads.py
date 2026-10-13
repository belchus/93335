import json

post_json = '{"titulo":"Desde loads","autor":"Camila desde loads","visitas":100}'

post = json.loads(post_json)

print(type(post_json))
print(post)
print(post["titulo"])
print(post["autor"])
print(type(post))