import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
# ==========================
# Create Main Window
# ==========================

app = tk.Tk()
app.title("Vanta AI Studio")
app.geometry("1200x700")
app.configure(bg="#1E1E1E")

# ==========================
# Top Menu Bar
# ==========================

menu_bar = tk.Frame(
    app,
    bg="#2D2D2D",
    height=50
)

menu_bar.pack(fill="x")

title = tk.Label(
    menu_bar,
    text="VANTA AI STUDIO",
    fg="white",
    bg="#2D2D2D",
    font=("Arial", 18, "bold")
)

title.pack(side="left", padx=20, pady=10)

# ==========================
# Main Body
# ==========================

body = tk.Frame(app, bg="#1E1E1E")
body.pack(fill="both", expand=True)

# ==========================
# Left Sidebar
# ==========================

sidebar = tk.Frame(
    body,
    bg="#252526",
    width=250
)

sidebar.pack(side="left", fill="y")

# Sidebar Title
sidebar_title = tk.Label(
    sidebar,
    text="TOOLS",
    fg="white",
    bg="#252526",
    font=("Arial", 16, "bold")
)

sidebar_title.pack(pady=20)

# Buttons
buttons = [
    "📁 Images",
    "🎵 Audio",
    "🎬 Videos",
    "✨ Effects",
    "📝 Captions",
    "⚙ Settings"
]
def open_image():

    filename = filedialog.askopenfilename(

        title="Select an Image",

        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp")
        ]

    )

    if filename:

        image = Image.open(filename)

        image.thumbnail((700, 500))

        photo = ImageTk.PhotoImage(image)

        preview_label.config(image=photo)

        preview_label.image = photo

        status.config(text=f"Selected: {filename}")
for text in buttons:
    btn = tk.Button(
        sidebar,
        text=text,
        width=20,
        height=2,
        bg="#3C3C3C",
        fg="white",
        relief="flat",
        command=open_image if text == "📁 Images" else None
)
    btn.pack(pady=6)

# ==========================
# Preview Area
# ==========================

preview = tk.Frame(
    body,
    bg="#333333"
)

preview.pack(side="left", fill="both", expand=True, padx=10, pady=10)

preview_label = tk.Label(
    preview,
    bg="#333333"
)

preview_label.pack(expand=True)

# ==========================
# Status Bar
# ==========================

status = tk.Label(
    app,
    text="Status: Ready",
    anchor="w",
    bg="#2D2D2D",
    fg="white"
)

status.pack(fill="x")

# ==========================
# Run Application
# ==========================

app.mainloop()