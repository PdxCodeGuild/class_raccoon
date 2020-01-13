import json

file = r"saves\autosave_S.json"
while True
    # file = input("please input the relative path of then save file")
    try:
        plaintext = open(file, 'r').read()
        break
    except FileNotFoundError:
        print("file not found.")

def id_search_(id):
    for i in content["QualitiesPossessedlist"]
    if content["QualitiesPossessedlist"][i] == id:
        return i

content = json.loads(plaintext)
