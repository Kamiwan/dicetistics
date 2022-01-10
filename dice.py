import sys
import numpy as np
import matplotlib.pyplot as plt

class Dice:
    def __init__(self, face_nb, custom_faces=None):
        self.face_nb = face_nb
        self.last_roll = 0
        if np.any(custom_faces == None) :
            self.custom_faces = np.arange(10, dtype=int)
        else:
            self.custom_faces = custom_faces

    def roll(self, nb_rolls):
        self.last_roll = self.custom_faces[np.random.randint(low=0, high=self.face_nb, size=nb_rolls)]
        return self.last_roll

    def set_custom_faces(self, custom_faces):
        self.custom_faces = custom_faces

    def get_custom_faces(self):
        return self.custom_faces


def main():
    print("=== Dicestistics tool! ===")
    face = int(input("How many faces for you dice: "))
    rolls = int(input("How many times do you want to roll the dice: "))
    custom_dice = np.array([0,0,0,0,1,1])
    a = Dice(face, custom_dice)
    a.roll(rolls)
    
    # plot
    x = a.last_roll
    fig, ax = plt.subplots()
    ax.hist(x, bins=np.arange(0,face+2), linewidth=0.5, edgecolor="white")
    ax.set(xlim=(0, face+1),xticks=np.arange(0, face+1))
    plt.show()
 
if __name__ == "__main__":
    main()