import json

with open("post.json","r",encoding="utf-8") as archivo:
    post = json.load(archivo)

print(post)
print(post["titulo"])
print(type(post))
