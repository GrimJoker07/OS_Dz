def Zad3():
    import json
    import os

    data = input()
    to_json = {'nadpis': data}
    with open('file.json', 'w') as f:
        f.write(json.dumps(to_json))
    with open('file.json') as f:
        print(f.read())
    os.remove('file.json')