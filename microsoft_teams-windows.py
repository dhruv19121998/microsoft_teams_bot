import pyautogui
import time

# Ask user for input
text = input("Enter text: ")

# Open Teams application
pyautogui.hotkey('win', 's')
time.sleep(1)
pyautogui.write('Teams')
time.sleep(1)
pyautogui.press('enter')
time.sleep(10) # wait for Teams to open

# Locate the chat button and click on it
chat_button = pyautogui.locateOnScreen('teams_chat_button.png', confidence=0.9)
if chat_button is not None:
    chat_button_center = pyautogui.center(chat_button)
    pyautogui.click(chat_button_center)

# Locate the input field and click on it
input_field = pyautogui.locateOnScreen('teams_input_field.png', confidence=0.9)
input_field_center = pyautogui.center(input_field)
pyautogui.click(input_field_center)

# Input the user's text
pyautogui.write(text)
time.sleep(3)
pyautogui.press('down')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)

# Locate the chat inbox and click on it
chat_inbox = pyautogui.locateOnScreen('teams_chat_inbox.png', confidence=0.9)
if chat_inbox is not None:
    chat_inbox_center = pyautogui.center(chat_inbox)
    pyautogui.click(chat_inbox_center)
else:
    chat_inbox2 = pyautogui.locateOnScreen('teams_chat_inbox2.png', confidence=0.9)
    chat_inbox_center2 = pyautogui.center(chat_inbox2)
    pyautogui.click(chat_inbox_center2)

# Input a message in the chat inbox
pyautogui.write("hello how are you?")
pyautogui.press('enter')

