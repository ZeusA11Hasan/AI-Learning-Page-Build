import reflex as rx
from app.state import LandingState


def feature_card(feature: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(feature["icon"], class_name="text-3xl"), class_name="mb-4"
        ),
        rx.el.h3(feature["title"], class_name="text-xl font-bold text-white mb-2"),
        rx.el.p(feature["description"], class_name="text-gray-400"),
        class_name="relative p-8 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-sm transition-all duration-300 ease-in-out hover:bg-white/10 hover:shadow-2xl hover:shadow-purple-500/20 transform hover:-translate-y-2 hover:[transform:perspective(1000px)_rotateX(-5deg)_rotateY(5deg)]",
    )


def features_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Everything you need to succeed",
                class_name="text-3xl md:text-4xl font-bold tracking-tight text-center mb-4",
            ),
            rx.el.p(
                "StudyAI provides powerful tools to supercharge your learning.",
                class_name="text-lg md:text-xl text-gray-400 text-center mb-12 max-w-3xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(LandingState.features, feature_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="container mx-auto py-24 px-4 md:px-8",
        ),
        id="features",
        class_name="w-full bg-slate-900/50",
    )