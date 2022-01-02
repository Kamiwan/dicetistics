import sys
import numpy as np
import matplotlib.pyplot as plt

#sys.path.append(".")

from dice import Dice


def main():
    print("Hello world!")
    face = int(input("How many faces for you dice: "))
    rolls = int(input("How many times do you want to roll the dice: "))
    a = Dice(face)
    a.roll(rolls)
    
    # plot
    x = a.last_roll
    fig, ax = plt.subplots()
    ax.hist(x, bins=np.arange(1,face+2), linewidth=0.5, edgecolor="white")
    ax.set(xlim=(1, face+1),xticks=np.arange(1, face+1))
    plt.show()
 
if __name__ == "__main__":
    main()