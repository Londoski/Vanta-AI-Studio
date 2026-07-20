import tkinter as tk


def create_sidebar(parent):

    sidebar = tk.Frame(
        parent,
        bg="#252526",
        width=250
    )

    sidebar.pack(side="left", fill="y")

    title = tk.Label(
        sidebar,
        text="TOOLS",
        fg="white",
        bg="#252526",
        font=("Arial", 16, "bold")
    )

    title.pack(pady=20)

    return sidebar