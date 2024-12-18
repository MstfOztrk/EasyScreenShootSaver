import pyautogui
import keyboard
import os
from datetime import datetime
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import threading

# Function to capture a screenshot and save to desktop
def capture_screenshot():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    screenshot_path = os.path.join(desktop_path, f"screenshot_{timestamp}.png")
    pyautogui.screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

def listen_for_print_screen():
    keyboard.add_hotkey('print_screen', capture_screenshot)

def create_camera_icon(size=64):
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle([size * 0.1, size * 0.3, size * 0.9, size * 0.8], fill="orange", outline="black")
    draw.ellipse([size * 0.35, size * 0.4, size * 0.65, size * 0.7], fill="black", outline="white")
    draw.rectangle([size * 0.15, size * 0.2, size * 0.3, size * 0.35], fill="yellow", outline="black")

    return image

def quit_application(icon, item):
    icon.stop()

# Main function
def main():
    icon_image = create_camera_icon(64)
    menu = Menu(MenuItem('Quit', quit_application))
    icon = Icon("Screenshot Tool", icon_image, "Screenshot Tool", menu)
    
    listener_thread = threading.Thread(target=listen_for_print_screen, daemon=True)
    listener_thread.start()
    
    # Run the system tray icon
    icon.run()

if __name__ == "__main__":
    main()
