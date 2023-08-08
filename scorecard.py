from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('JetBrains Mono', 20, 'normal')


class Scorecard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('score.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scorecard()

    def increase_score(self):
        self.score += 1
        self.update_scorecard()
