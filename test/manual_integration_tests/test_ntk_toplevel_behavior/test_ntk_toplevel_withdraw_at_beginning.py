import neotkinter

app = neotkinter.NTk()
app.geometry("400x400+300+300")

toplevel = neotkinter.NTkToplevel(app)
toplevel.geometry("350x240+800+300")

toplevel.withdraw()
toplevel.after(2000, toplevel.deiconify)

app.mainloop()
