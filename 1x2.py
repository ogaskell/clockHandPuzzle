from numpy import sign
from tkinter import *
import PIL
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.root = Tk()

        self.c_width  = 500
        self.c_height = 250

        self.c = Canvas(self.root,
                        width=self.c_width,
                        height=self.c_height,
                        bg="#ffffff")

        self.c.grid(row=0,column=0,columnspan=4)

        self.imgs = {}
        self.pimgs = {}
        self.cimgs = {}
        self.angles = {}
        self.coords = {(0,0):[1*(self.c_width/4),1*(self.c_height/2)],
                       (1,0):[3*(self.c_width/4),1*(self.c_height/2)]}

        self.oimg = Image.open("hand.png")
        self.imgs[(0,0)] = self.oimg
        self.angles[(0,0)] = 0
        self.pimgs[(0,0)] = ImageTk.PhotoImage(self.imgs[(0,0)])
        self.cimgs[(0,0)] = self.c.create_image(self.coords[(0,0)][0],
                                                self.coords[(0,0)][1],
                                                anchor=CENTER,
                                                image=self.pimgs[(0,0)])

        self.imgs[(1,0)] = self.oimg
        self.angles[(1,0)] = 0
        self.pimgs[(1,0)] = ImageTk.PhotoImage(self.imgs[(1,0)])
        self.cimgs[(1,0)] = self.c.create_image(self.coords[(1,0)][0],
                                                self.coords[(1,0)][1],
                                                anchor=CENTER,
                                                image=self.pimgs[(1,0)])

        self.c.bind("<Button-1>", self.click)
    
    def rotate(self,coord,_angle):
        for angle in range(self.angles[coord], self.angles[coord] + _angle + sign( _angle ), sign( _angle )):
            self.imgs[coord] = self.oimg.rotate(angle)
            self.pimgs[coord] = ImageTk.PhotoImage(self.imgs[coord])
            self.c.delete(self.cimgs[coord])
            self.cimgs[coord] = self.c.create_image(self.coords[coord][0],
                                                    self.coords[coord][1],
                                                    anchor=CENTER,
                                                    image=self.pimgs[coord])

            self.root.update()


        self.angles[coord] += _angle

    def click(self,event):
        if event.x < 125:
            self.rotate((0,0),45)
        elif event.x >= 125 and event.x < 250:
            self.rotate((0,0),-45)
        elif event.x >= 250 and event.x < 375:
            self.rotate((1,0),45)
        elif event.x >= 375:
            self.rotate((1,0),-45)

if __name__ == "__main__":
    app = App()
    app.root.mainloop()

