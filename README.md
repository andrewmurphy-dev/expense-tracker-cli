# 📦 CLI Expenses Manager

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)
![Status](https://img.shields.io/badge/Status-Learning%20Project-success)

A simple Python CLI (Command Line Interface) application for managing personal expenses. Users can add, view, calculate totals, and delete expense entries directly from the terminal.

## 📖 Project Description

CLI Expenses Manager is a lightweight Python project designed to help users track expenses through a simple terminal-based interface. It was built as a foundational backend practice project, focusing on core programming skills such as input validation, control flow, modular file structure, and dictionary-based data handling.

This project is useful for practicing how real programs are organized while still building something functional and interactive.

## 🚀 Features

- Add expenses with input validation
- View all saved expenses
- Calculate the total of all expenses
- Delete a single expense
- Delete all expenses with confirmation
- Run the application continuously through a CLI menu loop

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cli-expenses-manager.git
cd cli-expenses-manager

## 💻 Usage

### Example Menu

```text
welcome to main menu

press 1: register a new user
press 2: login
press 'exit' to quit
```

### Example Registration

```text
Enter a username: andy
Enter a password: password123
Signed up successfully!
```

### Example Login

```text
login name: andy
login password: password123
success, you have logged in successfully!
```

## 🧠 How It Works

### Storage Structure

```python
storage = {
    "andy": "password123"
}
```

- **Key** → username
- **Value** → password

### Login Validation Logic

```python
if username in storage and storage[username] == password:
    print("login successful")
```

## 🗂️ Project Structure

```text
python-cli-auth-system/
│
├── main.py        # Entry point and CLI menu
├── auth.py        # Authentication logic
├── storage.py     # In-memory user storage
└── README.md
```

## 📁 File Breakdown

### main.py

- Handles user input
- Controls program flow (menu loop)

### auth.py

- Contains validation logic
- Handles user registration and login

### storage.py

- Stores user data in a dictionary

## 💾 Data on disk (Week 10 practice)

- Expenses are stored in `expenses_data.txt` (plain text, one line: `name|amount`) using `with open(...)` in `storage.py`.
- The file is listed in `.gitignore` so your local totals are not pushed by default.

## ⚠️ Known Limitations

- No cloud sync (data is only the local `expenses_data.txt` on your machine)
- No database integration (file-based storage only)

## 🔧 Future Improvements

- Save users to JSON file
- Add password hashing (bcrypt)
- Add session handling
- Improve CLI UX
- Add unit tests
- Convert to FastAPI backend

## 🤝 Contributing

### Steps to contribute

```bash
git checkout -b feature/your-feature-name
git commit -m "Add meaningful feature"
git push origin feature/your-feature-name
```

Then open a Pull Request.

## 🎯 Purpose

This project demonstrates:

- Control flow design
- Input validation
- Dictionary-based data handling
- Modular Python structure
