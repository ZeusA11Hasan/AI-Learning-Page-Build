import reflex as rx
from app.state import LandingState


def nav_link(link: dict) -> rx.Component:
    """A navigation link component."""
    return rx.el.a(
        link["name"],
        href=link["href"],
        class_name="text-sm font-medium text-gray-300 hover:text-white transition-colors duration-200",
        on_click=lambda: rx.call_script(
            f"document.querySelector('{link['href']}').scrollIntoView({{behavior: 'smooth'}})"
        ),
    )


def navbar() -> rx.Component:
    """The navigation bar component."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.span("Study", class_name="text-white"),
                    rx.el.span("AI", class_name="text-indigo-400"),
                    href="#home",
                    class_name="text-2xl font-bold tracking-tighter",
                    on_click=lambda: rx.call_script(
                        "document.querySelector('#home').scrollIntoView({behavior: 'smooth'})"
                    ),
                ),
                class_name="flex items-center",
            ),
            rx.el.nav(
                rx.el.div(
                    rx.foreach(LandingState.nav_links, nav_link),
                    class_name="hidden md:flex items-center gap-6",
                ),
                rx.el.a(
                    rx.el.button(
                        "Get Started",
                        class_name="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 text-white px-4 py-2 rounded-lg text-sm font-medium hover:opacity-90 transition-opacity duration-200 shadow-[0_0_15px_rgba(79,70,229,0.5)]",
                    ),
                    href="#signup",
                    on_click=lambda: rx.call_script(
                        "document.querySelector('#signup').scrollIntoView({behavior: 'smooth'})"
                    ),
                ),
                class_name="flex items-center gap-6",
            ),
            class_name="container mx-auto flex items-center justify-between p-4",
        ),
        class_name="sticky top-0 z-50 w-full border-b border-white/10 bg-black/30 backdrop-blur-lg",
    )