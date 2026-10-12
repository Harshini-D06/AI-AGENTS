# Study Assistant Agent

## Overview

Study Assistant Agent is an AI-powered educational assistant built using
Python and Google's Gemini API.

It helps students understand concepts, answer frequently asked questions,
generate quizzes, and create personalized study plans.

## Features

- AI Study Assistant
- Intelligent FAQ Assistant
- AI Quiz Generator
- AI Study Plan Generator
- Zero-shot Prompting
- Few-shot Prompting
- Role Prompting

## Technologies Used

- Python
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv
- Git and GitHub

## Prompt Engineering

### 1. Zero-Shot Prompting

The AI is given a task without providing any examples.

Example:

"Explain linked lists in Python using simple language."

### 2. Few-Shot Prompting

The AI is given examples before receiving the actual task.

Example:

Question: What is Python?
Answer: Python is a programming language.

Question: What is SQL?
Answer: SQL is a database query language.

Question: What is Java?
Answer:

### 3. Role Prompting

The AI is assigned a specific role before answering.

Example:

"You are an experienced Python teacher.
Explain recursion with a simple Python example."

## Project Structure

```text
study-assistant-agent/
│
├── study_assistant.py
├── prompt_engineering.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore