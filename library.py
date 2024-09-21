from shutil import which
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import datetime
from backend.download import retrieve_downloads

def downloadFile(filename, timestamp):
    print(filename, timestamp)

root = ctk.CTk()

ico = Image.open('guiAssets/outstock.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


primary_color = "#F39C12"  # Burnt orange
secondary_color = "#2C3E50"  # Deep cool grey
button_color = "#1ABC9C"  # Teal
button_hover_color = "#16A085"  # Darker teal
font_main = ("Arial", 14)
font_header = ("Arial", 25, "bold")
text_color_light = "#ECF0F1"  # Light grey for text
text_color_dark = "#2C3E50"

root.configure(fg_color=secondary_color)

# Set the title and window size
root.title("OutStocker - Library")
root.geometry("516x908")
root.resizable(False, False)

# Create a canvas to hold the scrollable frame
canvas = Canvas(root, bg=secondary_color, highlightthickness=0)
canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

# Create a scrollbar for the canvas
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview, bg=secondary_color, troughcolor=secondary_color)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvas to work with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to contain the scrollable content, and place it inside the canvas
scrollable_frame = ctk.CTkFrame(master=canvas, fg_color=secondary_color, corner_radius=15)

# Update scrollable region to include the frame and its contents
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollable_frame.bind("<Configure>", update_scrollregion)

# Mouse Wheel scrolling (for both Windows and MacOS/Linux)
def on_mousewheel(event):
    if event.delta > 0:
        canvas.yview_scroll(event.delta, "units")
    else:
        if canvas.yview()[0] != 0.0:
            canvas.yview_scroll(event.delta, "units")
    # if event.delta:  # Windows and Linux systems (event.delta != 0)
    #     canvas.yview_scroll(-int(event.delta / 120), "units")
    # else:  # macOS systems (event.delta == 0, event.num is used)
    #     canvas.yview_scroll(-1 if event.num == 4 else 1, "units")

# Bind the mouse wheel scroll event
canvas.bind_all("<MouseWheel>", on_mousewheel)  # For Windows/Linux
canvas.bind_all("<Button-4>", on_mousewheel)  # For macOS
canvas.bind_all("<Button-5>", on_mousewheel)  # For macOS

# Header label (use grid instead of pack)
header_label = ctk.CTkLabel(master=scrollable_frame, text="OutStock download page", font=font_header, text_color="#D35400")
header_label.grid(row=0, column=0, columnspan=3, pady=20, padx=10)  # Add to grid with a colspan for centering

# Add the list of downloads with scrolling capability
for j in range(70):
    for index, i in enumerate(retrieve_downloads()):
        # Truncate the filename if it exceeds 15 characters
        if len(i[0]) >= 18:
            name = i[0][:15] + "..."
        else:
            name = i[0]

        # Convert timestamp to human-readable format
        timeStamp = datetime.datetime.fromtimestamp(int(i[1]) / 1000).strftime('%c')

        # Create the filename label
        label = ctk.CTkLabel(master=scrollable_frame,
            text=name,
            font=font_main,
            text_color=primary_color,
            fg_color="transparent")
        label.grid(row=index + j + 1, column=0, padx=20, pady=10, sticky=W)  # Shift rows by 1 because of the header

        # Create the timestamp label
        timeStampLabel = ctk.CTkLabel(
            master=scrollable_frame,
            text=timeStamp,
            font=("Arial", 13),
            text_color=primary_color,
            fg_color="transparent"
        )
        timeStampLabel.grid(row=index + j + 1, column=1, padx=10, pady=10, sticky=W)

        # Create the download button
        downloadButton = ctk.CTkButton(
            master=scrollable_frame,
            width=120,
            height=35,  # Increased height for better feel
            border_width=0,
            corner_radius=12,  # More rounded corners for modern look
            text="Download",
            font=font_main,
            fg_color=button_color,
            hover_color=button_hover_color,
            command=lambda filename=name, creationDate=i[1]: downloadFile(filename, creationDate)
        )
        downloadButton.grid(row=index + j + 1, column=2, padx=20, pady=10, sticky=E)

# Final configuration to enable scrolling
canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()