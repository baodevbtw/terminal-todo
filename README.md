# Terminal TODO

A simple beginner terminal-based TODO application written in Python.

This project is built step-by-step to practice Git, GitHub, and basic software development.

## Features (v0.4.0)

- Add new tasks  
- Mark tasks as done / undo  
- Delete tasks by number  
- Confirm before deleting  
- Task priority (low / medium / high)  
- Completed tasks sorted to the bottom  
- Tasks sorted by priority  
- Tasks are saved to disk (tasks.txt)  
- Tasks are loaded automatically on startup  

## File format

From version 0.4.0, tasks are stored like this:

0|3|Finish project  
1|1|Buy milk  
0|2|Learn git  

Where:
- First number: 0 = not done, 1 = done  
- Second number: 1 = low, 2 = medium, 3 = high  

## How to run

git clone https://github.com/baodevbtw/terminal-todo  
cd terminal-todo  
python src/main.py  

## Why this project exists

This project is intentionally simple and avoids frameworks.

The goal is to:
- Learn Git workflow (commits, tags, releases)  
- Practice semantic versioning  
- Understand file I/O  
- Learn how data formats evolve  
- Build features incrementally without overengineering  
