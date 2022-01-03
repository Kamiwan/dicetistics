import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from dice import Dice

class CustomRoll:
    def __init__(self, dice_nb, face_nb, roll_nb):
        self.dice_nb = dice_nb
        self.roll_nb = roll_nb
        self.dice = Dice(face_nb)
        self.raw_result = 0

    def roll_all(self):
        self.raw_result = np.zeros(shape=(self.roll_nb), dtype=int)
        for i in range(len(self.raw_result)):
            self.raw_result[i] = self.dice.roll(self.dice_nb).sum()

def main():
    print("=== Dicestistics tool! ===")
    face = int(input("How many faces for you dice: "))
    dice_nb = int(input("How many dice to roll in the same time: "))
    rolls = int(input("How many times do you want to repeat the roll: "))

    test = CustomRoll(dice_nb, face, rolls)
    test.roll_all()

    # plot
    x = test.raw_result
    
    moy = np.mean(x)
    std = np.std(x)
    print("moyenne = " , moy)
    print("ecart type = " , std)

    fig, ax = plt.subplots()
    ax.hist(x, bins=np.arange(1,face*dice_nb+2)) # linewidth=0.5, edgecolor="white"
    ax.set(xlim=(1, face*dice_nb+1),xticks=np.arange(1, face*dice_nb+1))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    title = "Histograms for rolling " + str(dice_nb) + " dice of " + str(face) + " faces " + str(rolls) + " times."
    plt.title(title, loc='center')
    plt.xlabel('Roll value')
    plt.ylabel('Amount of roll')
    plt.grid(axis="y")
    
    top = int(np.max(ax.get_ylim()))
    print(top)
    #plt.text(1,top*0.9,r'$\mu=100,\ \sigma=15$')
    mean_str = "mean = " + str(np.around(moy, 3))
    std_str = "$\sigma$ = " + str(np.around(std, 3))
    gap_str = str(int(moy-(std*2))) + "< 95% of values < " + str(int(moy+(std*2)))
    plt.text(1, top*0.9, mean_str, size=15, color='purple')
    plt.text(1, top*0.8, std_str, size=15, color='purple')
    plt.text(1, top*0.7, gap_str, size=10, color='purple')


    plt.show()
 
if __name__ == "__main__":
    main()
