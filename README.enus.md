# Copa Stickers - Data Structures Project

This repository contains a Python system for managing World Cup stickers for the Data Structures course at Fatec Rio Claro. The project focuses on implementing the required structures manually, without relying on built-in collections for the linked list and queue components requested by the assignment.

## Quick overview

The system supports:

- Registering collectors
- Adding stickers to an album
- Storing duplicate stickers
- Searching by sticker number, player, and team
- Registering exchange proposals
- Processing exchanges automatically
- Keeping an operation history
- Saving and loading data in JSON

## Requirements

- Python 3.10 or newer
- Pytest for running the test suite

## How to run

1. Clone the repository.
2. Open the project folder.
3. Start the interactive CLI:

python -m src.main

## How to run tests

pytest -q

## Project structure

- [src](src): main source code
- [tests](tests): automated tests
- [PLAN.md](PLAN.md): implementation plan
- [Projeto3.pdf](Projeto3.pdf): original assignment statement

## Technical approach

- Language: Python
- Required data structures implemented manually with linked nodes
- Separated layers for domain logic, business rules, persistence, and CLI interface

## Current status

- Core implementation completed
- Automated tests covering the main flows
- Test suite passing locally

## For guests and reviewers

If you are exploring the project for the first time, follow this order:

1. Read the assignment in [Projeto3.pdf](Projeto3.pdf).
2. Review the implementation plan in [PLAN.md](PLAN.md).
3. Run the system with python -m src.main.
4. Run the tests with pytest -q.

## Contributing

Contributions are welcome for code improvements, test coverage, and documentation.

## License

[MIT](LICENSE)
