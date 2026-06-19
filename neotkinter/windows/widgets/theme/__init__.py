from .theme_manager import ThemeManager

# load default purple theme
try:
    ThemeManager.load_theme("purple")
except FileNotFoundError as err:
    raise FileNotFoundError(f"{err}\nThe .json theme file for NeoTkinter could not be found.\n" +
                            f"If packaging with pyinstaller was used, have a look at the customtkinter wiki:\n" +
                            f"https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging#windows-pyinstaller-auto-py-to-exe")
