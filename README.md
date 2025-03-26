# Number Guessing Game

A professional-grade number guessing game built with Python, featuring a clean terminal UI and industry-standard practices. This project demonstrates core Python concepts including:
- Object-Oriented Programming
- Error Handling
- User Input Validation
- Time Management
- Score Tracking
- Data Structures
- Logging System
- Configuration Management
- Data Persistence
- Type Hints
- Unit Testing
- Clean Terminal UI

## Features
- Three difficulty levels with different ranges and attempts:
  - Easy (1-50): 15 attempts, 2 hints
  - Medium (1-100): 10 attempts, 1 hint
  - Hard (1-200): 8 attempts, no hints
- Player name tracking
- High score system with persistent storage
- Time tracking
- Score calculation based on attempts and time
- Smart hint system that tells you how close you are
- Achievement system with special rewards:
  - High Scorer: Beat your best score
  - Quick Thinker: Guess in 3 or fewer attempts
  - Speed Demon: Complete in under 10 seconds
- Player statistics tracking
- Clean terminal interface with:
  - ASCII art title
  - Clear status displays
  - Tables and panels
  - Progress indicators
- Comprehensive logging system
- Configuration management
- Data persistence using JSON
- Type hints for better code quality

## Project Structure
```
number_guessing_game/
├── number_guessing_game.py  # Main game file
├── config.py               # Configuration management
├── logger.py              # Logging system
├── data_manager.py        # Data persistence
├── ui_manager.py          # UI components
├── test_game.py           # Unit tests
├── game_config.json       # Game configuration
├── high_scores.json       # High scores data
├── player_stats.json      # Player statistics
└── game.log              # Game logs
```

## How to Play
1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
2. Run the game:
   ```
   python number_guessing_game.py
   ```
3. Enter your name when prompted
4. Choose a difficulty level (1-3)
5. Try to guess the number within the given range
6. Get hints by typing 'h' when prompted (if available)
7. Try to achieve the highest score and unlock achievements!

## Scoring System
- Score is calculated based on:
  - Difficulty level (higher difficulty = higher potential score)
  - Number of attempts (fewer attempts = higher score)
  - Time taken (faster completion = higher score)

## Requirements
- Python 3.x
- tabulate (for table formatting)
- python-dateutil (for date handling)


## Development
This project follows industry-standard practices:
- Modular design with separate concerns
- Comprehensive error handling
- Type hints for better code quality
- Logging system for debugging
- Configuration management
- Data persistence
- Unit testing
- Clean code principles
- Clean and responsive UI 
