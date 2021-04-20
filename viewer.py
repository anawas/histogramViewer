import cv2
import tkinter as tk
from tkinter import filedialog as fd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

matplotlib.use("TkAgg")


def draw_histogram(histogram):
    ax.clear()
    ax.set_yscale('log')
    ax.set_xlabel('Grauwert')
    ax.set_xlim([0, 255])
    ax.set_ylabel('Anzahl')
    ax.plot(histogram)
    figure.canvas.draw()


def load_image():
    filetypes = (
        ("JPEG Bilder", "*.jpg"),
        ("PNG Bilder", "*.png")
    )
    filename = ""
    filename = fd.askopenfilename(
        title='Bild auswählen',
        filetypes=filetypes
    )
    entry_filename.insert(0, filename)
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    hist = calculate_histogram(image)
    draw_histogram(hist)


def calculate_histogram(image):
    return cv2.calcHist([image], [0], None, [256], [0, 256])


root = tk.Tk()
root.resizable(False, False)

label_filename = tk.Label(root, text='Dateiname', fg='black')
label_filename.grid(row=0, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

entry_filename = tk.Entry(root, text='', fg='black', bg='white')
entry_filename.grid(row=0, column=1, ipadx=5, pady=5, sticky=tk.W+tk.N)

button_filename = tk.Button(root, text="Öffnen", fg='black', command=load_image)
button_filename.grid(row=0, column=2, ipadx=5, pady=5, sticky=tk.W+tk.N)

figure = Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=1, columnspan=3)
#draw_histogram([])

root.mainloop()
