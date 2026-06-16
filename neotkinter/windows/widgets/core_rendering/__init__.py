import sys

from .ntk_canvas import NTkCanvas
from .draw_engine import DrawEngine

NTkCanvas.init_font_character_mapping()

# determine draw method based on current platform
if sys.platform == "darwin":
    DrawEngine.preferred_drawing_method = "polygon_shapes"
else:
    DrawEngine.preferred_drawing_method = "font_shapes"
