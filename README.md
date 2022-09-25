# BattleRobots!

[Battle Robots Github Repository](https://github.com/M-Hawk/MatthewHawkins_T1A3)

## Table of Contents

- About
- Features
- Audience
- User Interaction and Experience
- Control Flow Diagram
- Implementation Plan
- Testing
- User Help Document
- Installation Instructions
- Resources
- Tech Stack
- Author

## About

Battle Robots is a Game that allows up to two players to design their own Battle Robot using Body or Weapon components, they then battle each other in an Arena to determine the winner. There is also a Single Player mode that allows one player to battle an AI player using a randomly designed Robot.

## Features

### Battle-Robot Design

Battle Robots allows players to battle each other using up to 3 selectable Body Types and 3 selectable Weapon Types.

The available Body Types are "Tracked", "Soft-Wheeled" and "Hard-Wheeled".

Each body type is Strong or Weak vs particular Weapon Types.

The available Weapon Types are the "Electrocutor", "Powersaw" and "Flipper".

Each weapon type is Strong or Weak vs particular Weapon Types.

Full details provided in Help Document.

### Single-Player Mode

Single Player Mode allows an individual to play against a randomly generated AI Player that selects a random name and components from a list.

Players can then battle the AI Player in the Arena, players take turns attacking each others Body or Weapon Components, when a players health falls to 0 they lose.

### Multi-Player Mode

Multi Player Mode allows two Human Players to Battle it out for dominance using their own self designed Battle Robot.

Players take turns selecting Body Type and Weapon Type.

Players then battle it out in the Arena taking turns attacking each other Body or Weapon Components, when a players health falls to 0 they lose.

### Random Arena Effects

Players can opt to add Arena Effects to any given Game.

Arena effects allow players to select an extra attack that interacts with the Battle Arena and damages the opposing players Battle Robot.

Players also have a random chance of taking damage from the Arena's own Weaponry.

## Audience

This Game was designed primarily for gamers, friends and anyone looking to try out a basic terminal game to battle each other in a fun and interesting way.

## User Interaction and Experience

Full details of the game experience, including interaction, user interface and damage details are provided in the Help Document provided in this README, link in headings.

### **Intro Screen**

![Battle Robots Intro Screen](/docs/br_intro.png)

### **Main Menu**

![Battle Robots Main Menu](/docs/br_mainmenu.png)

### **AI Battle Robot Generated**

![Battle Robots AI Select Screen](/docs/br_aiselect.png)

### **Arena Effects Screen**

![Battle Robots Arena Effects Screen](/docs/br_arenaeffects.png)

### **Versus Screen**

![Versus Screen](/docs/br_versus.png)

### **Attack Roll Screen**

![First Attack Roll Screen](/docs/br_roll.png)

### **Battle Screen**

![Battle Screen](/docs/br_battle.png)

### **Victory Screen**

![Victory Screen](/docs/br_victory.png)

## Control Flow Diagram

![Control Flow Diagram for BattleRobot Design](/docs/br_controlflow.png)

## Implementation Plan

[Trello Board](https://trello.com/b/YB6Y2VwP/t1a3)

![Trello Board Progress](/docs/trello_progress.png)

## Testing

For the testing of this application I implemented a manual testing approach. These tests focused on menu stack methods called each other correctly, whether user input was entered correctly and as expected, AI player selected correct attributes, first attacking player random roll worked correctly, user toggled Arena effects acted as designed and damage dealt was deducted correctly. These tests were carried out by myself and my partner. The table provided below describes in detail the results.

| Feature                    | Expected Outcome                     | Actual Outcome | Issues Encountered |
|---------|------------------|----------------|--------------------|
|**Intro Screen Display** | Intro screen clears terminal then displays appropriate red font message. | User able to type into terminal, which affects message position, works as expected. | If excessive input typed it can disrupt font display by skewing, doesn't affect funtionality.
|**Main Menu Screen** | Game Title in red font. Main menu displays a column of selectable entries "Single Player", "Multi Player", "Exit Game". | Menu loads as expected, user unable to type into terminal, works as expected. | The "escape" key caused a TypeError previously, handled
|**Body Type and Weapon Menu's Able to Return to Main Menu** | When Main Menu is selected in Body Type or Weapons Menu the Game returns to the Main Menu, resetting all flags options used. | As expected. | Nil.
|**Single Player Menu Select allows User to enter Name** | User can enter a non empty string name, that allocates name to player object. | If user enters empty string they are prompted to re-enter name, otherwise works as expected.  | The "escape" key allows user to enter name as blank, if enough escape characters entered, removes first character off string displayed in next screen.
|**Single Player Age Entry** | A valid whole number age is entered and saved to age in player object. | As expected. | Issues resolved catching non integers and negative numbers.
|**Computer Player Created Correctly** | Computer player selects random correct attributes from lists provided. | As expected. | Nil.
|**Body Type Select Menu** | Menu allows each player to select a body type and allocates it to their player object. | If user presses the "escape" key they are promted to select and option. Else as expected. | Nil.
|**Weapon Select Menu** | Menu allows each player to select a weapon and allocates it to their player object. | If user presses the "escape" key they are promted to select and option. Else as expected. | Nil.
|**Versus Screen Loads Correctly** | Player one and two's attributes are displayed correctly on screen | As expected. | Nil.
|**Roll For Player Who Attacks First** | Both players are randomly generated rolls from 1-6 inclusive, the highest value wins. Same roll causes a reroll. |Users can input into terminal, doesn't cause issues. Otherwise as expected. | Nil.
|**Battle Screen Display Correct Information** | Both players information is displayed on screen correclty, with health displayed in colour, and attack menu is available and selectable. | As expected. | Users can press the "escape" key, unintended "please select an option is printed" and are returned to main menu. Could be considered an unintented feature. No fatal issues.
|**Player Damage Calculated Correctly** | Both players health is deducted correctly from calculate from damage rubric and damage methods. Player objects health updated appropriately. | As expected. | Nil.
|**Multi Player Menu Name Select** | Game allows both users to enter name. Users can enter a non empty string name, that allocates name to each players object. | If users enter empty string or same name they are prompted to re-enter name, otherwise works as expected.  | The "escape" key allows user to enter name as blank.
|**Arena Effects Menu Allows Effects in Game** | If "yes" selected, Arena effects are added in game, including an Arena inclusive attack, and Random damage from Arena, if "No selected, No Arena effects in Game. | As expected. | Pressing the "escape" key during select screen causes what ever select is highlighted, to be selected for the game. Minor Issue.
|**Arena Effects Act Correctly** | If player or computer selects Arena attack, random damage between 0-40 inclusive, is deducted from health. Random Arena damage has 25% chance to inflict random damage between 0-20 inclusive each Player turn. | As expected. | Nil.
|**Winning Player is selected correctly** | At end of Player's turn and while both players health is above 0, battle continues. If one players health is 0 or below at end of round, a winner is selected. The player without 0 health is declared the winner. | As expected. | If both players somehow ended up with 0 health at the same time, possibly from random arena attack. Player one is declared victor. Unlikely. Minor Issue

## User Help Document

 [Battle Robots User Help Document](https://github.com/M-Hawk/MatthewHawkins_T1A3/blob/main/docs/help.md)

## Installation Instructions

In order to run this Game please follow the below instructions:

1. Ensure you have the latest version of Python installed on your computer, if not please go [here](https://www.python.org/downloads/).

2. Clone the files from this Repository using the following command into your desired source folder:

    ```bash
    git clone https://github.com/M-Hawk/MatthewHawkins_T1A3.git
    ```

3. Navigate to the src folder where you cloned the repository and change into the src directory using the below code:

    ```bash
    cd src
    ```

4. Now run the executable bash script below, this creates a virtual environment, installs the required packages, then runs the game: ENJOY!

    ```bash
    source run_game.sh
    ```

## Resources

### **Python3 Standard Libray Modules**

OS Module

Time Module

Random Module

### **Python3 Imported Modules**

Colorama Module

Art Module

Simple Term Menu Module

## Tech Stack

Python 3 Version 3.10.4

PEP 8 Standards

## Author

Matthew Hawkins
