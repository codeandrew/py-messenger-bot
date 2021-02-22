def read_quotes():
    with open('quotes/gandhi.json') as json_file:
        x = json.loads(json_file.read())
        print(x)