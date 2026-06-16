import neotkinter


class TestNTkToplevel():
    def __init__(self):
        self.root_ntk = neotkinter.NTk()
        self.root_ntk.title("TestNTkToplevel")
        self.ntk_toplevel = neotkinter.NTkToplevel()
        self.ntk_toplevel.title("TestNTkToplevel")

    def clean(self):
        self.root_ntk.quit()
        self.ntk_toplevel.withdraw()
        self.root_ntk.withdraw()

    def main(self):
        self.execute_tests()
        self.root_ntk.mainloop()

    def execute_tests(self):
        print("\nTestNTkToplevel started:")
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
        self.ntk_toplevel.geometry("200x300+200+300")
        assert self.ntk_toplevel.current_width == 200 and self.ntk_toplevel.current_height == 300

        self.ntk_toplevel.minsize(300, 400)
        assert self.ntk_toplevel.current_width == 300 and self.ntk_toplevel.current_height == 400
        assert self.ntk_toplevel.min_width == 300 and self.ntk_toplevel.min_height == 400

        self.ntk_toplevel.maxsize(400, 500)
        self.ntk_toplevel.geometry("600x600")
        assert self.ntk_toplevel.current_width == 400 and self.ntk_toplevel.current_height == 500
        assert self.ntk_toplevel.max_width == 400 and self.ntk_toplevel.max_height == 500

        self.ntk_toplevel.maxsize(1000, 1000)
        self.ntk_toplevel.geometry("300x400")
        self.ntk_toplevel.resizable(False, False)
        self.ntk_toplevel.geometry("500x600")
        assert self.ntk_toplevel.current_width == 500 and self.ntk_toplevel.current_height == 600
        print("successful")

    def test_scaling(self):
        print(" -> test_scaling: ", end="")

        neotkinter.ScalingTracker.set_window_scaling(1.5)
        self.ntk_toplevel.geometry("300x400")
        assert self.ntk_toplevel.current_width == 300 and self.ntk_toplevel.current_height == 400
        assert self.root_ntk.window_scaling == 1.5 * neotkinter.ScalingTracker.get_window_dpi_scaling(self.root_ntk)

        self.ntk_toplevel.maxsize(400, 500)
        self.ntk_toplevel.geometry("500x500")
        assert self.ntk_toplevel.current_width == 400 and self.ntk_toplevel.current_height == 500

        neotkinter.ScalingTracker.set_window_scaling(1)
        assert self.ntk_toplevel.current_width == 400 and self.ntk_toplevel.current_height == 500
        print("successful")

    def test_configure(self):
        print(" -> test_configure: ", end="")
        self.ntk_toplevel.configure(bg="white")
        assert self.ntk_toplevel.fg_color == "white"

        self.ntk_toplevel.configure(background="red")
        assert self.ntk_toplevel.fg_color == "red"
        assert self.ntk_toplevel.cget("bg") == "red"

        self.ntk_toplevel.config(fg_color=("green", "#FFFFFF"))
        assert self.ntk_toplevel.fg_color == ("green", "#FFFFFF")
        print("successful")

    def test_appearance_mode(self):
        print(" -> test_appearance_mode: ", end="")
        neotkinter.set_appearance_mode("light")
        self.ntk_toplevel.config(fg_color=("green", "#FFFFFF"))
        assert self.ntk_toplevel.cget("bg") == "green"

        neotkinter.set_appearance_mode("dark")
        assert self.ntk_toplevel.cget("bg") == "#FFFFFF"
        print("successful")

    def test_iconify(self):
        print(" -> test_iconify: ", end="")
        self.ntk_toplevel.iconify()
        self.ntk_toplevel.after(100, self.ntk_toplevel.deiconify)
        print("successful")


if __name__ == "__main__":
    TestNTkToplevel()
