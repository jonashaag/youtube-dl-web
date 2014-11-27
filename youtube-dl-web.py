import re
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
        if not re.match("^https?://(www.)?youtube.com/watch\\?v=.+$", url):
          error = "URL muss mit <tt>https://www.youtube.com/watch?v=</tt> beginnen"
        else:
          try:
              stdout = subprocess.check_output(["youtube-dl", "-j", url])
          except subprocess.CalledProcessError:
              error = "Fehler beim Abrufen des Videos :-("
          else:
              result = json.loads(stdout.decode('utf8'))
    return render_template("home.html", error=error, result=result)


if __name__ == '__main__':
  app.run(debug=1)
