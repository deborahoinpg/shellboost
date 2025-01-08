import ctypes
from ctypes import wintypes
import os

class ShellBoost:
    def __init__(self):
        self.user32 = ctypes.WinDLL('user32', use_last_error=True)

    def change_wallpaper(self, image_path):
        """Change Desktop Wallpaper"""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"The image file {image_path} was not found.")
        
        # SystemParametersInfoW is used to change system parameters
        result = self.user32.SystemParametersInfoW(20, 0, image_path, 3)
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())

    def toggle_taskbar_visibility(self, hide=True):
        """Hide or show the Taskbar"""
        hwnd = self.user32.FindWindowW("Shell_TrayWnd", None)
        if not hwnd:
            raise ctypes.WinError(ctypes.get_last_error())
        
        if hide:
            self.user32.ShowWindow(hwnd, 0)  # 0 to hide
        else:
            self.user32.ShowWindow(hwnd, 5)  # 5 to show

    def change_start_menu_color(self, color_hex):
        """Change Start Menu Color - Placeholder for actual implementation"""
        # This is a complex task as it involves dealing with Windows Registry directly
        print(f"Changing Start Menu color to {color_hex} is not implemented yet.")

if __name__ == "__main__":
    shellboost = ShellBoost()
    try:
        shellboost.change_wallpaper("C:\\path\\to\\your\\wallpaper.jpg")
        shellboost.toggle_taskbar_visibility(hide=False)
    except Exception as e:
        print(f"Error: {e}")