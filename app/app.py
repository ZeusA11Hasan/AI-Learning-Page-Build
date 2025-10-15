import reflex as rx
from app.state import LandingState
from app.components.navbar import navbar
from app.components.hero import hero_section
from app.components.features import features_section
from app.components.xp_competition import xp_competition_section
from app.components.community import community_section
from app.components.signup import signup_section
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        hero_section(),
        features_section(),
        xp_competition_section(),
        community_section(),
        signup_section(),
        footer(),
        class_name="font-['Inter'] bg-gradient-to-b from-[#0f172a] to-[#1e293b] text-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
    stylesheets=["/animations.css"],
)
app.add_page(index)