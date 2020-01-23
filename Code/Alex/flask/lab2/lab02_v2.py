def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))


def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data


@app.route('/', methods=['GET', 'POST'])
def index1():

    if request.method == 'POST':


    return render_template('index1.html')