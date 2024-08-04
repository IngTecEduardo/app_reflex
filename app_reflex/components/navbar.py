import reflex as rx

def navbar_icons_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
    )

def navbar_icons() -> rx.Component:
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
                    "My Trading App", size="7", weight="bold"
                ),
                align_items="center",
            ),
            rx.hstack(
                navbar_icons_item("Home", "home", "/#"),
                navbar_icons_item("Pricing", "coins", "/#"),
                navbar_icons_item("Contact", "mail", "/#"),
                navbar_icons_item("Services", "layers", "/#"),
                spacing="6",
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