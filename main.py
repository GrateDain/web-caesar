from flask import Flask, request
from helpers import alphabet_position, rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/" method="POST">
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" id="rot" value="0">
        <br/>
        <textarea name="text">{0}</textarea>
        <br/>
        <input type="submit" value="Submit Query">
      </form>
    </body>
</html> """

@app.route('/')
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form["text"]
    rotation = int(request.form["rot"])
    n_text = ''
    for char in text:
        n_text += rotate_character(char, rotation)
    return form.format(n_text)


app.run()