import neotkinter as ntk

window = ntk.NTk()
window.title("NeoTkinter Testing Application")
window.geometry("1000x500")
ntk.set_appearance_mode("dark")
ntk.set_default_color_theme("purple")

menuBar = ntk.NTkMenuBar(window)
menuButton = menuBar.add_cascade("Menu Entry")
blankMenuButton = menuBar.add_cascade("Blank Menu Entry")

dropdown = ntk.NTkDropdownMenu(menuButton)
dropdown.add_option(option="value") 
dropdown.add_separator() 
submenu = dropdown.add_submenu("submenu") 
submenu.add_option(option="value")

titlebar = ntk.NTkTitleMenu(window)
titlebarButton = titlebar.add_cascade("Titlebar Entry")
blankTitlebarButton = titlebar.add_cascade("Blank Titlebar Entry")

titleDropdown = ntk.NTkDropdownMenu(titlebarButton)
titleDropdown.add_option(option="value") 
titleDropdown.add_separator() 
titleSubmenu = titleDropdown.add_submenu("submenu") 
titleSubmenu.add_option(option="value")

app = ntk.NTkScrollableFrame(master = window, width = 1000)
app.pack(pady = 20, padx = 20, expand = True, fill = "both")

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

def selectFile():
    print("File select button clicked.")
    try:
        msg = "The file:", ntk.filedialog.askopenfile(mode = "r", filetypes=[("Python Files", "*.py")]).name, "was selected."
        ntk.NTkMessagebox(message= msg, icon="check", option_1="Ok")
    except Exception:
        ntk.NTkMessagebox(message= "No file was selected.", icon="warning", option_1="Ok")

button1 = ntk.NTkButton(master = app, text = "Select File", command = selectFile)
button1.pack(pady = 20, padx = 20)

tooltip = ntk.NTkToolTip(button1, message = "This is an NTkToolTip!")

notificationManager = ntk.NTkNotificationManager(window)
notificationManager.showNotification(message = "This is a NTkNotificationManager.showNotification!", notify_type = ntk.NTkNotifyType.INFO)

textEditor = ntk.NTkCodeBox(master = app, language = "txt")
textEditor.pack(pady = 20, padx = 20, expand = True, fill = "both")

window.mainloop()


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
from neotkinter.windows.widgets.image import NTkImage
from tkinter import StringVar
"""
