import connexion


def post_file():
    file = connexion.request.files['jsonfile']
    print(file)