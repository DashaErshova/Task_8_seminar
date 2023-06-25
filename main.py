from ui import interface

if __name__ == "__main__":
    while True:
        interface()
        command = input("Хотите выполнить другую операцию? (y/n): ")
        if command.lower() != "y":
            break
