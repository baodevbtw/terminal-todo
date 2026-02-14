tasks = []

while True:
    print("\n--- TODO ---")

    if not tasks:
        print("No tasks.")
    else:
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")

    print("\n[a] Add")
    print("[x] Delete")
    print("[q] Quit")

    cmd = input("> ")

    if cmd == "a":
        text = input("Task: ").strip()
        if text:
            tasks.append(text)
        else:
            print("Empty task ignored.")

    elif cmd == "q":
        break

    elif cmd == "x":
        if not tasks:
            print("No tasks to delete.")
            continue
        try:
            i = int(input("Delete number: ")) - 1
            if 0 <= i < len(tasks):
                removed = tasks.pop(i)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")
