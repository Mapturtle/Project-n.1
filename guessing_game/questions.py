from multiprocessing.connection import answer_challenge


class Question:
    def __init__(self, promt, answer):
        self.promt= promt
        self.answer= answer

