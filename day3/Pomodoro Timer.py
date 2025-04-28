import time

def pomodoro_timer(minutes):
    print(f"Starting {minutes}-minute Pomodoro session.")
    time.sleep(minutes * 60)
    print("Time's up! Take a break.")

pomodoro_timer(25)  # Starts a 25-minute focus session.
