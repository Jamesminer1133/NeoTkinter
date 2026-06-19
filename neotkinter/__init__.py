__version__ = "5.2.2"

import os
import sys
from tkinter import Variable, StringVar, IntVar, DoubleVar, BooleanVar
from tkinter.constants import *
import tkinter.filedialog as filedialog

# import manager classes
from .windows.widgets.appearance_mode import AppearanceModeTracker
from .windows.widgets.font import FontManager
from .windows.widgets.scaling import ScalingTracker
from .windows.widgets.theme import ThemeManager
from .windows.widgets.core_rendering import DrawEngine

# import base widgets
from .windows.widgets.core_rendering import NTkCanvas
from .windows.widgets.core_widget_classes import NTkBaseClass

# import widgets
from .windows.widgets import NTkButton
from .windows.widgets import NTkCheckBox
from .windows.widgets import NTkComboBox
from .windows.widgets import NTkEntry
from .windows.widgets import NTkFrame
from .windows.widgets import NTkLabel
from .windows.widgets import NTkOptionMenu
from .windows.widgets import NTkProgressBar
from .windows.widgets import NTkRadioButton
from .windows.widgets import NTkScrollbar
from .windows.widgets import NTkSegmentedButton
from .windows.widgets import NTkSlider
from .windows.widgets import NTkSwitch
from .windows.widgets import NTkTabview
from .windows.widgets import NTkTextbox
from .windows.widgets import NTkScrollableFrame
from .windows.widgets import NTkDropdownMenu
from .windows.widgets import NTkMenuBar

# import windows
from .windows import NTk
from .windows import NTkToplevel
from .windows import NTkInputDialog
from .windows import NTkTitleMenu
from .windows import NTkScrollableDropdown
from .windows import NTkScrollableDropdownFrame
from .windows import NTkMessagebox

# import font classes
from .windows.widgets.font import NTkFont

# import image classes
from .windows.widgets.image import NTkImage

from .windows import ntk_tk

_ = Variable, StringVar, IntVar, DoubleVar, BooleanVar, CENTER, filedialog  # prevent IDE from removing unused imports


def set_appearance_mode(mode_string: str):
    """ possible values: light, dark, system """
    AppearanceModeTracker.set_appearance_mode(mode_string)


def get_appearance_mode() -> str:
    """ get current state of the appearance mode (light or dark) """
    if AppearanceModeTracker.appearance_mode == 0:
        return "Light"
    elif AppearanceModeTracker.appearance_mode == 1:
        return "Dark"


def set_default_color_theme(color_string: str):
    """ set color theme or load custom theme file by passing the path """
    ThemeManager.load_theme(color_string)


def set_widget_scaling(scaling_value: float):
    """ set scaling for the widget dimensions """
    ScalingTracker.set_widget_scaling(scaling_value)


def set_window_scaling(scaling_value: float):
    """ set scaling for window dimensions """
    ScalingTracker.set_window_scaling(scaling_value)


def deactivate_automatic_dpi_awareness():
    """ deactivate DPI awareness of current process (windll.shcore.SetProcessDpiAwareness(0)) """
    ScalingTracker.deactivate_automatic_dpi_awareness = True


def set_ntk_parent_class(ntk_parent_class):
    ntk_tk.NTK_PARENT_CLASS = ntk_parent_class
