from datetime import datetime

def log_action(action, target, status):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("logs.txt", "a") as file:
            file.write(f"{current_time} | {action} | {target} | {status}\n")

    except OSError as e:
        print(f"Logging failed: {e}")