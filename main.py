import random

user_score = 0
computer_score = 0

choices_dict = {"r": "🪨 Rock", "p": "📄 Paper", "s": "✂️ Scissors"}

print("🎮 Welcome to Rock-Paper-Scissors!")
print("Type 'q' to quit the game anytime.\n")

while True:
    computer_choice = random.choice(["r", "p", "s"])
    your_choice = input("Choose (r = Rock, p = Paper, s = Scissors, q = Quit): ").lower()

    if your_choice == "q":
        print("\n👋 Game ended. Final Score:")
        print(f"🧍 You: {user_score} | 🤖 Computer: {computer_score}")
        break

    if your_choice not in choices_dict:
        print("❌ Invalid input! Please enter 'r', 'p', 's', or 'q'.")
        continue

    print(f"\n🧍 You chose: {choices_dict[your_choice]}")
    print(f"🤖 Computer chose: {choices_dict[computer_choice]}")

    if your_choice == computer_choice:
        print("🤝 It's a draw!")
    elif (your_choice == "r" and computer_choice == "s") or \
         (your_choice == "p" and computer_choice == "r") or \
         (your_choice == "s" and computer_choice == "p"):
        print("🏆 You win this round!")
        user_score += 1
        computer_score -= 1
    else:
        print("😢 You lose this round!")
        computer_score += 1
        user_score -= 1

    print(f"📊 Score — You: {user_score} | Computer: {computer_score}\n")

if computer_score > user_score:
    print("🤖 Computer wins the game!")
elif user_score > computer_score:
    print("🧍 You win the game!")
else:
    print("🤝 It's a tie overall!")


    
