import random


def game():
    print("That's your score ..")
    score = random.randint(1, 100)
    with open("highscore.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"your score : {score}")
    if (score > highscore):
        with open("highscore.txt", 'W') as f:
            f.write(str(score))
    return score


game()
