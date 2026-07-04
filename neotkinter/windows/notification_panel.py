from neotkinter.windows.widgets.ntk_frame import NTkFrame
from neotkinter.windows.widgets.theme import ThemeManager
from neotkinter.windows.widgets.ntk_label import NTkLabel
from neotkinter.windows.widgets.ntk_button import NTkButton
import tkinter as tk
from .notification_type import NotifyType


class NotificationPanel(NTkFrame):
    def __init__(
        self,
        master,
        manager,
        message,
        notify_type=NotifyType.INFO,
        duration=5000,
        bg_color=ThemeManager.get("NTk", "fg_color"),
        text_color=ThemeManager.get("NTkLabel", "text_color")
    ):
        text_length = len(message)
        width = max(250, min(600, text_length * 7))
        height = 50

        super().__init__(
            master, corner_radius=0, fg_color=bg_color, width=width, height=height
        )
        self.pack_propagate(False)
        self.duration = duration
        self.manager = manager

        self.line_frame = NTkFrame(
            self, width=5, height=height, fg_color=notify_type.line_color
        )
        self.line_frame.place(relx=0, rely=0, anchor="nw")

        self.label = NTkLabel(
            self,
            text=message,
            text_color=text_color,
            anchor="w",
            font=("Arial", 12),
            justify="left",
            wraplength=width - 50,
        )
        self.label.pack(pady=5, padx=(15, 10), fill="both", expand=True)

        self.close_button = NTkButton(
            self,
            text="✖",
            width=15,
            height=15,
            command=self.removeNotification,
            fg_color="transparent",
            hover_color=bg_color,
            text_color=text_color,
            corner_radius=10,
        )
        self.close_button.place(relx=0.98, rely=0.1, anchor="ne")

        self.manager.addNotification(self)

        self.after(duration, self.removeNotification)

    def removeNotification(self):
        self.manager.removeNotification(self)
        self.destroy()
