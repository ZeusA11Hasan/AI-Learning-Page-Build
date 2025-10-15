import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.el.span("Study", class_name="text-white"),
                        rx.el.span("AI", class_name="text-indigo-400"),
                        href="#home",
                        class_name="text-xl font-bold tracking-tighter",
                        on_click=lambda: rx.call_script(
                            "document.querySelector('#home').scrollIntoView({behavior: 'smooth'})"
                        ),
                    ),
                    class_name="mb-4 md:mb-0",
                ),
                rx.el.div(
                    rx.el.a(
                        "About",
                        href="#",
                        class_name="text-sm text-gray-400 hover:text-white transition-colors",
                    ),
                    rx.el.a(
                        "Contact",
                        href="#",
                        class_name="text-sm text-gray-400 hover:text-white transition-colors",
                    ),
                    rx.el.a(
                        "Privacy",
                        href="#",
                        class_name="text-sm text-gray-400 hover:text-white transition-colors",
                    ),
                    rx.el.a(
                        "Terms",
                        href="#",
                        class_name="text-sm text-gray-400 hover:text-white transition-colors",
                    ),
                    class_name="flex items-center gap-6",
                ),
                class_name="flex flex-col md:flex-row items-center justify-between",
            ),
            rx.el.div(class_name="border-t border-white/10 my-8"),
            rx.el.div(
                rx.el.p(
                    "© 2025 StudyAI. Built with ❤️ using GPT-5.",
                    class_name="text-sm text-gray-500",
                ),
                class_name="text-center",
            ),
            class_name="container mx-auto py-8 px-4 md:px-8",
        ),
        class_name="w-full bg-slate-900",
    )