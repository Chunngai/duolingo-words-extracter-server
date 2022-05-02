import json
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello!"


@app.route("/run/", methods=["POST"])
def run():
    language = request.values.get('language')
    unit = request.values.get('unit')
    skill = request.values.get('skill')
    level = request.values.get('level')

    sheet = f"U{unit}, {skill}, l{level}"
    os.system(f"""
        cd ../duolingo-words-extracter; 
        python main.py --lang {language} --sheet "{sheet}"
    """)

    try:
        fp_new_words = "../duolingo-words-extracter/.new_words"

        with open(fp_new_words, "r", encoding="utf-8") as f:
            words = list(filter(
                bool,
                f.read().split("\n")
            ))
        os.remove(fp_new_words)

        return json.dumps({
            'code': 200,
            'data': words
        })
    except:
        return json.dumps({
            'code': 100_000,
            'data': []
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
