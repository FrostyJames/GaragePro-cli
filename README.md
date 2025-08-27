# GaragePro CLI

GaragePro is a Python-based command-line application for managing vehicle service records in an auto garage. It features a fully interactive menu-driven interface, allowing users to register customers, manage vehicles, log service records, and search by vehicle attributes—all backed by a SQLite database and SQLAlchemy ORM.

---

## Features

- Register customers with contact details
- Add vehicles linked to customers
- Log service records with type, cost, notes, and date
- View all customer, vehicle, and service data in a dashboard-style summary
- Search vehicles by make, model, or year
- Interactive menu-driven CLI (no need to memorize commands)
- SQLite database with SQLAlchemy ORM
- Alembic-ready for future migrations

---

## Tech Stack

- **Python 3.8+**
- **SQLAlchemy** – ORM for database modeling
- **SQLite** – Lightweight local database
- **Alembic** – Optional migration tool
- *(Click is no longer required in the current version)*

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd garagepro-cli

2. **- Initialize Pipenv with Python 3.8**
   ```bash
   pipenv --python 3.8

3. **- Install dependencies**
   ```bash
   pipenv install sqlalchemy alembic

4. **Install Click if needed later**
   ```bash
   pipenv install click

5. **Set up Alembic for migrations**
   ```bash
   pipenv run alembic init migrations

6. **- Edit Alembic config In alembic.ini**
   ```bash
   sqlalchemy.url = sqlite:///garagepro.db

7. **- Activate the environment**
   ```bash
   pipenv shell

8. **- Run the CLI**
   ```bash
   python main.py

## Project structure

garagepro-cli/
├── crud.py           # All database operations
├── main.py           # Interactive CLI entry point
├── models.py         # SQLAlchemy models
├── garagepro.db      # SQLite database file
├── migrations/       # Alembic migration folder (optional)
├── alembic.ini       # Alembic config file
└── README.md

## How to use

 ***- Run the CLI***
     python main.py

***Navigate through the commands***
GaragePro CLI Main Menu
1. View All Records
2. Customer Management
3. Vehicle Management
4. Service Records
5. Exit

## Author
By: James Ivan