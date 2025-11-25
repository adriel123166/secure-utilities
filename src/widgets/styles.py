# styles.py

# Define color palette
PRIMARY_COLOR = "#4A90E2"
SECONDARY_COLOR = "#D9E6F2"
ACCENT_COLOR = "#F5A623"
BACKGROUND_COLOR = "#FFFFFF"
TEXT_COLOR = "#333333"

# Define font styles
FONT_FAMILY = "Arial"
FONT_SIZE = 12
FONT_BOLD = "bold"

# Define button styles
BUTTON_STYLE = {
    "bg": PRIMARY_COLOR,
    "fg": BACKGROUND_COLOR,
    "font": (FONT_FAMILY, FONT_SIZE, FONT_BOLD),
    "activebackground": ACCENT_COLOR,
    "activeforeground": BACKGROUND_COLOR,
    "borderwidth": 2,
}

# Define label styles
LABEL_STYLE = {
    "bg": BACKGROUND_COLOR,
    "fg": TEXT_COLOR,
    "font": (FONT_FAMILY, FONT_SIZE),
}

# Define entry styles
ENTRY_STYLE = {
    "bg": SECONDARY_COLOR,
    "fg": TEXT_COLOR,
    "font": (FONT_FAMILY, FONT_SIZE),
    "borderwidth": 2,
}

# Define frame styles
FRAME_STYLE = {
    "bg": BACKGROUND_COLOR,
}