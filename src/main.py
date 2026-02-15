import os

tasks = []

if os.path.exists("tasks.txt"):
    with open("tasks.txt") as f:
        for line in f:
            line = line.strip()
            parts = line.split("|")
            if len(parts) == 3:
                done, prio, text = parts
                tasks.append((done == "1", int(prio), text))
            elif len(parts) == 2:
                done, text = parts
                tasks.append((done == "1", 2, text))
            else:
                tasks.append((False, 2, line))

while True:
    print("\n--- TODO ---")

    if not tasks:
        print("No tasks.")
    else:
        for i, (done, prio, text) in enumerate(tasks):
            mark = "x" if done else " "
            pmark = "!" * prio
            print(f"{i+1}. [{mark}] [{pmark}] {text}")

    print("\n[a] Add")
    print("[d] Mark done")
    print("[x] Delete")
    print("[q] Quit")

    cmd = input("> ").strip().lower()

    if cmd == "a":
        text = input("Task: ").strip()
        if text:
            try:
                prio = int(input("Priority (1=low, 2=med, 3=high): "))
                if prio not in (1, 2, 3):
                    prio = 2
            except ValueError:
                prio = 2
            tasks.append((False, prio, text))
        else:
            print("Empty task ignored.")

    elif cmd == "d":
        if not tasks:
            print("No tasks.")
            continue
        try:
            i = int(input("Done number: ")) - 1
            if 0 <= i < len(tasks):
                done, prio, text = tasks[i]
                tasks[i] = (not done, prio, text)
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
                confirm = input(f"Delete '{tasks[i][2]}'? (y/n): ")
                if confirm.lower() == "y":
                    removed = tasks.pop(i)
                    print(f"Deleted: {removed[2]}")
                else:
                    print("Cancelled.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

    elif cmd == "q":
        break

    tasks.sort(key=lambda t: (t[0], -t[1]))

    with open("tasks.txt", "w") as f:
        for done, prio, text in tasks:
            f.write(f"{'1' if done else '0'}|{prio}|{text}\n")
