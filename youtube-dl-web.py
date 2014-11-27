import subprocess
import json
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    error = None
    result = None
    url = request.form.get('url')
    if url:
        try:
            stdout = subprocess.check_output(["youtube-dl", "-j", url])
        except subprocess.CalledProcessError as e:
            error = e
        else:
            result = json.loads(stdout.decode('utf8'))
    return render_template("home.html", error=error, result=result)


if __name__ == '__main__':
  app.run(debug=1)
