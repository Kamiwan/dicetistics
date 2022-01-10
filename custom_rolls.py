import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from dice import Dice

class CustomRoll:
    def __init__(self, dice_nb, dice, roll_nb):
        self.dice_nb = dice_nb
        self.roll_nb = roll_nb
        self.dice = dice
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

    custom_faces = np.array([0,0,0,0,1,1])
    custom_dice = Dice(face, custom_faces)
    max_face = np.max(custom_faces)
    test = CustomRoll(dice_nb, custom_dice, rolls)
    test.roll_all()

    # plot
    x = test.raw_result
    
    moy = np.mean(x)
    std = np.std(x)
    print("moyenne = " , moy)
    print("ecart type = " , std)

    print(x)
    print(np.max(x))

    fig, ax = plt.subplots()
    ax.hist(x, bins=np.arange(0,face*dice_nb+2)) # linewidth=0.5, edgecolor="white"
    ax.set(xlim=(0, max_face*dice_nb+1),xticks=np.arange(0, face*dice_nb+1))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    title = "Histograms for rolling " + str(dice_nb) + " dice of " + str(face) + " faces " + str(rolls) + " times."
    title = title + "\n dice faces = " + str(custom_faces)
    plt.title(title, loc='center')
    plt.xlabel('Roll value')
    plt.ylabel('Amount of roll')
    plt.grid(axis="y")
    
    top = int(np.max(ax.get_ylim()))
    print(top)
    #plt.text(1,top*0.9,r'$\mu=100,\ \sigma=15$')
    mean_str = "mean = " + str(np.around(moy, 3))
    std_str = "$\sigma$ = " + str(np.around(std, 3))
    gap_str = str(int(moy-std)) + "< 68% of values < " + str(int(moy+std))
    gap_2str = str(int(moy-(std*2))) + "< 95% of values < " + str(int(moy+(std*2)))
    plt.text(0, top*0.9, mean_str, size=15, color='purple')
    plt.text(0, top*0.8, std_str, size=15, color='purple')
    plt.text(0, top*0.7, gap_str, size=10, color='purple')
    plt.text(0, top*0.6, gap_2str, size=10, color='purple')


    plt.show()
 
if __name__ == "__main__":
    main()
