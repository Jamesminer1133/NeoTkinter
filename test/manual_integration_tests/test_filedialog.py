import tkinter.messagebox
import neotkinter

neotkinter.set_appearance_mode("dark")


class App(neotkinter.NTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("test filedialog")

        self.button_1 = neotkinter.NTkButton(master=self, text="askopenfile", command=lambda: print(neotkinter.filedialog.askopenfile()))
        self.button_1.pack(pady=10)
        self.button_2 = neotkinter.NTkButton(master=self, text="askopenfiles", command=lambda: print(neotkinter.filedialog.askopenfiles()))
        self.button_2.pack(pady=10)
        self.button_3 = neotkinter.NTkButton(master=self, text="askdirectory", command=lambda: print(neotkinter.filedialog.askdirectory()))
        self.button_3.pack(pady=10)
        self.button_4 = neotkinter.NTkButton(master=self, text="asksaveasfile", command=lambda: print(neotkinter.filedialog.asksaveasfile()))
        self.button_4.pack(pady=10)
        self.button_5 = neotkinter.NTkButton(master=self, text="askopenfilename", command=lambda: print(neotkinter.filedialog.askopenfilename()))
        self.button_5.pack(pady=10)
        self.button_6 = neotkinter.NTkButton(master=self, text="askopenfilenames", command=lambda: print(neotkinter.filedialog.askopenfilenames()))
        self.button_6.pack(pady=10)
        self.button_7 = neotkinter.NTkButton(master=self, text="asksaveasfilename", command=lambda: print(neotkinter.filedialog.asksaveasfilename()))
        self.button_7.pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
