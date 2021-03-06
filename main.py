from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form="""
<!DOCTYPE html>
<!-- uploaded code from web caesar below -->
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
      <form action="/encrypted" method='POST'>
      <label for="rot">Rotate By:</label>
      <input id="rot" type="text" name="rot" />
      
      <textarea type='text' name='text'rows="3" cols="4">{0}</textarea>
      <input type="submit" value='Submit Query'></input>
      </form>
    </body>
</html>
</form>
"""
@app.route("/")
def index():
    return form.format("")


@app.route("/encrypted", methods=['POST'])
def encrypt():
    message=request.form['text']
    rot=request.form["rot"]
    rot=int(rot)
    content= rotate_string(message, rot)
    return form.format(content)

app.run()
