from random import choice
from flask import Flask
from os import environ

app = Flask(__name__)
options_file = environ.get("OPTIONS_FILE", "options.txt")
#choices = ["first", "second", "third"]

def load_options(file_path):
  with openf(ile_path, "r", encoding="uft8") as f:
  file_contents = f.read()
    return file_contents.split()

options = load_options(options_file)

@app.route("/")
def pick_word():
  return choice(options)
