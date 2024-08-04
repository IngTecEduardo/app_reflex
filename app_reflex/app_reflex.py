"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/logo.png",
                    width="2.25em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Trading", size="7", weight="bold"
                ),
                align_items="center",
            ),
            rx.hstack(
                navbar_link("Home", "/#"),
                navbar_link("About", "/#"),
                navbar_link("Pricing", "/#"),
                navbar_link("Contact", "/#"),
                justify="end",
                spacing="5",
            ),
            justify="between",
            align_items="center",
        ),
    bg=rx.color("accent", 3),
    padding="1em",
    # position="fixed",
    # top="0px",
    # z_index="5",
    width="100%",
)

def index() -> rx.Component:
    return rx.box(
        navbar(),
    )


app = rx.App()
app.add_page(index)
app._compile()