import reflex as rx
from app.state import LandingState


def community_card(member: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=member["avatar"], class_name="w-16 h-16 rounded-full mb-4 mx-auto"
        ),
        rx.el.h3(member["name"], class_name="text-lg font-bold text-white"),
        rx.el.p(member["handle"], class_name="text-sm text-gray-400"),
        class_name="text-center p-6 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-sm",
    )


def community_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                class_name="absolute inset-0 -z-10 h-full w-full bg-white [mask-image:radial-gradient(100%_100%_at_top_right,white,transparent)]"
            ),
            rx.el.h2(
                "Join thousands of students learning smarter.",
                class_name="text-3xl md:text-4xl font-bold tracking-tight text-center mb-4 text-slate-800",
            ),
            rx.el.p(
                "Become part of a vibrant community of learners and achievers.",
                class_name="text-lg md:text-xl text-slate-600 text-center mb-12 max-w-3xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(LandingState.community_members, community_card),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4",
            ),
            class_name="container mx-auto py-24 px-4 md:px-8",
        ),
        id="community",
        class_name="w-full bg-white",
    )