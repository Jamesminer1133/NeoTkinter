import neotkinter as ntk

app = ntk.NTk()
app.title("NeoTkinter Testing Application")
app.geometry("1000x500")

menuBar = ntk.NTkMenuBar(app)
menuButton = menuBar.add_cascade("Menu Entry")
blankMenuButton = menuBar.add_cascade("Blank Menu Entry")

dropdown = ntk.NTkDropdownMenu(menuButton)
dropdown.add_option(option="value") 
dropdown.add_separator() 
submenu = dropdown.add_submenu("submenu") 
submenu.add_option(option="value")

titlebar = ntk.NTkTitleMenu(app)
titlebarButton = titlebar.add_cascade("Titlebar Entry")
blankTitlebarButton = titlebar.add_cascade("Blank Titlebar Entry")

titleDropdown = ntk.NTkDropdownMenu(titlebarButton)
titleDropdown.add_option(option="value") 
titleDropdown.add_separator() 
titleSubmenu = titleDropdown.add_submenu("submenu") 
titleSubmenu.add_option(option="value")

randomWords = ["Dark","Celebration","Example","Relenquish","Scandal",
               "Wriggle","Paint","Ostracize","Figure","Agriculture",
               "Of","Mix","Consider","Tissue","Follow",
               "Goalkeeper","Extraterrestrial","Truck","Recycle","Afford",
               "Clay","Confidence","Statement","Nerve","Functional"]
randomWords.sort()

scrollingOptionMenu = ntk.NTkOptionMenu(app, values = randomWords, anchor = "center")
scrollingOptionMenu.set("Select Value From NTkOptionMenu")
scrollingOptionMenu.pack(pady = 20, padx = 20)
ntk.NTkScrollableDropdown(attach = scrollingOptionMenu, values = randomWords)

def click():
    print("Button 1 clicked.")
    try:
        print("The file:", ntk.filedialog.askopenfile(mode = "r", filetypes=[("Python Files", "*.py")]).name, "was selected.")
    except Exception:
        print("No file was selected.")

button1 = ntk.NTkButton(master = app, text = "Click Me!", command = click)
button1.pack(pady = 20, padx = 20)

app.mainloop()


"""
MAIN IMPORT LIST FOR WIDGETS / WINDOWS THAT USE MAIN CLASSES:

from neotkinter.windows.ntk_toplevel import NTkToplevel
from neotkinter.windows.widgets.ntk_frame import NTkFrame
from neotkinter.windows.widgets.ntk_scrollable_frame import NTkScrollableFrame
from neotkinter.windows.widgets.ntk_entry import NTkEntry
from neotkinter.windows.widgets.ntk_label import NTkLabel
from neotkinter.windows.widgets.ntk_button import NTkButton
from neotkinter.windows.widgets.ntk_combobox import NTkComboBox
from neotkinter.windows.widgets.ntk_optionmenu import NTkOptionMenu
from neotkinter.windows.widgets.theme import ThemeManager
from tkinter import StringVar
"""