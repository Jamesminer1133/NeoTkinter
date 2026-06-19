import tkinter
import neotkinter

neotkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
neotkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = neotkinter.NTk()
app.geometry("1100x900")
app.title("NeoTkinter simple_example.py")


def create_all_widgets(master, state="normal"):
    label_1 = neotkinter.NTkLabel(master=master, justify=tkinter.LEFT)
    label_1.pack(pady=10, padx=10)

    progressbar_1 = neotkinter.NTkProgressBar(master=master)
    progressbar_1.pack(pady=10, padx=10)

    button_1 = neotkinter.NTkButton(master=master, state=state, border_width=0)
    button_1.pack(pady=10, padx=10)

    slider_1 = neotkinter.NTkSlider(master=master, from_=0, to=1, state=state)
    slider_1.pack(pady=10, padx=10)
    slider_1.set(0.5)

    entry_1 = neotkinter.NTkEntry(master=master, placeholder_text="NTkEntry", state=state)
    entry_1.pack(pady=10, padx=10)

    optionmenu_1 = neotkinter.NTkOptionMenu(master, values=["Option 1", "Option 2", "Option 42 long long long..."], state=state)
    optionmenu_1.pack(pady=10, padx=10)
    optionmenu_1.set("NTkOptionMenu")

    combobox_1 = neotkinter.NTkComboBox(master, values=["Option 1", "Option 2", "Option 42 long long long..."], state=state)
    combobox_1.pack(pady=10, padx=10)
    optionmenu_1.set("NTkComboBox")

    checkbox_1 = neotkinter.NTkCheckBox(master=master, state=state)
    checkbox_1.pack(pady=10, padx=10)

    radiobutton_var = tkinter.IntVar(value=1)

    radiobutton_1 = neotkinter.NTkRadioButton(master=master, variable=radiobutton_var, value=1, state=state)
    radiobutton_1.pack(pady=10, padx=10)

    radiobutton_2 = neotkinter.NTkRadioButton(master=master, variable=radiobutton_var, value=2, state=state)
    radiobutton_2.pack(pady=10, padx=10)

    switch_1 = neotkinter.NTkSwitch(master=master, state=state)
    switch_1.pack(pady=10, padx=10)

    text_1 = neotkinter.NTkTextbox(master=master, width=200, height=70, state=state)
    text_1.pack(pady=10, padx=10)
    text_1.insert("0.0", "NTkTextbox\n\n\n\n")

    segmented_button_1 = neotkinter.NTkSegmentedButton(master=master, values=["NTkSegmentedButton", "Value 2"], state=state)
    segmented_button_1.pack(pady=10, padx=10)

    tabview_1 = neotkinter.NTkTabview(master=master, width=200, height=100, state=state, border_width=2)
    tabview_1.pack(pady=10, padx=10)
    tabview_1.add("NTkTabview")
    tabview_1.add("Tab 2")


frame_0 = neotkinter.NTkFrame(master=app, fg_color="transparent")
frame_0.grid(row=0, column=0, padx=10, pady=10)
create_all_widgets(frame_0, state="disabled")

frame_1 = neotkinter.NTkFrame(master=app, fg_color="transparent")
frame_1.grid(row=0, column=1, padx=10, pady=10)
create_all_widgets(frame_1)

frame_2 = neotkinter.NTkFrame(master=app)
frame_2.grid(row=0, column=2, padx=10, pady=10)
create_all_widgets(frame_2)

frame_3 = neotkinter.NTkFrame(master=app)
frame_3.grid(row=0, column=3, padx=10, pady=10)
frame_4 = neotkinter.NTkFrame(master=frame_3)
frame_4.grid(row=0, column=0, padx=25, pady=25)
create_all_widgets(frame_4)

appearance_mode_button = neotkinter.NTkSegmentedButton(app, values=["light", "dark"], command=lambda v: neotkinter.set_appearance_mode(v))
appearance_mode_button.grid(row=1, column=0, columnspan=3, padx=25, pady=25)

app.mainloop()
