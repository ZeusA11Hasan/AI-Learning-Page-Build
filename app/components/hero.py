import reflex as rx


def animated_background() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute top-0 left-0 w-full h-full bg-gradient-to-b from-slate-900 to-slate-800 -z-10"
        ),
        rx.el.div(
            class_name="absolute top-1/2 left-1/4 w-96 h-96 bg-indigo-600 rounded-full filter blur-3xl opacity-20 animate-blob"
        ),
        rx.el.div(
            class_name="absolute top-1/4 right-1/4 w-96 h-96 bg-purple-600 rounded-full filter blur-3xl opacity-20 animate-blob animation-delay-2000"
        ),
        rx.el.div(
            class_name="absolute bottom-8 left-1/3 w-96 h-96 bg-pink-600 rounded-full filter blur-3xl opacity-20 animate-blob animation-delay-4000"
        ),
        class_name="absolute inset-0 w-full h-full overflow-hidden",
    )


def macbook_scroll_mockup() -> rx.Component:
    """A mockup of the macbook scroll component."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(class_name="h-2 w-2 rounded-full bg-red-500"),
            rx.el.div(class_name="h-2 w-2 rounded-full bg-yellow-500"),
            rx.el.div(class_name="h-2 w-2 rounded-full bg-green-500"),
            class_name="flex items-center gap-2 p-2 bg-gray-800 border-b border-gray-700",
        ),
        rx.el.div(
            rx.image(
                src="/placeholder.svg",
                class_name="w-full h-auto object-cover opacity-50",
            ),
            rx.el.p(
                "MacbookScroll UI Animation Demo",
                class_name="absolute inset-0 flex items-center justify-center text-sm text-gray-400",
            ),
            class_name="relative bg-gray-900 p-4 aspect-[4/3] w-full",
        ),
        class_name="w-full max-w-2xl mx-auto rounded-t-lg border border-gray-700 overflow-hidden shadow-2xl shadow-black/50",
    )


def hero_section() -> rx.Component:
    return rx.el.section(
        animated_background(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Learn Smarter with ",
                        rx.el.span(
                            "StudyAI",
                            class_name="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400",
                        ),
                        " 💡",
                        class_name="text-4xl md:text-6xl font-bold tracking-tighter mb-6",
                    ),
                    rx.el.p(
                        "Your AI study buddy trained with NCERT, PYQs & interactive quizzes.",
                        class_name="text-lg md:text-xl text-gray-300 max-w-2xl mb-8",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.el.button(
                                "Start Learning",
                                class_name="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 text-white px-6 py-3 rounded-lg font-semibold hover:opacity-90 transition-opacity shadow-lg shadow-indigo-500/20 hover:shadow-indigo-500/40",
                            ),
                            href="#signup",
                            on_click=lambda: rx.call_script(
                                "document.querySelector('#signup').scrollIntoView({behavior: 'smooth'})"
                            ),
                        ),
                        rx.el.a(
                            rx.el.button(
                                "Try Quiz Mode",
                                class_name="bg-white/10 border border-white/20 text-white px-6 py-3 rounded-lg font-semibold hover:bg-white/20 transition-colors",
                            ),
                            href="#features",
                            on_click=lambda: rx.call_script(
                                "document.querySelector('#features').scrollIntoView({behavior: 'smooth'})"
                            ),
                        ),
                        class_name="flex items-center gap-4",
                    ),
                    class_name="flex-1 flex flex-col justify-center items-start z-10 p-4 md:p-8",
                ),
                rx.el.div(
                    macbook_scroll_mockup(),
                    class_name="flex-1 flex items-center justify-center p-4 md:p-8",
                ),
                class_name="container mx-auto grid md:grid-cols-2 gap-8 items-center",
            )
        ),
        id="home",
        class_name="relative w-full min-h-screen flex items-center justify-center overflow-hidden",
    )