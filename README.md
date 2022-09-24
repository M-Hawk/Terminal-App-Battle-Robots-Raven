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
|**Single Player Menu Select allows User to enter Name** | User can enter a non empty string name, that allocates name to player object. | If user enters empty string they are prompted to re-enter name, otherwise works as expected  | The "escape" key allows user to enter name as blank, if enough escape characters entered, removes first character off string displayed in next screen.
|**Multi Player Menu Select allows both Users to enter Name** | Users can enter a non empty string name, that allocates name to each players object. | If users enter empty string or same name they are prompted to re-enter name, otherwise works as expected  | The "escape" key allows user to enter name as blank.

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
