from flask import Flask         # from the flask module import the Flask class
#OOP - object oriented paradigm
app = Flask(__name__)           # When you create an instance of a class, you get an object; app is now an object

@app.get("/")                   # Flask decorator that allows us to define routes
def home():
    me = {                      # pyhton3 dictionary
        "first_name": "Rafael",
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "is_online": True
    }
    return me                    # When you return a dictionary from a flask function, its converted to JSON
