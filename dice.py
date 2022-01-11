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

    def display_hist(self):
        fig, ax = plt.subplots()
        ax.hist(self.last_roll, bins=np.arange(0,self.face_nb+2), linewidth=0.5, edgecolor="white")
        ax.set(xlim=(0, self.face_nb+1),xticks=np.arange(0, self.face_nb+1))
        title = "Histograms for rolling a dice of " + str(self.face_nb) + " faces " + str(len(self.last_roll)) + " times."
        title = title + "\n dice faces = " + str(self.custom_faces)
        plt.title(title, loc='center')
        plt.xlabel('Roll value')
        plt.ylabel('Amount of roll')
        plt.show()


def main():
    print("=== Dicestistics tool! ===")
    face = int(input("How many faces for you dice: "))
    rolls = int(input("How many times do you want to roll the dice: "))

    custom_dice = np.array([0,0,0,0,1,1])
    a = Dice(face, custom_dice)
    a.roll(rolls)
    a.display_hist()
 
if __name__ == "__main__":
    main()