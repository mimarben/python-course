import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")
        self.root.geometry("600x600")

        self.image = None
        self.tk_image = None

        # GUI Components
        self.load_btn = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_btn.pack(pady=10)

        self.canvas = tk.Canvas(root, width=500, height=400, bg="gray")
        self.canvas.pack()

        self.watermark_entry = tk.Entry(root, width=50)
        self.watermark_entry.pack(pady=10)
        self.watermark_entry.insert(0, "Enter watermark text here")

        self.apply_btn = tk.Button(root, text="Apply Watermark", command=self.apply_watermark)
        self.apply_btn.pack(pady=5)

        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_btn.pack(pady=5)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image = Image.open(file_path).convert("RGBA")
            self.display_image(self.image)

    def display_image(self, img):
        img_resized = img.resize((500, 400))
        self.tk_image = ImageTk.PhotoImage(img_resized)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def apply_watermark(self):
        if self.image is None:
            messagebox.showerror("Error", "Please load an image first.")
            return

        text = self.watermark_entry.get()
        watermark_img = self.image.copy()

        draw = ImageDraw.Draw(watermark_img)
        font = ImageFont.truetype("arial.ttf", 36)

        width, height = watermark_img.size
        textwidth, textheight = draw.textsize(text, font)

        x = width - textwidth - 20
        y = height - textheight - 20

        draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
        self.image = watermark_img
        self.display_image(watermark_img)

    def save_image(self):
        if self.image is None:
            messagebox.showerror("Error", "No image to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG Image", "*.png")])
        if file_path:
            self.image.save(file_path)
            messagebox.showinfo("Saved", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
