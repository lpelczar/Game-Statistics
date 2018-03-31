# Game Statistics

## Story

You are a happy programmer at a big game developer company, named "ID Software". Judy, your statistician colleague, asks help from you in a competitor evaluation project. She has a data file with a lot of statistical information about famous games of all time. Judy has some unanswered questions about the games. She need you to write a program that can answer these questions.

## Description

Your task is to write reports that answer Judy's questions. Every report need to be implemented as a function so every function is related to a question. For every report function you need to write a printer function also. The printer function has to pretty print the return value(s) of the report function.

The name of the input file is game_stat.txt. You can find it in the repository.

Every line in the file contains the following information about a game:

- title
- total copies sold (million)
- release date
- genre
- publisher
These are the properties of a game. Properties are separated by a tab character and lines are separated by line break characters. You need to pay attention these special characters when you read the file.

The first line:
Minecraft->23->2009->Survival game->Microsoft↲

## Expectations

Every report function:

- has to be named properly (as you see in the Questions section)
- must NOT contain printing to console
- returns only the asked information
- should run in any order
- has one dependency: the input file
- has to be prepared for any other data files (not just the game_stat.txt) within the same structure

You need to write your project into 3 source files:

- reports.py: write only the report functions in it.
- printing.py: for printing the output of the report functions. You can use this to test your solutions.
- export.py: for exporting the reports into a single export file. By running this program Judy will get a single text file with all the answers she needs (you should export only the answers line by line, Judy will know the questions).

## More info

Project made for [Codecool](https://codecool.com/) programming course.
