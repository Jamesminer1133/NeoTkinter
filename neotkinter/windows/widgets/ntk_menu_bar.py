"""
Custom Dropdown Menu for NTkMenuBar
Original Author: LucianoSaldivia | https://github.com/LucianoSaldivia
Modified by: Akash Bora (Akascape)
"""

from __future__ import annotations
from .ntk_button import NTkButton
from .ntk_frame import NTkFrame
from .ntk_frame import NTkFrame
from .theme import ThemeManager
from functools import partial
import tkinter as tk
from typing import Callable

"""
NeoTkinter Menu Bar
Author: Akash Bora
"""

class NTkMenuBar(NTkFrame):
    """
    A custom menu bar widget for NeoTkinter applications.
    
    This class creates a horizontal menu bar that can contain multiple menu buttons.
    Each button can be configured with custom text, colors, and callback functions.
    The menu bar automatically adapts its appearance based on the parent widget type.
    
    Attributes:
        height (int): Height of the menu bar
        width (int): Width of menu buttons
        num (int): Counter for the number of menu items added
        menu (list): List of associated dropdown menus
        padx (int): Horizontal padding for menu buttons
        pady (int): Vertical padding for menu buttons
    """
        
    def __init__(
        self,
        master,
        bg_color = None,
        height: int = 25,
        width: int = 10,
        padx: int = 5,
        pady: int = 2,
        **kwargs):
        """
        Initialize a NtkMenuBar instance.
        
        Creates a menu bar widget that automatically adapts its appearance based on
        whether it's placed in a NtkFrame or other widget type.
        
        Args:
            master: The parent widget to contain this menu bar
            bg_color: Background color (light, dark theme colors). Defaults to ["white","black"]
            height (int): Height of the menu bar in pixels. Defaults to 25
            width (int): Width of individual menu buttons in pixels. Defaults to 10
            padx (int): Horizontal padding between menu buttons. Defaults to 5
            pady (int): Vertical padding for menu buttons. Defaults to 2
            **kwargs: Additional arguments passed to the parent NtkFrame
        """

        if bg_color is None:
            bg_color = ThemeManager.theme["NTkFrame"]["fg_color"]

        if master.winfo_name().startswith("!ntkframe"):
            bg_corners = ["", "", bg_color, bg_color]
            corner = master.cget("corner_radius")
        else:
            bg_corners = ["", "", "", ""]
            corner = 0
            
        super().__init__(master, fg_color=bg_color, corner_radius=corner, height=height, background_corner_colors=bg_corners, **kwargs)
        self.height = height
        self.width = width
        self.after(10)
        self.num = 0
        self.menu = []
        self.padx = padx
        self.pady = pady

        super().pack(anchor="n", fill="x")

    def add_cascade(self, text=None, postcommand=None, **kwargs):
        """
        Add a menu button to the menu bar.
        
        Creates and adds a new menu button to the menu bar with customizable
        appearance and behavior. The button is automatically positioned in
        the next available column.
        
        Args:
            text (str, optional): The text label for the menu button.
                                If None, defaults to "Menu {number}"
            postcommand (callable, optional): Callback function to execute
                                            when the button is clicked
            **kwargs: Additional configuration options for the button including:
                - fg_color: Foreground/background color of the button
                - text_color: Color of the button text
                - anchor: Text alignment within the button
                - Other NtkButton configuration options
                
        Returns:
            neotkinter.NtkButton: The created menu button widget
        """
    
        if not "fg_color" in kwargs:
            fg_color = "transparent"
        else:
            fg_color = kwargs.pop("fg_color")
        if not "text_color" in kwargs:
            text_color = ThemeManager.theme["NTkLabel"]["text_color"]
        else:
            text_color = kwargs.pop("text_color")
            
        if not "anchor" in kwargs:
            anchor = "w"
        else:
            anchor = kwargs.pop("anchor")

        if text is None:
            text = f"Menu {self.num+1}"
            
        self.menu_button = NTkButton(self, text=text, fg_color=fg_color,
                                                   text_color=text_color, width=self.width,
                                                   height=self.height, anchor=anchor, **kwargs)
        self.menu_button.grid(row=0, column=self.num, padx=(self.padx,0), pady=self.pady)
        
        if postcommand:
            self.menu_button.bind("<Button-1>", lambda event: postcommand(), add="+")
            
        self.num += 1

        return self.menu_button
    
    def configure(self, **kwargs):
        """
        Configure the menu bar with various styling options.
        
        This method allows updating the menu bar's appearance after creation.
        The bg_color parameter is mapped to fg_color for consistency with
        the NtkFrame parent class.
        
        Args:
            **kwargs: Configuration options including:
                - bg_color: Background color (mapped to fg_color)
                - Other NtkFrame configuration options
        """
        if "bg_color" in kwargs:
           super().configure(fg_color=kwargs.pop("bg_color"))
        super().configure(**kwargs)