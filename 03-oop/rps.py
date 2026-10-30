import random

throws = ("rock", "paper", "scissors")
wins = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]   # (winner, loser)

def play_round():
    human = input("throw > ").strip().lower()
    cpu = random.choice(throws)
    return {"human": human, "cpu": cpu}

def judge(human, cpu):
    if human not in throws:
        return "invalid throw, type rock, paper or scissors"
    print(f"{human} vs {cpu}")
    if human == cpu:
        return "same throw, its a draw"
    if (human, cpu) in wins:
        return "human wins"
    return "cpu wins"

round_one = play_round()
print(judge(round_one["human"], round_one["cpu"]))
