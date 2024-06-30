import pyautogui
import time

#time before start
delay_before_start = 10

#time betwen clicks
interval_between_clicks = 0

#number of clicks
number_of_clicks = 150

def auto_clicker():
    print(f"Autoclicker starts in {delay_before_start} seconds...")
    time.sleep(delay_before_start)
    
    for i in range(number_of_clicks):
        pyautogui.click()
        print(f"Klick {i + 1}")
        time.sleep(interval_between_clicks)

    print("Autoclicker stopped.")

if __name__ == "__main__":
    auto_clicker()
