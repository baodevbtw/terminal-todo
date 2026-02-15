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


def show_help():
    print("""
Commands:
a <text>        Add task
<number>       Toggle done
x <number>     Delete task
h              Show help
q              Quit
""")


while True:
    print("\n--- TODO ---")

    if not tasks:
        print("No tasks.")
    else:
        for i, (done, prio, text) in enumerate(tasks):
            mark = "x" if done else " "
            pmark = "!" * prio
            print(f"{i+1}. [{mark}] [{pmark}] {text}")

    cmd = input("> ").strip().lower()
    parts = cmd.split(maxsplit=1)

    # HELP
    if cmd in ("h", "help"):
        show_help()

    # QUIT
    elif cmd in ("q", "quit", "exit"):
        break

    # TOGGLE BY NUMBER
    elif cmd.isdigit():
        i = int(cmd) - 1
        if 0 <= i < len(tasks):
            done, prio, text = tasks[i]
            tasks[i] = (not done, prio, text)
        else:
            print("Invalid number.")

    # ADD
    elif parts[0] in ("a", "add"):
        if len(parts) == 2:
            text = parts[1]
        else:
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

    # DELETE
    elif parts[0] in ("x", "del", "delete"):
        try:
            if len(parts) == 2:
                i = int(parts[1]) - 1
            else:
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

    else:
        print("Unknown command. Press 'h' for help.")

    # sort: not done first, high priority first
    tasks.sort(key=lambda t: (t[0], -t[1]))

    with open("tasks.txt", "w") as f:
        for done, prio, text in tasks:
            f.write(f"{'1' if done else '0'}|{prio}|{text}\n")