import os

LANGUAGE = os.getenv("LANGUAGE", "pt")

PUBLIC_ROUTES = [
    "/users/auth/register",
    "/users/auth/login",
    "/"
]