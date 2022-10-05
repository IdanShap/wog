from flask import Flask
from pathlib import Path
import utils

app = Flask(__name__)


@app.route("/")
def display_scoreboard():
    if Path(utils.SCORES_FILE_NAME).is_file():
        file = open(utils.SCORES_FILE_NAME, "r", encoding="utf-8")
        lines = file.readlines()

        html_list = '<table>'
        for line in lines:
            score = line.split(',')
            html_list += f'<tr><td>{score[0]}</td><td>{score[1]}</td></tr>'
        html_list += '</table>'

        return html_list
    else:
        return 'An error occurred, cannot find the scoreboard right now'


app.run(host='0.0.0.0', port=80)