# The Hero Game

## Overview
The Hero Game is an exciting text-based battle game where you play as a hero fighting against a formidable enemy. This Python-based game showcases object-oriented programming principles and provides an interactive combat experience.

## Features
- Character-based gameplay with distinct Hero and Enemy classes
- Turn-based combat system
- Random damage calculation for realistic battle outcomes
- Special attack ability for the Hero
- Detailed character information display

## How to Play
1. Run the game by executing `the-hero-game.py`
2. The game starts with Batman (Hero) vs Joker (Enemy)
3. Each turn, you can choose between:
   - Regular Attack
   - Special Attack (Bat-rang)
4. The enemy attacks automatically after your turn
5. The battle continues until one character is defeated
6. The last character standing wins the game

## Code Structure
- `Character`: Base class for all characters
- `Hero`: Subclass of Character with special attack ability
- `Enemy`: Subclass of Character with a specific kind
- `Game`: Orchestrator class that manages the game flow

## Technical Highlights
- Encapsulation using private attributes
- Inheritance demonstrating OOP principles
- Random number generation for attack damage
- User input handling for interactive gameplay

## Get Started
Clone the repository and run the Python script to embark on your heroic journey!

```python
python the-hero-game.py