# Dominic Minnich - April 2024


# Takes in a list of subfolders and a folder of pictures
#
# It will provide a ration of pictures to subfolders and moved the pictures into the subfolders accordingly
#
# The ratio must be a whole number
#
# This was designed for Student computer damage pictures to streamline the process of moving pictures to the correct student folder
#
# A bundle of pictures will be moved to a folder with the current date in the subfolder

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from datetime import datetime


class PictureMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Picture Mover")

        # Styling
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#F0F0F0")
        self.style.configure(
            "TButton",
            background="#4CAF50",
            foreground="white",
            font=("Helvetica", 10, "bold"),
            padx=10,
            pady=5,
        )
        self.style.configure(
            "TLabel", background="#F0F0F0", font=("Helvetica", 10), pady=5
        )

        # Layout
        self.left_frame = ttk.Frame(self.root)
        self.left_frame.pack(side="left", padx=10, pady=10)

        self.right_frame = ttk.Frame(self.root)
        self.right_frame.pack(side="right", padx=10, pady=10)

        self.title_label = ttk.Label(
            self.root, text="AutoClayton", font=("kristen itc", 20, "bold")
        )
        self.title_label.pack()

        self.title_label = ttk.Label(
            self.root, text="Dev: Dominic Minnich 2024", font=("Helvetica", 10, "bold")
        )
        self.title_label.pack()

        self.left_total_label = ttk.Label(self.left_frame, text="Total Subfolders: 0")
        self.left_total_label.pack()

        self.left_listbox = tk.Listbox(self.left_frame, selectmode=tk.SINGLE)
        self.left_listbox.pack(expand=True, fill="both")

        self.left_choose_button = ttk.Button(
            self.left_frame, text="Choose Directory", command=self.choose_directory
        )
        self.left_choose_button.pack(pady=10)

        self.right_total_label = ttk.Label(self.right_frame, text="Total Pictures: 0")
        self.right_total_label.pack()

        self.right_listbox = tk.Listbox(self.right_frame, selectmode=tk.SINGLE)
        self.right_listbox.pack(expand=True, fill="both")

        self.right_choose_button = ttk.Button(
            self.right_frame,
            text="Choose Picture Folder",
            command=self.choose_picture_folder,
        )
        self.right_choose_button.pack(pady=10)

        self.move_button = ttk.Button(
            self.root, text="Move Pictures", command=self.move_pictures
        )
        self.move_button.pack(pady=10)

        self.ratio = ttk.Label(self.root, text="")
        self.ratio.pack()

        self.picture_folder_path = ""
        self.subfolder_paths = []

    # Function to choose the directory with subfolders
    def choose_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.subfolder_paths = sorted(
                [
                    os.path.join(directory_path, d)
                    for d in os.listdir(directory_path)
                    if os.path.isdir(os.path.join(directory_path, d))
                ]
            )
            self.left_listbox.delete(0, tk.END)
            for path in self.subfolder_paths:
                self.left_listbox.insert(tk.END, os.path.basename(path))
            self.left_total_label.config(
                text="Total Subfolders: {}".format(len(self.subfolder_paths))
            )

    # Function to choose the directory with pictures
    def choose_picture_folder(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.picture_folder_path = directory_path
            picture_files = sorted(
                [
                    f
                    for f in os.listdir(directory_path)
                    if os.path.isfile(os.path.join(directory_path, f))
                ]
            )
            self.right_listbox.delete(0, tk.END)
            for file in picture_files:
                self.right_listbox.insert(tk.END, file)
            self.right_total_label.config(
                text="Total Pictures: {}".format(len(picture_files))
            )

            # Calculate ratio of pictures to subfolders and display it
            if len(self.subfolder_paths) > 0:
                ratio = len(picture_files) / len(self.subfolder_paths)
                self.ratio.config(
                    text="Ratio: {:.2f} pictures per subfolder".format(ratio)
                )
            else:
                self.ratio.config(text="No subfolders chosen yet")

    # Function to move the pictures to the subfolders
    def move_pictures(self):
        if not self.picture_folder_path or not self.subfolder_paths:
            messagebox.showerror(
                "Error",
                "Please choose both a picture folder and a directory with subfolders.",
            )
            return

        picture_files = self.right_listbox.get(0, tk.END)
        num_pictures = len(picture_files)
        num_subfolders = len(self.subfolder_paths)

        # Check if the ratio is a whole number
        if num_pictures % num_subfolders != 0:
            messagebox.showerror(
                "Error",
                "The ratio of pictures to subfolders is not a whole number. Please adjust your selection.",
            )
            return

        pics_per_subfolder = num_pictures // num_subfolders
        remainder = num_pictures % num_subfolders

        start_index = 0
        for i, subfolder_path in enumerate(self.subfolder_paths):
            num_to_move = pics_per_subfolder + (1 if i < remainder else 0)
            for j in range(num_to_move):
                picture_name = picture_files[start_index + j]
                date_folder_name = datetime.now().strftime("%m_%d_%Y")
                destination_folder = os.path.join(subfolder_path, date_folder_name)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.copy(
                    os.path.join(self.picture_folder_path, picture_name),
                    os.path.join(destination_folder, picture_name),
                )
                print(
                    "Moved {} to {}".format(
                        picture_name, os.path.basename(subfolder_path)
                    )
                )
            start_index += num_to_move

        messagebox.showinfo("Success", "Pictures moved successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PictureMoverApp(root)
    root.mainloop()
