import neotkinter as ntk

app = ntk.NTk()
app.title("NeoTkinter Testing Application")
app.geometry("400x300")

def click():
    print("Button 1 clicked.")
    print(app.askOpenFile(mode = "r", filetypes=[("Python Files", "*.py")]).name)

button1 = ntk.NTkButton(master = app, text = "Click Me!", command = click)
button1.pack(pady = 20, padx = 20)

app.mainloop()