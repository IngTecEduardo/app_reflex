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
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
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
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )

def index() -> rx.Component:
    return rx.container(
        navbar(),
    # # Welcome Page (Index)
    # return rx.container(
    #     rx.color_mode.button(position="top-right"),
    #     rx.vstack(
    #         rx.heading("Welcome to Reflex!", size="9"),
    #         rx.text(
    #             "Get started by editing ",
    #             rx.code(f"{config.app_name}/{config.app_name}.py"),
    #             size="5",
    #         ),
    #         rx.link(
    #             rx.button("Check out our docs!"),
    #             href="https://reflex.dev/docs/getting-started/introduction/",
    #             is_external=True,
    #         ),
    #         spacing="5",
    #         justify="center",
    #         min_height="85vh",
    #     ),
    #     rx.logo(),
    # )

    # def navbar_link(text: str, url: str) -> rx.Component:
    # return rx.link(
    #     rx.text(text, size="4", weight="medium"), href=url
    )


app = rx.App()
app.add_page(index)
app._compile()