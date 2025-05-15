import random

print("Welcome to the 🪨 Rock, 📄 Paper, ✂️ Scissors Game!")
choices = {"r": "🪨 Rock", "p": "📄 Paper", "s": "✂️ Scissors"}

user = input("🎯 Enter your choice (r for 🪨, p for 📄, s for ✂️): ").lower()
if user not in choices:
    print("❌ Invalid choice!")
else:
    computer_choice = random.choice(["r", "p", "s"])

    print(f"🤖 Computer chose: {choices[computer_choice]}")
    print(f"🧍 You chose: {choices[user]}")

    if user == computer_choice:
        print("🤝 It's a tie!")
    elif (user == "r" and computer_choice == "s") or \
         (user == "p" and computer_choice == "r") or \
         (user == "s" and computer_choice == "p"):
        print("🏆 You win!")
    else:
        print("😢 You lose!")


