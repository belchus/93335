import json

post = {
    "titulo":"Mi primer post",
    "autor":"Camila",
    "visitas" : 100
}

with open ("post.json","w",encoding="utf-8") as archivo:
    json.dump(post,archivo,indent=4)

print("post guardado")