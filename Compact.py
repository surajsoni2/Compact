from PIL import ImageTk
from PIL import Image as PilImage
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

class ImageCompressor(Tk):
    def __init__(self, winTitle, xSize, ySize, *args):
        super(ImageCompressor, self).__init__()
        if args:
            self.configure(bg=args[0])
        self.geometry(f"{xSize}x{ySize}")
        self.title(winTitle)
        self.resizable(False, False)
        self.compressFile = Button(text="Choose Image", command =self.GetImageFile)
        self.compressFile.place(x=25,y=15)
        self.chooseQuality = Label(self, text = "Choose Quality", font = ('Courier',10))
        self.chooseQuality.place(x=60,y=70)
        self.scaleValue = Scale(self, from_=0,to=100)
        self.scaleValue.place(x=0,y=70)
        self.saveFolder = Button(text = "Choose which folder to save to", command= self.saveFolder)

        self.saveFolder.place(x=62.5,y=100)

        self.imageNameLabel = Label(text = "Enter new file name")
        self.imageNameLabel.place(x=62.5,y=135)

        self.imageName = Entry(self, bd=3)
        self.imageName.place(x=62.5,y=160)

        self.compressImageBtn = Button(text = "Compress Image",command=self.CompressImage,bd=5)
        self.compressImageBtn.place(x=290,y=90)
        self.mainloop()

    def GetImageFile(self):
        self.compressLocation = filedialog.askopenfilename()
        if self.compressLocation:
            messagebox.showwarning("File",self.compressLocation)
        else:
            messagebox.showwarning("Error","NO image selected")

    def saveFolder(self):
        self.saveTo = filedialog.askdirectory()
        if self.saveTo:
            messagebox.showwarning("Save to:",self.saveTo)
        else:
            messagebox.showwarning("Error","No folder selected")

    def CompressImage(self):
        self.scaleNum = self.scaleValue.get()
        try:
            self.imageToCompress = PilImage.open(self.compressLocation)
            self.getImageExtension= self.compressLocation.rsplit(".",1)
            self.imageExtension= self.getImageExtension[1]
            self.imageEntryName = self.imageName.get()
            self.imageToCompress.save(f"{self.saveTo}/{self.imageEntryName}.{self.imageExtension}",quality=self.scaleNum)
            messagebox.showinfo("Successful",f"Compressed image saved to {self.saveTo}")
        except:
            messagebox.showwarning("Error","Somthing went wrong")


GUI = ImageCompressor("Image Compressor",450,225)
