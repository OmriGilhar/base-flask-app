from flask import Flask

app = Flask(__name__)
BASE_HTML = '''<!DOCTYPE html>
<html>
   <body>
      <h1>Heroku Rules!</h1>
      <img src="http://i.stack.imgur.com/SBv4T.gif" alt="this slowpoke moves"  width="250" />
   </body>

</html>'''


@app.route("/")
def index():
    return BASE_HTML


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)
