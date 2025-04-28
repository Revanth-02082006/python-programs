import pyautogui
import time

while True:
    screenshot = pyautogui.screenshot()
    screenshot.save(f"screenshot_{time.time()}.png")
    time.sleep(10)  # Takes a screenshot every 10 seconds
