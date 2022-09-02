#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from dice import Dice
import custom_rolls
from custom_rolls import CustomRoll

INDEX_OUTPUT_NAME = 0
INDEX_FACES = 1
INDEX_NB_DICES = 2
INDEX_NB_REPEAT = 3
INDEX_CUSTOM_DICE_REQUEST = 4
INDEX_CUSTOM_VALUES = 5

def convert_custom_faces(parsed_line):
    array_size = len(parsed_line)
    array = np.empty(len(parsed_line), dtype='int')
    for i in range(0,array_size):
        array[i] = int(parsed_line[i])
    return array


def line_parsing(script_filename):
    print("line parsing")
    with open(script_filename) as f:
        lines = f.readlines()
        for current_line in lines:
            test_string = current_line.split(";")

            if test_string[INDEX_CUSTOM_DICE_REQUEST] == 'n':
                dice = Dice(int(test_string[INDEX_FACES]))
            else:
                custom_faces_array = convert_custom_faces(test_string[INDEX_CUSTOM_VALUES:-1])
                dice = Dice(int(test_string[INDEX_FACES]), custom_faces_array)

            current_test = CustomRoll(int(test_string[INDEX_NB_DICES]), dice, int(test_string[INDEX_NB_REPEAT]))
            current_test.roll_all()
            current_test.display_hist()


def main():
    print("=== Dicestistics Scripts! ===")
    
    req_custom_face = input("Do you want to use a script file for automated tests? (y:yes n:no)")
    if req_custom_face == "y":
        script_filename = input("Please enter the name of the input file: ")
        line_parsing(script_filename)
    else:
        print("Manual mode selected.")
        custom_rolls.main()
    
    input("Press [enter] to continue.")


if __name__ == "__main__":
    main()
