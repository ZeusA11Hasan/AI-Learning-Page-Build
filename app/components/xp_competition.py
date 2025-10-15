import reflex as rx
from app.state import LandingState


def leaderboard_item(entry: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(entry["rank"], class_name="font-bold text-lg text-indigo-400"),
            rx.image(src=entry["avatar"], class_name="w-10 h-10 rounded-full"),
            rx.el.span(entry["name"], class_name="font-medium text-white"),
            class_name="flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.span(f"{entry['xp']} XP", class_name="font-semibold text-white"),
            rx.el.div(
                rx.el.div(
                    class_name="h-full bg-gradient-to-r from-purple-500 to-pink-500 rounded-full",
                    style={
                        "width": f"{entry['xp'] / LandingState.max_xp * 100}%",
                        "transition": "width 1s ease-in-out",
                    },
                ),
                class_name="w-full h-2 bg-white/10 rounded-full overflow-hidden",
            ),
            class_name="flex items-center gap-4 w-1/3",
        ),
        class_name="flex items-center justify-between p-4 rounded-lg bg-white/5 border border-white/10",
    )


def xp_competition_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Join the XP Competition",
                class_name="text-3xl md:text-4xl font-bold tracking-tight text-center mb-4",
            ),
            rx.el.p(
                "Climb the ranks and earn your spot on the leaderboard.",
                class_name="text-lg md:text-xl text-gray-400 text-center mb-12 max-w-3xl mx-auto",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(LandingState.leaderboard, leaderboard_item),
                    class_name="space-y-4",
                ),
                class_name="max-w-4xl mx-auto p-8 rounded-2xl bg-slate-900/50 border border-white/10 backdrop-blur-sm",
            ),
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        "Join the XP Race",
                        class_name="mt-8 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 text-white px-8 py-3 rounded-lg font-semibold hover:opacity-90 transition-opacity shadow-lg shadow-purple-500/20 hover:shadow-purple-500/40",
                    ),
                    href="#signup",
                    on_click=lambda: rx.call_script(
                        "document.querySelector('#signup').scrollIntoView({behavior: 'smooth'})"
                    ),
                ),
                class_name="text-center",
            ),
            class_name="container mx-auto py-24 px-4 md:px-8",
        ),
        id="xp",
        class_name="w-full",
    )