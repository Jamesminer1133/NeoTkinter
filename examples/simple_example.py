import neotkinter

neotkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
neotkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = neotkinter.NTk()
app.geometry("400x780")
app.title("NeoTkinter simple_example.py")


def button_callback():
    print("Button click", combobox_1.get())


def slider_callback(value):
    progressbar_1.set(value)


frame_1 = neotkinter.NTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = neotkinter.NTkLabel(master=frame_1, justify=neotkinter.LEFT)
label_1.pack(pady=10, padx=10)

progressbar_1 = neotkinter.NTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

button_1 = neotkinter.NTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=10, padx=10)

slider_1 = neotkinter.NTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)

entry_1 = neotkinter.NTkEntry(master=frame_1, placeholder_text="NTkEntry")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = neotkinter.NTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("NTkOptionMenu")

combobox_1 = neotkinter.NTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("NTkComboBox")

checkbox_1 = neotkinter.NTkCheckBox(master=frame_1)
checkbox_1.pack(pady=10, padx=10)

radiobutton_var = neotkinter.IntVar(value=1)

radiobutton_1 = neotkinter.NTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = neotkinter.NTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=10, padx=10)

switch_1 = neotkinter.NTkSwitch(master=frame_1)
switch_1.pack(pady=10, padx=10)

text_1 = neotkinter.NTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "NTkTextbox\n\n\n\n")

segmented_button_1 = neotkinter.NTkSegmentedButton(master=frame_1, values=["NTkSegmentedButton", "Value 2"])
segmented_button_1.pack(pady=10, padx=10)

tabview_1 = neotkinter.NTkTabview(master=frame_1, width=300)
tabview_1.pack(pady=10, padx=10)
tabview_1.add("NTkTabview")
tabview_1.add("Tab 2")

app.mainloop()
