# Project 1: Writing Loops & Sequences
Please complete the following 2 functions. You can test by running the `pytest` or `python3` commands:

* To run just the main code for one problem: `python3 hello.py`
* To run the tests prior to submission: `pytest hello_test.py`

You **SHOULD NOT** modify `hello_test.py`.
You **SHOULD** implement your problem solutions in `hello.py`.

## Problem 1: squared_sum

Write a function ```squared_sum``` that takes an array of numbers as a parameter and returns the sum of each number in the array squared:

| **Example call** | **Returns** |
| -------------- | --------- |
| `squared_sum ([])` | `0` |
| `squared_sum ([5, -2, 3])` | `38` |
| `squared_sum ([-3, 4])` | `25` |
| `squared_sum ([7, -1, 15, 0])` | `275` |

_**Hint**: use the accumulator / aggregator pattern of a variable & for loop over a range_

## Problem 2: mix

Write a function `mix` that takes two strings as parameters and returns one string with the first element from the first string, and the second element from the second string, and every other element thereafter.

| **Example call** | **Returns** |
| -------------- | --------- |
| `mix(hello, there)` | `htehlelroe` |
| `mix(1234, abcd)` | `1a2b3c4d` |
| `mix(12, abcd)` | `1a2bcd` |
| `mix(1234, ab)` | `1a2b34` |

_**Hints**:_
* Just try to print the strings in the right order first, then worry about returning 
* What happens if one string is longer than the other? There are two approaches:
  * Loop over the shortest string & then loop over the longest string
  * Loop over the longest string & have an if inside the loop for the shorter string
* If you put your ifs inside your loop (I recommend using a while), your solution can be under 10 lines long!

## Getting started

### Develop online

After accepting the assignment, import (or clone) your project repo into an online IDE such as repl.it or vs code. Edit the file. To run, see the commands below.

### Develop in PyCharm

With this option, you can develop on your laptop. You will need to install PyCharm (or another IDE) and git. PyCharm has some built-in git support.

## Testing
The tests are failing right now because the functions aren't outputting the correct information. Fixing this up will make the tests green.

### Setup
To use pytest on repl.it, install it first:

`pip3 install pytest`

To install pytest on the command line for running on a laptop (using a linux or unix based command-line like MacOS):

`sudo -H pip3 install pytest`

If using PyCharm, you may need to fix your project setup.
- Open the **Settings/Preferences | Tools | Python Integrated Tools** settings dialog.
- In the Default test runner field select **pytest**.
- Click OK to save the settings.

### Run commands
To run just your main code:
`python3 hello.py`

To run all the tests:
`pytest`

If an error shows saying it's not on PATH try:
`python -m pytest` 

### Submitting
Commit & push your repo! Make sure your changes are reflected in `main`. 
Run your tests online to verify that your project is complete, then move your ticket on the project board to "Ready for Review" for feedback. 

To run your tests online:
- Go to the `Actions` tab here on github
- Select the `Autograding Tests` workflow
- Under the `Run workflow` dropdown, select the green `Run workflow` button
- Wait for the tests to finish (usually around 30 seconds)
- If green - Great! you passed _all_ pytests in the project. Proceed to move your project to be reviewed
- Else if red, then there is a failing test in your project somewhere! Ask for help in finding the error
