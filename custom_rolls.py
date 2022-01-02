import sys
import numpy as np
import matplotlib.pyplot as plt

from dice import Dice

class CustomRoll:
    def __init__(self, dice_nb, face_nb, roll_nb):
        self.dice_nb = dice_nb
        self.roll_nb = roll_nb
        self.dice = Dice(dice_nb)
        self.raw_result = 0

    def roll_all(self):
        self.raw_result = np.zeros(shape=(self.roll_nb), dtype=int)
        for i in range(len(self.raw_result)):
            self.raw_result[i] = self.dice.roll(self.dice_nb).sum()
            print(self.raw_result[i])
        print(self.raw_result)

def main():
    print("Hello world!")
    face = int(input("How many faces for you dice: "))
    dice_nb = int(input("How many dice to roll in the same time: "))
    rolls = int(input("How many times do you want to repeat the roll: "))

    test = CustomRoll(dice_nb, face, rolls)
    test.roll_all()

    # plot
    x = test.raw_result
    fig, ax = plt.subplots()
    ax.hist(x, bins=np.arange(1,face*dice_nb+2), linewidth=0.5, edgecolor="white")
    ax.set(xlim=(1, face*dice_nb+1),xticks=np.arange(1, face*dice_nb+1))
    plt.show()
 
if __name__ == "__main__":
    main()
