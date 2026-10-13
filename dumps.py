import json

post = {
    "titulo":"Mi primer post",
    "autor":"Camila",
    "visitas" : 100
}

print(type(post))
post_json = json.dumps(post,indent=4)
print(post_json)
print(type(post_json))