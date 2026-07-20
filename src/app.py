import tkinter as tk


from PIL import Image, ImageTk

from src.media import choose_image



from src.sidebar import create_sidebar
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

media_files = []
current_image = None
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
def show_image(filename):

    global current_image

    image = Image.open(filename)

    image.thumbnail((700, 500))

    current_image = ImageTk.PhotoImage(image)

    preview_label.config(image=current_image)

    preview_label.image = current_image

    status.config(text=f"Viewing: {filename}")
def open_image():

    filename = choose_image()

    if filename:

        media_files.append(filename)

        media_list.insert(tk.END, filename.split("/")[-1])

        show_image(filename)

        status.config(text=f"Imported: {filename}")
    
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
# Media Library
# ==========================

library = tk.Frame(
    body,
    bg="#2B2B2B",
    width=220
)

library.pack(side="left", fill="y")

library_title = tk.Label(
    library,
    text="MEDIA LIBRARY",
    bg="#2B2B2B",
    fg="white",
    font=("Arial", 14, "bold")
)

library_title.pack(pady=10)

media_list = tk.Listbox(
    library,
    bg="#3C3C3C",
    fg="white",
    width=30,
    height=25
)

media_list.pack(padx=10, pady=10, fill="both", expand=True)

def on_media_select(event):

    selection = media_list.curselection()

    if not selection:
        return

    index = selection[0]

    filename = media_files[index]

    show_image(filename)

media_list.bind("<<ListboxSelect>>", on_media_select)

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