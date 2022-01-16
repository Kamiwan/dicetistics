#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from dice import Dice

class CustomRoll:
    """CustomRoll class

    This class allows to roll several identical ``Dice`` to perform statistics on many rolls.
    This helps to determine the data spread of a specific combination of rolls. Thus, the 
    user can adapt its roll configuration to have the desired data spread for its game design.

    Attributes:
        dice_nb (int): The amount of dice used in one roll.
        roll_nb (int): The amount of roll configured.
        dice (Dice): The Dice object used. See Dice class documentation.
        raw_result (ndarray, dtype=int): Array that stores results of the last set of rolls.

    Example:
        Basic use of the class also described in the main function of this file::

            face = int(input("How many faces for you dice: "))
            dice_nb = int(input("How many dice to roll in the same time: "))
            rolls = int(input("How many times do you want to repeat the roll: "))

            custom_dice = Dice(face)

            test = CustomRoll(dice_nb, custom_dice, rolls)
            test.roll_all()
            test.display_hist()
    """

    def __init__(self, dice_nb, dice, roll_nb):
        """Inits the CustomRolls class.
        
        Args:
            dice_nb (int): The amount of dice used in one roll.
            dice (Dice): The Dice object used. See Dice class documentation.
            roll_nb (int): The amount of roll configured.
        """
        self.dice_nb = dice_nb
        self.roll_nb = roll_nb
        self.dice = dice
        self.raw_result = 0

    def roll_all(self):
        """Performs all rolls with the configured Dice setup.
        
        When more than one dice is used in one roll, the sum of all dice value is computed and considered as one result.
        Example, if we roll 2 dice of 6 faces 4 times the content of ``raw_result`` may be [7, 12, 4, 9].
        """
        self.raw_result = np.zeros(shape=(self.roll_nb), dtype=int)
        for i in range(len(self.raw_result)):
            self.raw_result[i] = self.dice.roll(self.dice_nb).sum()

    def display_hist(self):
        """Generates and display a bar chart with the content of the attribute ``raw_result``.
        
        Some statistics data are also printed with the percentage of each bar.
        """
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

        self.display_stats_on_hist(ax)
        self.display_perc_on_hist(ax, counts, bins)

        plt.show()
        
    def display_stats_on_hist(self, ax):
        """Computes statistics on the current bar chart and write them on the plot.
        
        The mean, the standard deviation are computed. Besides, 68% and 95% gap values are 
        computed.

        Args:
            ax (matplotlib.axes._subplots.AxesSubplot): The matplotlib subplot to write on.
        """
        moy = np.mean(self.raw_result)
        std = np.std(self.raw_result)
        top = int(np.max(ax.get_ylim()))
        mean_str = "mean = " + str(np.around(moy, 3))
        std_str = r"$\sigma$ = " + str(np.around(std, 3))
        gap_str = str(int(moy-std)) + "< 68% of values < " + str(int(moy+std))
        gap_2str = str(int(moy-(std*2))) + "< 95% of values < " + str(int(moy+(std*2)))

        ax.text(1, top*0.9, mean_str, size=15, color='purple')
        ax.text(1, top*0.8, std_str, size=15, color='purple')
        ax.text(1, top*0.7, gap_str, size=10, color='purple')
        ax.text(1, top*0.6, gap_2str, size=10, color='purple')

    def display_perc_on_hist(self, ax, counts, bins):
        """Writes on a matplotlib bar chart the percentage of each bar.
        
        Args:
            ax (matplotlib.axes._subplots.AxesSubplot): The matplotlib subplot to write on
            counts (ndarray): Amount of occurrence of each bins (y-axis).
            bins (ndarray): Column values of the hist graph (x-axis).
        """
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
    print(test.__doc__)
    help(test.display_hist())
 
if __name__ == "__main__":
    main()


## TODO
##
## [x] 1. put graphics display their in own methods
## [x] 2. add percentage of each histogram bar 
## [x] 3. add method to allow user to enter his custom dice with terminal
## [x] 4. add comments to the code (check python system)
## [x] 5. add Licence / Changelog
## [x] 6. use pylint to clean the code
## [x] 7. create a windows executable
## [ ] 8. Update readme to allow user to execute program
##
