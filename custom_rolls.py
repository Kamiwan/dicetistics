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

    def display_hist(self):
        max_face = np.max(self.dice.get_custom_faces())
        
        fig, ax = plt.subplots()
        counts, bins, bars = ax.hist(self.raw_result, bins=np.arange(0,max_face*self.dice_nb+2)) # linewidth=0.5, edgecolor="white"
        ax.set(xlim=(0, max_face*self.dice_nb+1),xticks=np.arange(0, max_face*self.dice_nb+1))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        title = "Histograms for rolling " + str(self.dice_nb) + " dice of " + str(self.dice.face_nb) + " faces " + str(self.roll_nb) + " times."
        title = title + "\n dice faces = " + str(self.dice.custom_faces)
        plt.title(title, loc='center')
        plt.xlabel('Roll value')
        plt.ylabel('Amount of roll')

        self.display_stats_on_hist(fig, ax)
        self.display_perc_on_hist(ax, counts, bins)

        plt.show()
        
    def display_stats_on_hist(self, fig, ax):
        """
        dd
        """
        max_face = np.max(self.dice.get_custom_faces())
        moy = np.mean(self.raw_result)
        std = np.std(self.raw_result)
        top = int(np.max(ax.get_ylim()))
        mean_str = "mean = " + str(np.around(moy, 3))
        std_str = r"$\sigma$ = " + str(np.around(std, 3))
        gap_str = str(int(moy-std)) + "< 68% of values < " + str(int(moy+std))
        gap_2str = str(int(moy-(std*2))) + "< 95% of values < " + str(int(moy+(std*2)))

        plt.text(max_face*self.dice_nb-1, top*0.9, mean_str, size=15, color='purple')
        plt.text(max_face*self.dice_nb-1, top*0.8, std_str, size=15, color='purple')
        plt.text(max_face*self.dice_nb-1, top*0.7, gap_str, size=10, color='purple')
        plt.text(max_face*self.dice_nb-1, top*0.6, gap_2str, size=10, color='purple')

    def display_perc_on_hist(self, ax, counts, bins):
        for i in range(len(counts)):
            ax.text(x=bins[i]+0.5, y=counts[i],
                s="{}%".format(np.around(counts[i]/self.roll_nb*100, 3)),
                ha='center')

def main():
    print("=== Dicestistics tool! ===")
    face = int(input("How many faces for you dice: "))
    dice_nb = int(input("How many dice to roll in the same time: "))
    rolls = int(input("How many times do you want to repeat the roll: "))

    custom_dice = Dice(face)

    req_custom_face = input("Do you want to customize dice faces? (y:yes n:no)")
    if req_custom_face == "y":
        custom_dice.set_custom_faces_term()
    elif req_custom_face == "n":
        print("No custom faces, got it.")
    else:
        print("Wrong answer, classic faces used.")

    test = CustomRoll(dice_nb, custom_dice, rolls)
    test.roll_all()
    test.display_hist()
 
if __name__ == "__main__":
    main()


## TODO
##
## [x] 1. put graphics display their in own methods
## [x] 2. add percentage of each histogram bar 
## [x] 3. add method to allow user to enter his custom dice with terminal
## [ ] 4. add comments to the code (check python system)
## [ ] 5. add Licence / Changelog
## [x] 6. use pylint to clean the code
## [ ] 7. create a windows executable
## [ ] 8. Update readme to allow user to execute program
##
