from numpy import random  # Using NumPy random

# Dice faces stored in a dictionary
dice_faces = {
    1: [
        "-----------",
        "|         |",
        "|    0    |",
        "|         |",
        "-----------"
    ],
    2: [
        "-----------",
        "|         |",
        "| 0     0 |",
        "|         |",
        "-----------"
    ],
    3: [
        "-----------",
        "|    0    |",
        "|    0    |",
        "|    0    |",
        "-----------"
    ],
    4: [
        "-----------",
        "| 0     0 |",
        "|         |",
        "| 0     0 |",
        "-----------"
    ],
    5: [
        "-----------",
        "| 0     0 |",
        "|    0    |",
        "| 0     0 |",
        "-----------"
    ],
    6: [
        "-----------",
        "| 0  0  0 |",
        "|         |",
        "| 0  0  0 |",
        "-----------"
    ]
}

def roll_dice():
    number = random.randint(1, 7)  # 1 to 6 (upper bound exclusive)
    for line in dice_faces[number]:
        print(line)

print("                         Dice Simulator                  ")

while True:
    roll_dice()
    choice = input("Do you want to play again (y/n): ").lower()
    if choice == "n":
        break
