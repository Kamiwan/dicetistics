import sys
import numpy as np
import matplotlib.pyplot as plt

class Dice:
    """Dice class

    This class model a dice and its use by rolling it the desired amount of time.
    Results of these rolls are stored in the attribute ``last_roll``. Faces of the
    dice can be customized with any integer values.

    Attributes:
        face_nb (int): The amount of faces of the dice.
        last_roll (ndarray, dtype=int): Array that stores results of the last roll of the dice.
        custom_faces (ndarray, dtype=int): Contain values of each dice faces.

    Example:
        Basic use of the class also described in the main function of this file::

            face = int(input("How many faces for you dice: "))
            rolls = int(input("How many times do you want to roll the dice: "))
            dice = Dice(face)
            dice.roll(rolls)
            dice.display_hist()
    """

    def __init__(self, face_nb, custom_faces=None):
        """Inits the Dice class 
        
        Args:
            face_nb (int): The amount of faces of the dice.
            custom_faces (ndarray, dtype=int, optional): Array that contains values of each dice faces.
        """
        self.face_nb = face_nb
        self.last_roll = 0
        if np.any(custom_faces == None) :
            self.custom_faces = np.arange(start=1,stop=face_nb+1, dtype=int)
        else:
            self.custom_faces = custom_faces

    def roll(self, nb_rolls):
        """Rolls the dice ``nb_rolls`` times.
        
        Args:
            nb_rolls: The amount of times you want to roll the dice.

        Returns:
            last_roll: The attribute with result of each roll executed by the call of this method.
        """
        self.last_roll = self.custom_faces[np.random.randint(low=0, high=self.face_nb, size=nb_rolls)]
        return self.last_roll

    def set_custom_faces(self, custom_faces):
        """Sets custom faces to the dice.
        
        Args:
            custom_faces (ndarray, dtype=int): Array that contains new values of each dice faces.
        """
        self.custom_faces = custom_faces

    def set_custom_faces_term(self):
        """Allows a user to set custom faces of its dice through Terminal interface."""
        for i in range(self.face_nb):
            str_req = "Enter the value of the face " + str(i+1) + " : "
            val_face = int(input(str_req))
            self.custom_faces[i] = val_face

    def get_custom_faces(self):
        """Returns the attribute ``custom_faces`` that stores dice faces."""
        return self.custom_faces

    def display_hist(self):
        """Generates and display a bar chart of occurrences for each face with the last roll."""
        fig, ax = plt.subplots()
        counts, bins, bars = ax.hist(self.last_roll, bins=np.arange(0,self.face_nb+2), linewidth=0.5, edgecolor="white")
        ax.set(xlim=(0, self.face_nb+1),xticks=np.arange(0, self.face_nb+1))
        title = "Histograms for rolling a dice of " + str(self.face_nb) + " faces " + str(len(self.last_roll)) + " times."
        title = title + "\n dice faces = " + str(self.custom_faces)
        plt.title(title, loc='center')
        plt.xlabel('Roll value')
        plt.ylabel('Amount of roll')
        self.display_perc_on_hist(ax, counts, bins)
        plt.show()

    def display_perc_on_hist(self, ax, counts, bins):
        """Writes on a matplotlib bar chart the percentage of each bar.
        
        Args:
            ax (matplotlib.axes._subplots.AxesSubplot): The matplotlib subplot to write on
            counts (ndarray): Amount of occurrence of each bins (y-axis).
            bins (ndarray): Column values of the hist graph (x-axis).
        """
        for i in range(len(counts)):
            ax.text(x=bins[i]+0.5, y=counts[i],
                s="{}%".format(np.around(counts[i]/len(self.last_roll)*100, 3)),
                ha='center')


def main():
    print("=== Dicestistics tool! ===")
    face = int(input("How many faces for you dice: "))
    rolls = int(input("How many times do you want to roll the dice: "))

    dice = Dice(face)
    
    req_custom_face = input("Do you want to customize dice faces? (y:yes n:no)")
    if req_custom_face == "y":
        dice.set_custom_faces_term()
    elif req_custom_face == "n":
        print("No custom faces, got it.")
    else:
        print("Wrong answer, classic faces used.")

    dice.roll(rolls)
    dice.display_hist()
 
if __name__ == "__main__":
    main()