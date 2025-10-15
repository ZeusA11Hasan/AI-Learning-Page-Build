import reflex as rx
from app.state import LandingState


def signup_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Start Your Learning Journey Today",
                    class_name="text-3xl md:text-4xl font-bold tracking-tight text-center mb-4",
                ),
                rx.el.p(
                    "Sign up to get early access and join the StudyAI community.",
                    class_name="text-lg md:text-xl text-gray-400 text-center mb-8 max-w-2xl mx-auto",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.input(
                            placeholder="Enter your email",
                            name="email",
                            type="email",
                            class_name="w-full md:w-auto flex-grow px-4 py-3 rounded-l-lg bg-white/5 border border-white/20 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500",
                            required=True,
                        ),
                        rx.el.button(
                            "Get Early Access",
                            type="submit",
                            class_name="bg-gradient-to-r from-indigo-500 to-purple-500 text-white px-6 py-3 rounded-r-lg font-semibold hover:opacity-90 transition-opacity",
                        ),
                        class_name="flex flex-col md:flex-row justify-center max-w-md mx-auto",
                    ),
                    on_submit=LandingState.handle_signup,
                    reset_on_submit=True,
                    class_name="w-full",
                ),
                class_name="max-w-4xl mx-auto p-8 md:p-12 rounded-2xl bg-slate-900/50 border border-white/10 backdrop-blur-sm shadow-2xl shadow-black/50",
            ),
            class_name="container mx-auto py-24 px-4 md:px-8",
        ),
        id="signup",
        class_name="w-full",
    )