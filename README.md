# T1A3 Terminal Application Assignment
Coder Academy Term 1 Assignment 3
### Student: Fabian Sugandhi

[Github Repository](https://github.com/FabSugandhi/FabianSugandhi_T1A3)

[Source Control Repository](https://github.com/FabSugandhi/FabianSugandhi_T1A3/commits/main)

[Implementation Plan](https://github.com/users/FabSugandhi/projects/2/views/1)

## Style Guide

This terminal application is made to follow coding conventions set out in [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code (van Rossum, et. al., 2023) as close as possible. [Pylint](https://pypi.org/project/pylint/) and its [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) has also been used to help maintain adherence to PEP 8 (LogiLab & Pylint Contributors, 2023).
While PEP 8 suggested that codes are limited to 79 characters per lime, some of the code lines in this application might be longer than this recommendation. This is a done on purpose, as they would either not make as much sense or not function as intended should they be separated into multiple lines to conform to the PEP 8 recommendation.

## Features & Functions

This Connect Four terminal application is designed to allow users to play the traditional "Connect Four™" game created by Hasbro Inc. (Hasbro, 2024) with added features and functionality to suit the virtual environment.

### Connect Four Match

The main feature of this terminal application. It generates a "Connect Four™" (Hasbro, 2024) board and its corresponding game pieces which will then be used in a 2-player match of the game. 

The match follows the established rule of the traditional "Connect Four™" (Hasbro, 2024) game, which involves:
- Standard-sized game board, consisting of 7 columns and 6 rows.
- Winning condition of stacking 4 game pieces consecutively (either horizontally, vertically, or diagonally).
- Game draw condition of filling out the whole board without having any player reaching the winning condition.
- The game flow which consists of players taking turns dropping their pieces on the board. This is done by inputting the intended column number. This game flow will continue until either one player achieves the winning condition or the game draw condition is met.

Once a game is completed, the winning board will be shown and the match result will be shown and recorded into the user accounts. The players are then given the option to restart the game with a fresh board or go back to the main menu.

### User Account System

