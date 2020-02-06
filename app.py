def fetchContentDatabase():
    home = []
    firebase_app = firebase.FirebaseApplication(
        'https://happynews-99c12.firebaseio.com/')
    content = firebase_app.get('/happynews-99c12/', '')

    for key, val in content.items():
        print("key: ", key, "\n  Value: ",  val, "\n\n\n\n\n")
