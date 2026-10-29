import random
def get_choices():
    player_choice = input("Enter Your Choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"your choice: {player} \ncomputer choice: {computer}")
    if player == computer:
        return "its a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock beats scissors you won"
        else:
            return "paper beats rock computer won"
    elif player == "scissors":
        if computer == "rock":
            return "rock beats scissors computer won" 
        else:
            return "scissors beats paper you won"
    else:
        if computer == "scissors":
            return "scissor beats paper so computer won"
        else:
            return "paper beats rock so you won"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)


 
        
