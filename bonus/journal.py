date = input("Enter today's date")
mood = input("Enter your mood from 1 - 10")
thoughts = input("How was your day today:")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(f"Your mood was: {mood}" + 1 * "\n")
    file.write(f"Your thought for that day: {thoughts}" + 1 * "\n")
