# BattleRobots!

add link to source control repo

## Table of Contents

Create links to below contents

- About
- User Interaction and Experience
- Control Flow Diagram
- Implementation Plan
- Testing
- Related Documents
- References (if required)
- Resources
- Tech Stack

## About

### Statement of Purpose

### Features

#### BattleRobot Design

#### Single-Player Mode

#### Multi-Player Mode

#### Random Map Interaction

### Audience

## User Interaction and Experience

Add photos of game and text

## Control Flow Diagram

![Control Flow Diagram for BattleRobot Design](/docs/BattleRobots%20Control%20Flowchart.png)

## Implementation Plan

Add photo of Trello Board

Add link to Trello Board

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

## Related Documents

Add development log (time permitting)

Add help documents

## References (if required)

## Resources

imported modules

ascii art

## Tech Stack

languages used

include coding style and styling conventions
