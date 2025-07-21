# Yahtzee CLI Game - Implementation To-Do List

## 1. Project Setup
- [x] Set up project structure and main entry point
- [x] Create initial files: `yahtzee.py`, `scorecard.py`, `dice.py`, `cli.py`, `utils.py`
- [x] Set up a `tests/` directory for test files
- [x] Add `pytest` to project requirements (if using a requirements file)

## 2. Data Structures
- [ ] Implement `Player` class
- [ ] Implement `Scorecard` class
- [ ] Define Yahtzee categories (as constants or Enum)
- [ ] Implement `Dice` class
- [ ] Implement `Game` class (single player, but extensible)

## 3. Game Logic
- [ ] Implement dice rolling and re-rolling logic
- [ ] Implement scoring logic for all categories
- [ ] Implement scorecard updating and validation (category used only once)
- [ ] Implement main game loop (13 rounds, per player)

## 4. Command-Line Interface (CLI)
- [ ] Implement CLI prompts for player name(s)
- [ ] Implement CLI display for dice, scorecard, and categories
- [ ] Implement CLI input for dice selection and category choice
- [ ] Implement input validation and error handling
- [ ] Implement end-of-game summary and results display

## 5. Testing
- [ ] Write unit tests for `Player` class
- [ ] Write unit tests for `Scorecard` class
- [ ] Write unit tests for `Dice` class
- [ ] Write unit tests for scoring logic
- [ ] Write tests for CLI input validation (where possible)
- [ ] Write integration tests for main game loop (optional)

## 6. Extensibility & Extras
- [ ] Refactor for multiplayer support
- [ ] Add high score tracking (optional)
- [ ] Add save/load game feature (optional)
- [ ] Polish CLI user experience (instructions, formatting, etc.)

---

**Tip:** Tackle each section in order, testing as you go. Start with core data structures, then game logic, then CLI, and finally add extras and polish. 