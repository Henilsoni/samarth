import time
import pyautogui

def Find_object(a):
    print("Waiting....")
    time.sleep(0.2)

    try:
        position = pyautogui.locateOnScreen(a, confidence=0.8)  # Use confidence if applicable
        if position is None:
            raise ValueError("Image not found")
        else:

        # Extract coordinates
            x = position.left
            y = position.top
            x = int(x + 20)
            y = int(y + 20)
            print(f"Coordinates: {x}, {y}")
            time.sleep(0.2)
            return True

    except Exception as e:
        print(f"Error: {e}")
        return False
while True:
    a = "C:/Users/BAPS/OneDrive/Documents/Codes/AI/sp/TR/App25.png"
    aa = Find_object(a)
    b = "C:/Users/BAPS/OneDrive/Documents/Codes/AI/sp/TR/App26.png"
    bb = Find_object(b)
    if aa == True:
        pyautogui.click(53,627)
        continue
    elif bb == True:
        pyautogui.click(48,273)
        continue
    else:
        continue

    