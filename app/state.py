import reflex as rx
from typing import TypedDict


class NavLink(TypedDict):
    name: str
    href: str


class LeaderboardEntry(TypedDict):
    rank: int
    name: str
    xp: int
    avatar: str


class CommunityMember(TypedDict):
    name: str
    handle: str
    avatar: str


class LandingState(rx.State):
    """The state for the landing page."""

    nav_links: list[NavLink] = [
        {"name": "Home", "href": "#home"},
        {"name": "Features", "href": "#features"},
        {"name": "XP Competition", "href": "#xp"},
        {"name": "Community", "href": "#community"},
    ]
    features: list[dict[str, str]] = [
        {
            "icon": "🧠",
            "title": "AI Trained on NCERT & PYQs",
            "description": "Personalized concept explanations.",
        },
        {
            "icon": "🗣️",
            "title": "Conversational Tutor Mode",
            "description": "Chat like a real teacher.",
        },
        {
            "icon": "🏆",
            "title": "Quiz + XP System",
            "description": "Earn XP from daily questions.",
        },
        {
            "icon": "⚡",
            "title": "Smart Progress Tracker",
            "description": "See strengths, fix weak spots.",
        },
    ]
    leaderboard: list[LeaderboardEntry] = [
        {
            "rank": 1,
            "name": "Rohan",
            "xp": 4800,
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Rohan",
        },
        {
            "rank": 2,
            "name": "Priya",
            "xp": 4500,
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Priya",
        },
        {
            "rank": 3,
            "name": "Amit",
            "xp": 4200,
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Amit",
        },
        {
            "rank": 4,
            "name": "Sneha",
            "xp": 3900,
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Sneha",
        },
        {
            "rank": 5,
            "name": "Vikram",
            "xp": 3600,
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Vikram",
        },
    ]
    community_members: list[CommunityMember] = [
        {
            "name": "Aarav",
            "handle": "@aarav",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Aarav",
        },
        {
            "name": "Isha",
            "handle": "@isha",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Isha",
        },
        {
            "name": "Kavya",
            "handle": "@kavya",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Kavya",
        },
        {
            "name": "Rhea",
            "handle": "@rhea",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Rhea",
        },
        {
            "name": "Zoya",
            "handle": "@zoya",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Zoya",
        },
        {
            "name": "Anika",
            "handle": "@anika",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Anika",
        },
    ]

    @rx.var
    def max_xp(self) -> int:
        return 5000

    @rx.event
    def handle_signup(self, form_data: dict):
        email = form_data.get("email")
        if email:
            print(f"New signup: {email}")
            return rx.toast.success(f"Thanks for signing up, {email}!")
        return rx.toast.error("Please enter a valid email.")