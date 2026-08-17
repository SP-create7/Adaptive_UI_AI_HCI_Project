# Adaptive UI Using AI/HCI Project

## Project Overview

This project demonstrates an AI-based adaptive human-computer interaction system. The application allows users to select different interface preferences and records their interactions.

A machine-learning Decision Tree classifier analyzes the user's interaction history and predicts the user's preferred interface style. The prediction is then used to adapt the interface.

## Adaptive Behavior

The system supports three interface preferences:

- Simple Interface
- Detailed Interface
- Dark Interface

The application records how many times each preference is selected. The interaction history is passed to a machine-learning model, which predicts the user's preferred interface style.

When the model predicts a dark-interface preference, the user interface adapts to a dark presentation.

## Technologies Used

- Python 3.11
- Flask
- HTML
- CSS
- JavaScript
- Scikit-learn
- Decision Tree Classifier
- Visual Studio Code
- GitHub

## Project Structure

```text
Adaptive_UI_AI_HCI_Project
│
├── app
│   ├── static
│   ├── templates
│   │   └── index.html
│   ├── adaptive_model.py
│   └── app.py
│
├── documentation
├── report
├── screenshots
└── README.md