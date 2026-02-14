tasks = []

while True:
    print("\n--- TODO ---")

    if not tasks:
        print("No tasks.")
    else:
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")

    print("\n[a] Add")
    print("[q] Quit")

    cmd = input("> ")

    if cmd == "a":
        text = input("Task: ")
        tasks.append(text)

    elif cmd == "q":
        break