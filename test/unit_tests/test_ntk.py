import time
import neotkinter


class TestNTk():
    def __init__(self):
        self.root_ntk = neotkinter.NTk()
        self.root_ntk.title("TestNTk")

    def clean(self):
        self.root_ntk.quit()
        self.root_ntk.withdraw()

    def main(self):
        self.execute_tests()
        self.root_ntk.mainloop()

    def execute_tests(self):
        print("\nTestNTk started:")
        start_time = 0

        self.root_ntk.after(start_time, self.test_geometry)
        start_time += 100

        self.root_ntk.after(start_time, self.test_scaling)
        start_time += 100

        self.root_ntk.after(start_time, self.test_configure)
        start_time += 100

        self.root_ntk.after(start_time, self.test_appearance_mode)
        start_time += 100

        self.root_ntk.after(start_time, self.test_iconify)
        start_time += 1500

        self.root_ntk.after(start_time, self.clean)

    def test_geometry(self):
        print(" -> test_geometry: ", end="")
        self.root_ntk.geometry("100x200+200+300")
        assert self.root_ntk.current_width == 100 and self.root_ntk.current_height == 200

        self.root_ntk.minsize(300, 400)
        assert self.root_ntk.current_width == 300 and self.root_ntk.current_height == 400
        assert self.root_ntk.min_width == 300 and self.root_ntk.min_height == 400

        self.root_ntk.maxsize(400, 500)
        self.root_ntk.geometry("600x600")
        assert self.root_ntk.current_width == 400 and self.root_ntk.current_height == 500
        assert self.root_ntk.max_width == 400 and self.root_ntk.max_height == 500

        self.root_ntk.maxsize(1000, 1000)
        self.root_ntk.geometry("300x400")
        self.root_ntk.resizable(False, False)
        self.root_ntk.geometry("500x600")
        assert self.root_ntk.current_width == 500 and self.root_ntk.current_height == 600
        print("successful")

    def test_scaling(self):
        print(" -> test_scaling: ", end="")

        neotkinter.ScalingTracker.set_window_scaling(1.5)
        self.root_ntk.geometry("300x400")
        assert self.root_ntk._current_width == 300 and self.root_ntk._current_height == 400
        assert self.root_ntk.window_scaling == 1.5 * neotkinter.ScalingTracker.get_window_dpi_scaling(self.root_ntk)

        self.root_ntk.maxsize(400, 500)
        self.root_ntk.geometry("500x500")
        assert self.root_ntk._current_width == 400 and self.root_ntk._current_height == 500

        neotkinter.ScalingTracker.set_window_scaling(1)
        assert self.root_ntk._current_width == 400 and self.root_ntk._current_height == 500
        print("successful")

    def test_configure(self):
        print(" -> test_configure: ", end="")
        self.root_ntk.configure(bg="white")
        assert self.root_ntk.cget("fg_color") == "white"

        self.root_ntk.configure(background="red")
        assert self.root_ntk.cget("fg_color") == "red"
        assert self.root_ntk.cget("bg") == "red"

        self.root_ntk.config(fg_color=("green", "#FFFFFF"))
        assert self.root_ntk.cget("fg_color") == ("green", "#FFFFFF")
        print("successful")

    def test_appearance_mode(self):
        print(" -> test_appearance_mode: ", end="")
        neotkinter.set_appearance_mode("light")
        self.root_ntk.config(fg_color=("green", "#FFFFFF"))
        assert self.root_ntk.cget("bg") == "green"

        neotkinter.set_appearance_mode("dark")
        assert self.root_ntk.cget("bg") == "#FFFFFF"
        print("successful")

    def test_iconify(self):
        print(" -> test_iconify: ", end="")
        self.root_ntk.iconify()
        self.root_ntk.after(100, self.root_ntk.deiconify)
        print("successful")


if __name__ == "__main__":
    TestNTk().main()
