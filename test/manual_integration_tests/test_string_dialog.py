import neotkinter

neotkinter.set_appearance_mode("dark")
neotkinter.set_default_color_theme("blue")
neotkinter.set_window_scaling(0.8)
neotkinter.set_widget_scaling(0.8)

app = neotkinter.NTk()
app.geometry("400x300")
app.title("NTkDialog Test")


def change_mode():
    if c1.get() == 0:
        neotkinter.set_appearance_mode("light")
    else:
        neotkinter.set_appearance_mode("dark")


def button_1_click_event():
    dialog = neotkinter.NTkInputDialog(text="Type in a number:", title="Test")
    print("Number:", dialog.get_input())


def button_2_click_event():
    dialog = neotkinter.NTkInputDialog(text="long text "*100, title="Test")
    print("Number:", dialog.get_input())


button_1 = neotkinter.NTkButton(app, text="Open Dialog", command=button_1_click_event)
button_1.pack(pady=20)
button_2 = neotkinter.NTkButton(app, text="Open Dialog", command=button_2_click_event)
button_2.pack(pady=20)
c1 = neotkinter.NTkCheckBox(app, text="dark mode", command=change_mode)
c1.pack(pady=20)

app.mainloop()
