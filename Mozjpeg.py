import os
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import tempfile

class BulkMozjpegCompressor:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk MozJPEG Compressor")

        self.input_folder = ''
        self.output_folder = ''

        # Define the full path to cjpeg.exe
        # Modify this path to point to your cjpeg.exe location
        self.CJPEG_PATH = r'D:\mozjpeg\mozjpeg-v4.0.3-win-x64\shared\Release\cjpeg.exe'

        self.create_widgets()

    def create_widgets(self):
        # Input folder selection
        self.input_label = tk.Label(self.root, text="Input Folder:")
        self.input_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.grid(row=0, column=1, padx=10, pady=5)
        self.input_button = tk.Button(self.root, text="Browse", command=self.select_input_folder)
        self.input_button.grid(row=0, column=2, padx=10, pady=5)

        # Output folder selection
        self.output_label = tk.Label(self.root, text="Output Folder:")
        self.output_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.grid(row=1, column=1, padx=10, pady=5)
        self.output_button = tk.Button(self.root, text="Browse", command=self.select_output_folder)
        self.output_button.grid(row=1, column=2, padx=10, pady=5)

        # Compression Quality
        self.quality_label = tk.Label(self.root, text="Compression Quality (0-100):")
        self.quality_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.quality_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL)
        self.quality_scale.set(80)  # Default quality set to 80
        self.quality_scale.grid(row=2, column=1, padx=10, pady=5)

        # cjpeg.exe path
        self.cjpeg_label = tk.Label(self.root, text="Path to cjpeg.exe:")
        self.cjpeg_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.cjpeg_entry = tk.Entry(self.root, width=50)
        self.cjpeg_entry.grid(row=3, column=1, padx=10, pady=5)
        self.cjpeg_entry.insert(0, self.CJPEG_PATH)
        self.cjpeg_button = tk.Button(self.root, text="Browse", command=self.select_cjpeg_path)
        self.cjpeg_button.grid(row=3, column=2, padx=10, pady=5)

        # Filename prefix and suffix
        self.prefix_label = tk.Label(self.root, text="Filename Prefix:")
        self.prefix_label.grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.prefix_entry = tk.Entry(self.root, width=20)
        self.prefix_entry.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        self.suffix_label = tk.Label(self.root, text="Filename Suffix:")
        self.suffix_label.grid(row=5, column=0, padx=10, pady=5, sticky='e')
        self.suffix_entry = tk.Entry(self.root, width=20)
        self.suffix_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')

        # Option to replace original files
        self.replace_var = tk.BooleanVar()
        self.replace_check = tk.Checkbutton(self.root, text="Replace Original Files", variable=self.replace_var)
        self.replace_check.grid(row=6, column=1, padx=10, pady=5, sticky='w')

        # Start button
        self.start_button = tk.Button(self.root, text="Start Compression", command=self.start_compression)
        self.start_button.grid(row=7, column=1, padx=10, pady=15)

    def select_input_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.input_folder = folder_selected
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, folder_selected)

            # If replacing original files, set output folder to input folder
            if self.replace_var.get():
                self.output_entry.delete(0, tk.END)
                self.output_entry.insert(0, folder_selected)

    def select_output_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_folder = folder_selected
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder_selected)

    def select_cjpeg_path(self):
        file_selected = filedialog.askopenfilename(title="Select cjpeg.exe", filetypes=[("Executable Files", "*.exe")])
        if file_selected:
            self.CJPEG_PATH = file_selected
            self.cjpeg_entry.delete(0, tk.END)
            self.cjpeg_entry.insert(0, file_selected)

    def start_compression(self):
        if not self.input_entry.get():
            messagebox.showerror("Error", "Please select an input folder.")
            return
        if not self.output_entry.get() and not self.replace_var.get():
            messagebox.showerror("Error", "Please select an output folder.")
            return
        if not self.cjpeg_entry.get():
            messagebox.showerror("Error", "Please specify the path to cjpeg.exe.")
            return

        self.input_folder = self.input_entry.get()
        self.output_folder = self.output_entry.get()
        self.CJPEG_PATH = self.cjpeg_entry.get()
        quality = self.quality_scale.get()
        prefix = self.prefix_entry.get()
        suffix = self.suffix_entry.get()
        replace_original = self.replace_var.get()

        # Verify cjpeg.exe path
        if not os.path.isfile(self.CJPEG_PATH):
            messagebox.showerror("Error", "The specified cjpeg.exe path is invalid.")
            return

        # If replacing original files, set output folder to input folder
        if replace_original:
            self.output_folder = self.input_folder

        # Ensure output directory exists
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # Process the images
        supported_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
        error_files = []
        total_files = 0
        processed_files = 0

        for root_dir, _, files in os.walk(self.input_folder):
            for filename in files:
                if filename.endswith(supported_extensions):
                    total_files += 1
                    input_path = os.path.join(root_dir, filename)
                    relative_path = os.path.relpath(root_dir, self.input_folder)
                    output_dir = os.path.join(self.output_folder, relative_path)
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)

                    # Construct output filename
                    base_name, ext = os.path.splitext(filename)
                    output_filename = f"{prefix}{base_name}{suffix}.jpg"
                    output_path = os.path.join(output_dir, output_filename)

                    # Use mozjpeg to compress
                    try:
                        if filename.lower().endswith('.png'):
                            # Convert PNG to BMP using Pillow
                            with Image.open(input_path) as img:
                                img = img.convert('RGB')  # Ensure image is in RGB mode
                                with tempfile.NamedTemporaryFile(suffix='.bmp', delete=False) as temp_bmp:
                                    temp_bmp_name = temp_bmp.name
                                    img.save(temp_bmp_name, format='BMP')

                            # Compress BMP using mozjpeg
                            subprocess.run([
                                self.CJPEG_PATH,
                                '-quality', str(quality),
                                '-baseline',
                                '-optimize',
                                '-sample', '1x1',
                                '-outfile', output_path,
                                temp_bmp_name
                            ], check=True)

                            # Remove temporary BMP file
                            os.remove(temp_bmp_name)
                        else:
                            # Compress JPEG files directly
                            subprocess.run([
                                self.CJPEG_PATH,
                                '-quality', str(quality),
                                '-baseline',
                                '-optimize',
                                '-sample', '1x1',
                                '-outfile', output_path,
                                input_path
                            ], check=True)

                        # Replace original file if option is selected
                        if replace_original:
                            shutil.move(output_path, input_path)
                        processed_files += 1
                    except subprocess.CalledProcessError as e:
                        error_files.append((filename, str(e)))
                    except Exception as e:
                        error_files.append((filename, str(e)))

        # Display completion message
        if error_files:
            error_msg = f"Compression completed with errors.\n\nProcessed {processed_files} out of {total_files} files.\nFailed files:\n"
            for fname, err in error_files:
                error_msg += f"- {fname}: {err}\n"
            messagebox.showwarning("Completed with Errors", error_msg)
        else:
            messagebox.showinfo("Success", f"Compression completed successfully.\nProcessed {processed_files} files.")

if __name__ == '__main__':
    root = tk.Tk()
    app = BulkMozjpegCompressor(root)
    root.mainloop()
