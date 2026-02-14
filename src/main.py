import os

tasks = []

if os.path.exists("tasks.txt"):
    with open("tasks.txt") as f:
        for line in f:
            line = line.strip()
            if "|" in line:
                done, text = line.split("|", 1)
                tasks.append((done == "1", text))
            else:
                tasks.append((False, line))

while True:
    print("\n--- TODO ---")

    if not tasks:
        print("No tasks.")
    else:
        for i, (done, text) in enumerate(tasks):
            mark = "x" if done else " "
            print(f"{i+1}. [{mark}] {text}")

    print("\n[a] Add")
    print("[d] Mark done")
    print("[x] Delete")
    print("[q] Quit")

    cmd = input("> ").strip().lower()

    if cmd == "a":
        text = input("Task: ").strip()
        if text:
            tasks.append((False, text))
        else:
            print("Empty task ignored.")

    elif cmd == "d":
        if not tasks:
            print("No tasks.")
            continue
        try:
            i = int(input("Done number: ")) - 1
            if 0 <= i < len(tasks):
                done, text = tasks[i]
                tasks[i] = (True, text)
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

    elif cmd == "x":
        if not tasks:
            print("No tasks to delete.")
            continue
        try:
            i = int(input("Delete number: ")) - 1
            if 0 <= i < len(tasks):
                confirm = input(f"Delete '{tasks[i][1]}'? (y/n): ")
                if confirm.lower() == "y":
                    removed = tasks.pop(i)
                    print(f"Deleted: {removed[1]}")
                else:
                    print("Cancelled.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

    elif cmd == "q":
        break
    
    tasks.sort(key=lambda t: t[0])
    with open("tasks.txt", "w") as f:
        for done, text in tasks:
            f.write(("1" if done else "0") + "|" + text + "\n")