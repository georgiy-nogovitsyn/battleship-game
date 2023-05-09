# Ship colors
CLEAN_CELL = (255, 255, 255)
DAMAGED_CELL = (128, 128, 255)
SHIP_CELL = (128, 128, 128)
DAMAGED_SHIP_CELL = (255, 128, 128)

# Game colors
HIGHLIGHT_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (200,200,200)

# Basic colors
GREY = (150, 150, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cell size
CELL = 30

# Settings for the game window
WIDTH = CELL * 23  # 800
HEIGHT = CELL * 12  # 500

# Offsets for correct rectangle drawing
left_border_offset = CELL
right_border_offset = WIDTH - CELL * 11
top_offset = CELL