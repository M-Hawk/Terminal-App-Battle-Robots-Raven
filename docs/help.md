# Battle Robots Help Document

This Readme is designed to explain to users how to install and play Battle Robots.

If you have not installed the required files in order to play this Game, please read below.

## Installation

In order to play this game please run the BASH script below in you're terminal.

## Game

### **How to play Battle Robots**

Please note. (The below pictures provided were captured over multiple game playthroughs and may not show consistent player information throughout)

#### **Intro Screen**

Once the game has been executed, you're terminal will clear and you will the result below.

![Battle Robots Intro Screen](/docs/br_intro.png)

#### **Main Menu**

Once the Intro is complete the Main Menu Screen will appear.

Players can select the Single Player, Multi Player or Exit Game options.

Single Player allows you to play against a randomly generated AI Player.

Multi Player allows you to play against a friend.

Exit Game will end the game and close the program.

![Battle Robots Main Menu](/docs/br_mainmenu.png)

### **Single Player Mode**

#### **Age Entry Screen**

If Single Player is selected, the next screen that appears is the Age Entry Screen.

Player is to enter their age in a whole number format.

If a player enters a negative, blank or decimal point number, they will be prompted to enter their age again.

![Battle Robots Age Screen](/docs/br_age.png)

#### **Battle Robot Name Screen**

After a player has selected their age the next screen is the Battle Robot Name Screen.

Player is prompted to enter a name for their Battle Robot.

If the name entered is blank, it will prompt player to enter a non blank name.

Please note. (No meta data is recorded for the duration of the Game)

![Battle Robots Name Screen](/docs/br_name.png)

#### **AI Battle Robot Generated**

After a player has chosen their Battle Robots name, a screen will display a randomly chosen AI Player.

![Battle Robots AI Select Screen](/docs/br_aiselect.png)

#### **Arena Effects Screen**

After an AI Player is selected the Arena Effects Menu will appear.

Players are able to choose whether they would like to have Arena Effects enabled.

If Arena Effects are selected.

Both players have the ability to select an extra attack that interacts with the Battle Arena. This attack deals random damage between (0-40) inclusive.

Arena effects also cause players to have a 25% chance after each attack turn, for a random player to take random damage between (0-20) inclusive, from the Arena's Weapons.

If Arena Effects are not selected.

Players will play the standard version of the game, with only two attacks available.

![Battle Robots Arena Effects Screen](/docs/br_arenaeffects.png)

#### **Body Type Select Screen**

The next screen is the body type select screen which allows each player to select a body type from the below list.

Each player selects sequentially. Note, AI displays selected Components in a later screen.

Body Types are classed as Strong or Weak vs certain Weapons, more information is provided further below in the Damage Chart.

Please note. (Viewing the Damage Chart may reduce the experience of playing the Game)

![Battle Robots Body Select Screen](/docs/br_bodyselect.png)

#### **Weapon Select Screen**

After players have selected their Body Type, the Weapon Select screen appears.

This screen allows players to select a Weapon type from the below list.

Each player selects sequentially. Note, AI displays selected Components in a later screen.

Weapons are classed as Strong or Weak vs certain Weapons and Body Types, more information is provided further below in the Damage Chart.

Please note. (Viewing the Damage Chart may reduce the experience of playing the Game)

![Battle Robots Weapon Select Screen](/docs/br_weaponselect.png)

#### **AI Component Select Screen**

This screen appears momentarily, displaying information about the Components the AI has selected.

AI Components are selected randomly.

![Battle Robots AI Component Select Screen](/docs/br_aicomponent.png)

#### **Versus Screen**

This screen appears momentairly, it displays each players attributes and components selected to the screen.

![Versus Screen](/docs/br_versus.png)

#### **Attack Roll Screen**

After the Versus Screen concludes the Roll Screen appears.

Each player automatically rolls a randomly generated 6 sides dice.

If rolls result in the same number, a reroll occurs.

The player with the highest roll attacks first.

![First Attack Roll Screen](/docs/br_roll.png)

#### **Battle Screen**

After the Roll Screen concludes, the Battle Screen starts.

Players both start with 120 Health

Players take sequential attacks to determine on each others components.

Player who won the roll attacks first.

Players may attack either the opponents Body or Weapon.

If players have Arena Effects on, they may also use the Arena Weapons in the attack.

If players have Arena Effects on, then after a player attacks, any player may randomly take damage from the Arena's Weapons.

Please note. (If a player presses the "escape" key during Battle, they Battle ends and the Game returns to the Main Menu)

![Battle Screen](/docs/br_battle.png)

See below for what an attack may look like on screen

Note the health colour display change.
Health from 80 - 120 is Green, 40 - 79 is Yellow and below 40 is Red.

![Attack In Battle](/docs/br_attack.png)

Below is a player taking damage from an Arena Effect.

![Arena Damage In Battle](/docs/br_arenadmg.png)

#### **Victory Screen**

When a players health falls to or below 0, their opponent is declared the winner.

The game then returns to the Main Menu Screen.

![Victory Screen](/docs/br_victory.png)

### **Multi Player Mode**

Multi Player mode works much the same way as Single Player mode, except the AI Player is substituted with a friend, or enemy.

The Age select screen is omitted for Multi Player mode.

Players both select their Battle Robots Name, then sequentially both select Body Type, then Weapon.

Player One selects both first.

Please see Single Player Mode Description for full details.

### **Damage Chart**

Please note. (Viewing the Damage Chart may reduce the experience of playing the Game)

![Damage Chart](/docs/br_damagechart.png)

### Installation Instructions

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
