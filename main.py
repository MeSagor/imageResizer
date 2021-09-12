import tkinter
from PIL import Image
from tkinter import filedialog, messagebox


class resizeWindow:
    def __init__(self):
        self.path = "empty"
        self.click = 0

        def browseFile():
            path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
            self.path = path
            self.click = 0
            self.pathLabel.configure(text="path: " + path)

        def resizeIt():
            if self.click == 0:
                if self.path == "empty":
                    messagebox.showerror("showerror", "Please select a picture.!")
                else:
                    self.click += 1
                    try:
                        w = Width.get()
                        h = Height.get()
                        imageFile = Image.open(self.path)
                        newImage = imageFile.resize((w, h))
                        newImage.save("modified_Image.jpg", quality=95, optimize=True)
                        messagebox.showinfo("showinfo", "Done")
                        newImage.show()
                    except:
                        messagebox.showerror("showerror", "Something got Bad.!")
            else:
                messagebox.showinfo("showinfo", "Already Resized or Error")

        self.win = tkinter.Tk(className="imageResizer")
        self.win.minsize(500, 400)
        self.win.maxsize(600, 500)
        Width = tkinter.IntVar(self.win, value=300, name="w")
        Height = tkinter.IntVar(self.win, value=400, name="h")

        filePath = tkinter.Button(self.win, text="Select Image", fg="green", command=browseFile)
        filePath.pack(pady=10)

        self.pathLabel = tkinter.Label(self.win, text="path:")
        self.pathLabel.pack(pady=5)

        labelWidth = tkinter.Label(self.win, text="Width")
        labelWidth.pack()
        entryWidth = tkinter.Entry(self.win, textvariable=Width)
        entryWidth.pack()
        labelHeight = tkinter.Label(self.win, text="Height")
        labelHeight.pack()
        entryHeight = tkinter.Entry(self.win, textvariable=Height)
        entryHeight.pack()

        # resizeIt = partial(resizeIt, Width, Height)
        resizeImage = tkinter.Button(self.win, text="Resize", fg="red", command=resizeIt)
        resizeImage.pack(pady=50)

        self.win.mainloop()


resizer = resizeWindow()
