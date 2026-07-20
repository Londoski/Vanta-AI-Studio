from tkinter import filedialog


def choose_image():

    filename = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp")
        ]
    )

    return filename