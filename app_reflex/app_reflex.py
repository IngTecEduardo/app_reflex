"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
print(root)
sys.path.append(str(root))

import reflex as rx
from rxconfig import config

from app_reflex.components.navbar import navbar_icons, navbar_icons_item

class State(rx.State):
    """The app state."""
    pass

def index() -> rx.Component:
    return rx.box(
        navbar_icons(),
    )


app = rx.App()
app.add_page(index)
app._compile()