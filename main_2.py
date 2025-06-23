import random

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def get_result(user, computer):
    if user == computer:
        return "Draw!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("🐍 Snake 🧴 Water 🔫 Gun Game")
    user_score = 0
    comp_score = 0

    while True:
        print("\nChoose one: snake, water, gun (or 'exit' to quit)")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'exit':
            print("Game Over!")
            print(f"Final Score → You: {user_score} | Computer: {comp_score}")
            break

        if user_choice not in ['snake', 'water', 'gun']:
            print("Invalid choice, try again.")
            continue

        comp_choice = get_computer_choice()
        print(f"Computer chose: {comp_choice}")

        result = get_result(user_choice, comp_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            comp_score += 1

        print(f"Score → You: {user_score} | Computer: {comp_score}")

if __name__ == "__main__":
    main()
