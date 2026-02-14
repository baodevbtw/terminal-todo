# Terminal TODO

A simple beginner terminal-based TODO application written in Python.

This project is built step-by-step to practice Git, GitHub, and basic software development.

## Features (v0.3.1)

- Add new tasks  
- Mark tasks as done  
- Delete tasks by number  
- Confirm before deleting  
- Tasks are saved to disk (tasks.txt)  
- Tasks are loaded automatically on startup  
- Uses a strict internal file format (done|text)

## File format

From version 0.3.0, tasks are stored like this:

0|Buy milk  
1|Finish homework  
0|Learn git  

Where:
- 0 = not done  
- 1 = done  

Older tasks.txt files (pre-0.3.0) are automatically migrated on startup.

## How to run

git clone https://github.com/baodevbtw/terminal-todo  
cd terminal-todo  
python src/main.py  

## Roadmap

- 0.3.1 – Migrate old file format automatically  
- 0.4.0 – Task priority (low / medium / high)  
- 0.5.0 – Due dates  
- 1.0.0 – Stable CLI tool

## Why this project exists

This project is intentionally simple and avoids frameworks.

The goal is to:
- Learn Git workflow (commits, tags, releases)  
- Practice semantic versioning  
- Understand file I/O  
- Build features incrementally without overengineering  
