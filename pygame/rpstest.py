from random import randint

options = ['rock', 'paper', 'scissors']
tries = 10

# Markov Chain Tracking (Tracks transitions from one move to the next)
transition_counts = {
    "rock": {"rock": 0, "paper": 0, "scissors": 0},
    "paper": {"rock": 0, "paper": 0, "scissors": 0},
    "scissors": {"rock": 0, "paper": 0, "scissors": 0}
}
last_move = None  # Track the last move of the player

def predict_player_move():
    """ Predict the player's next move using Markov Chain probabilities """
    global last_move
    if last_move is None:  # No history yet
        return options[randint(0, 2)]

    # Find the most frequent move after the last move
    predicted_move = max(transition_counts[last_move], key=transition_counts[last_move].get)

    # Counter the predicted move
    counter_moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter_moves[predicted_move]


def compare(player, computer):
    if player == computer:
        return "It's a tie!"

    winning_combos = {
        ('rock', 'scissors'): "You win! Rock beats Scissors!",
        ('paper', 'rock'): "You win! Paper beats Rock!",
        ('scissors', 'paper'): "You win! Scissors beats Paper!",
        ('rock', 'paper'): "You lose! Paper beats Rock!",
        ('paper', 'scissors'): "You lose! Scissors beats Paper!",
        ('scissors', 'rock'): "You lose! Rock beats Scissors!"
    }

    return winning_combos.get((player, computer), "Something went wrong!")


while tries > 0:
    listChoices = []
    choice = input("Pick two: Rock (r), Paper (p), or Scissors (s)? ").lower()
    choice = choice.split()

    for letter in choice:
        if letter == 'r':
            listChoices.append("rock")
        elif letter == 'p':
            listChoices.append("paper")
        elif letter == 's':
            listChoices.append("scissors")

    if len(listChoices) != 2:
        print("Please pick exactly two choices!")
        continue

    # AI picks based on Markov Chain prediction
    computer_choice_1 = predict_player_move()
    computer_choice_2 = options[randint(0, 2)]  # Random second choice
    computer = [computer_choice_1, computer_choice_2]

    print("Player chooses:", listChoices[0], "and", listChoices[1])
    print("Computer chooses:", computer[0], "and", computer[1])

    # Player selects one of their choices
    choice = input(f"Which would you like to pick? 1. {listChoices[0]} or 2. {listChoices[1]}? ")
    
    if choice == '1':
        selected_move = listChoices[0]
    elif choice == '2':
        selected_move = listChoices[1]
    else:
        print("Invalid selection!")
        continue

    # Compare with one of the computer's choices
    computer_final_choice = computer[randint(0, 1)]
    print(compare(selected_move, computer_final_choice))

    # Update Markov Chain
    if last_move is not None:
        transition_counts[last_move][selected_move] += 1
    last_move = selected_move  # Update the last move

    tries -= 1
    print("You have", tries, "tries left.")