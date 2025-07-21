# Yahtzee CLI Game - Implementation To-Do List

## 1. Project Setup
- [x] Set up project structure and main entry point
- [x] Create initial files: `yahtzee.py`, `scorecard.py`, `dice.py`, `cli.py`, `utils.py`
- [x] Set up a `tests/` directory for test files
- [x] Add `pytest` to project requirements (if using a requirements file)

## 2. Data Structures
- [x] Implement `Player` class
- [x] Implement `Scorecard` class
- [x] Define Yahtzee categories (as constants or Enum)
- [x] Implement `Dice` class
- [x] Implement `Game` class (single player, but extensible)

## 3. Game Logic
- [x] Implement dice rolling and re-rolling logic
- [x] Implement scoring logic for all categories
- [x] Implement scorecard updating and validation (category used only once)
- [x] Implement main game loop (13 rounds, per player)

## 4. Command-Line Interface (CLI)
- [x] Implement CLI prompts for player name(s)
- [x] Implement CLI display for dice, scorecard, and categories
- [x] Implement CLI input for dice selection and category choice
- [x] Implement input validation and error handling
- [ ] Implement end-of-game summary and results display

## 5. Testing
- [x] Write unit tests for `Player` class
- [x] Write unit tests for `Scorecard` class
- [x] Write unit tests for `Dice` class
- [x] Write unit tests for scoring logic
- [ ] Write tests for CLI input validation (where possible)
- [ ] Write integration tests for main game loop (optional)

## 6. Extensibility & Extras
- [ ] Refactor for multiplayer support
- [ ] Add high score tracking (optional)
- [ ] Add save/load game feature (optional)
- [ ] Polish CLI user experience (instructions, formatting, etc.)

---

**Tip:** Tackle each section in order, testing as you go. Start with core data structures, then game logic, then CLI, and finally add extras and polish. 