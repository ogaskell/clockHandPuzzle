from numpy import sign
from tkinter import *
import PIL
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.root = Tk()

        self.c_width  = 500
        self.c_height = 500

        self.c = Canvas(self.root,
                        width=self.c_width,
                        height=self.c_height,
                        bg="#ffffff")

        self.rotate_r = Button(self.root,
                               text=">>>",
                               command=lambda:self.rotate(-45))
        self.rotate_l = Button(self.root,
                               text="<<<",  
                               command=lambda:self.rotate(45))

        self.c.pack()
        self.rotate_l.pack()
        self.rotate_r.pack()

        self.oimg = Image.open("hand.png")
        self.img = self.oimg
        self.angle = 0
        self.pimg = ImageTk.PhotoImage(self.img)
        self.cimg = self.c.create_image(self.c_width/2,
                                        self.c_height/2,
                                        anchor=CENTER,
                                        image=self.pimg)

    def rotate(self,_angle):
        for angle in range(self.angle, self.angle + _angle + sign( _angle ), sign( _angle )):
            self.img = self.oimg.rotate(angle)
            self.pimg = ImageTk.PhotoImage(self.img)
            self.c.delete(self.cimg)
            self.cimg = self.c.create_image(self.c_width/2,
                                            self.c_height/2,
                                            anchor=CENTER,
                                            image=self.pimg)

            self.root.update()

        self.angle += _angle

if __name__ == "__main__":
    app = App()
    app.root.mainloop()
