# Task Management System

## Overview
This is a backend-only task management system built using Python and the Model-View-Controller (MVC) architecture. It allows users to create, manage, and track tasks through a command-line interface. Key features include task creation, deletion, sorting, status updates (e.g., DOING to DONE), and tracking task completion percentages. The system uses SQLite for lightweight and simple data storage, requiring no complex configuration.

## Features
- **User Authentication**: Sign up or log in to access the task management system.
- **Task Management**:
  - Create new tasks with details.
  - Edit or delete existing tasks.
  - Sort tasks by title or status (e.g., DOING, DONE).
  - Update task status (e.g., from DOING to DONE).
  - Track task completion percentage via a progress indicator.
- **Lightweight Database**: Uses SQLite for simple and efficient data storage.
- **Command-Line Interface**: Interact with the system via a terminal-based interface.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: Standard Python libraries (no external dependencies)
- **Database**: SQLite
- **Architecture**: Model-View-Controller (MVC)
- **Environment**: Virtual environment (`.venv`)

## Prerequisites
- Python 3.8 or higher installed on your system.
- No additional libraries are required, as the project uses Python's built-in libraries.

## Installation
Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Awmirhm/TaskManagement.git

Navigate to the Project Directory:
bashcd TaskManagement

Activate the Virtual Environment:

On Windows:
bash.venv\Scripts\activate

On macOS/Linux:
bashsource .venv/bin/activate


Note: The virtual environment (.venv) already includes all required libraries.
Run the Application:
bashpython main.py
This will start the task management system in your terminal.

Usage

Sign Up/Login:

On startup, the application asks if you have an account.
Choose "No" to create a new account or "Yes" to log in with existing credentials.


Managing Tasks:

Navigate to the task management section via the command-line prompts.
Add a new task by entering task details.
Sort tasks by title or status.
Update task status (e.g., mark as DONE) or edit task details.
Track progress by updating the completion percentage.



Example Interaction:
plaintextDo you have an account? (Yes/No): No
Enter username: user1
Enter password: mypassword123
Account created successfully!
---
Task Management Menu:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Sort Tasks
6. Exit
(Optional: Add a screenshot or ASCII diagram of the CLI interface here for better visualization.)
# Project Structure
# textTaskManagement/
├── controllers/
## Handles business logic (MVC Controller)
├── models/
## Defines data structures and database interactions (MVC Model)
├── views/
## Manages command-line interface output (MVC View)
├── .venv/
## Virtual environment with required libraries
├── main.py
## Entry point of the application
├── database.db
## SQLite database file (auto-generated if not present)
└── README.md
## Project documentation
# Contributing
We welcome contributions to improve this project! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.

Please read our Contributing Guide for more details (if available).
License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contact

Author: Amir (Awmirhm)

GitHub: Awmirhm
