# **NeoTkinter**

NeoTkinter is a python UI-library based on CustomTkinter, which combines the elements of which of customtkinter and it's extensions.

## Example Program
To test NeoTkinter you can try this simple example with only a single button:
```python
import NeoTkinter

NeoTkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
NeoTkinter.set_default_color_theme("blue")  # Themes: purple (default), blue, dark-blue, green

app = NeoTkinter.NTk()  # create NTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use NTkButton instead of tkinter Button
button = NeoTkinter.NTkButton(master=app, text="NTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=NeoTkinter.CENTER)

app.mainloop()
```
which results in the following window on macOS:

<img src="documentation_images/single_button_macOS.png" width="400"/>