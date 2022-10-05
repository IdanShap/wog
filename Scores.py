import utils
from pathlib import Path


class Scores:

    def __init__(self, username):
        self.username = username

    def add_score(self, difficulty):
        points = difficulty * 3

        scoreboard = Path(utils.SCORES_FILE_NAME)
        if scoreboard.is_file():
            mode = "r+"
        else:
            mode = "w+"

        file = open(utils.SCORES_FILE_NAME, mode, encoding="utf-8")
        current_scores = file.readlines()

        score_found = False
        for i in range(len(current_scores)):
            seperated = current_scores[i].split(',')
            if seperated[0] == self.username:
                new_score = int(seperated[1]) + points
                current_scores[i] = f'{seperated[0]},{new_score}\n'
                score_found = True

        if not score_found:
            current_scores.append(f'{self.username},{points}\n')

        file.close()

        file = open(utils.SCORES_FILE_NAME, "w+", encoding="utf-8")
        file.writelines(current_scores)
        file.close()

