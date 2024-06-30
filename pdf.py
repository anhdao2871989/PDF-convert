import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def select_image_files():
    # Open a file dialog to select multiple image files
    image_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.png;*.gif")])
    
    # Update the image entry field with the selected file paths
    image_entry.delete(0, tk.END)
    image_entry.insert(0, ";".join(image_paths))

def select_output_folder():
    # Open a folder dialog to select the output folder
    output_folder = filedialog.askdirectory()
    
    # Update the output entry field with the selected folder path
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_folder)

def convert_to_pdf():
    try:
        # Get the image file paths from the user input
        image_paths = image_entry.get().split(";")
        
        # Get the output folder path from the user input
        output_folder = output_entry.get()
        
        # Convert each image to PDF and save it in the output folder
        for image_path in image_paths:
            img = Image.open(image_path)
            image = img.convert("RGB")
            output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0] + ".pdf")
            image.save(output_file, "PDF")
        
        # Update the status label
        status_label.config(text="PDF conversion successful!")
    except Exception as e:
        # Update the status label with the error message
        status_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("PDF Converter")

# Create the image label and entry
image_label = tk.Label(root, text="Image files:")
image_label.grid(row=0, column=0, padx=10, pady=10)

image_entry = tk.Entry(root)
image_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the "Select Files" button
select_button = tk.Button(root, text="Select Files", command=select_image_files)
select_button.grid(row=0, column=2, padx=10, pady=10)

# Create the output label and entry
output_label = tk.Label(root, text="Output folder:")
output_label.grid(row=1, column=0, padx=10, pady=10)

output_entry = tk.Entry(root)
output_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the "Select Folder" button
select_folder_button = tk.Button(root, text="Select Folder", command=select_output_folder)
select_folder_button.grid(row=1, column=2, padx=10, pady=10)

# Create the convert button
convert_button = tk.Button(root, text="Convert to PDF", command=convert_to_pdf)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Create the status label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Start the main event loop
root.mainloop()