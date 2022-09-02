# Dicetistics

A simple tool to do statistics using dice for board games.

## How to run Dicetistics?

### Using the Windows executable

Double click on the file `Dicestistics.exe` and a terminal window will appear.

### Using Python

Python 3 is required, use the following command in the root folder of this repository:

    $ python ./automated_rolls.py


## Use a script file to launch many tests in one execution

Each line of the script file is a configuration of one test.

Here is the template of what a line look likes:

    output_file_name;nb_faces;nb_dices;nb_repeat;custom?(y,n);0;1;2;3;4;

Then here is an example of file content:

    test1;5;1;1000;n;
    test2;6;2;1000;y;0;0;0;0;1;1;

The `input_file.txt` file is an example provided to launch several tests in a row.

## Generate a Windows executable

    python -m PyInstaller --onefile '.\automated_rolls.py'

