import time
import neotkinter


class TestNTkButton():
    def __init__(self):
        self.root_ntk = neotkinter.NTk()
        self.ntk_button = neotkinter.NTkButton(self.root_ntk)
        self.ntk_button.pack(padx=20, pady=20)
        self.root_ntk.title(self.__class__.__name__)

    def clean(self):
        self.root_ntk.quit()
        self.root_ntk.withdraw()

    def main(self):
        self.execute_tests()
        self.root_ntk.mainloop()

    def execute_tests(self):
        print(f"\n{self.__class__.__name__} started:")

        start_time = 0

        self.root_ntk.after(start_time, self.test_iconify)
        start_time += 1500

        self.root_ntk.after(start_time, self.clean)

    def test_iconify(self):
        print(" -> test_iconify: ", end="")
        self.root_ntk.iconify()
        self.root_ntk.after(100, self.root_ntk.deiconify)
        print("successful")


if __name__ == "__main__":
    TestNTkButton().main()
