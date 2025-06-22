# GUI code for attendance-system1 (interface only)
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("IT Dep.")
root.geometry("1000x600")
root.configure(bg="#ECD4C0")

# Header
header_frame = tk.Frame(root, bg="#dbeafe")
header_frame.pack(pady=10, fill="x")

try:
    logo_img = Image.open("logo.png")
    logo_img = logo_img.resize((60, 60), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(header_frame, image=logo_photo, bg="#dbeafe")
    logo_label.image = logo_photo
    logo_label.pack(side="left", padx=10)
except Exception as e:
    print("Logo not found:", e)

title_label = tk.Label(
    header_frame,
    text="مجموعة شركات بدوى بيكو\nقسم تكنولوجيا المعلومات\nحركات التنقل بين المصانع",
    font=("Arial", 16, "bold"),
    fg="#003366",
    bg="#dbeafe",
    justify="right"
)
title_label.pack(side="left", padx=10)

# Run
root.mainloop()
