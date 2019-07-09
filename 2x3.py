from numpy import sign
from tkinter import *
import PIL
from PIL import Image, ImageTk
from random import choice
from time import sleep

class App:
    def __init__(self):
        f = frozenset

        self.root = Tk()

        self.c_width  = 750
        self.c_height = 500

        self.c = Canvas(self.root,
                        width=self.c_width,
                        height=self.c_height,
                        bg="#0000ff")

        self.c.grid(row=0,column=0,columnspan=4)

        self.imgs = {}
        self.pimgs = {}
        self.cimgs = {}
        self.angles = {}
        self.coords = {(0,0):[1*(self.c_width/6),1*(self.c_height/4)],
                       (1,0):[3*(self.c_width/6),1*(self.c_height/4)],
                       (2,0):[5*(self.c_width/6),1*(self.c_height/4)],
                       (0,1):[1*(self.c_width/6),3*(self.c_height/4)],
                       (1,1):[3*(self.c_width/6),3*(self.c_height/4)],
                       (2,1):[5*(self.c_width/6),3*(self.c_height/4)]}

        link_weights = [-2,-1,0,1,2]
        self.links = {f(( (0,0) , (1,0) )): choice(link_weights),
                      f(( (0,0) , (0,1) )): choice(link_weights),
                      f(( (0,1) , (1,1) )): choice(link_weights),
                      f(( (1,0) , (1,1) )): choice(link_weights),
                      f(( (1,0) , (2,0) )): choice(link_weights),
                      f(( (1,1) , (2,1) )): choice(link_weights),
                      f(( (2,0) , (2,1) )): choice(link_weights)}

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

        self.imgs[(0,1)] = self.oimg
        self.angles[(0,1)] = 0
        self.pimgs[(0,1)] = ImageTk.PhotoImage(self.imgs[(0,1)])
        self.cimgs[(0,1)] = self.c.create_image(self.coords[(0,1)][0],
                                                self.coords[(0,1)][1],
                                                anchor=CENTER,
                                                image=self.pimgs[(0,1)])

        self.imgs[(1,1)] = self.oimg
        self.angles[(1,1)] = 0
        self.pimgs[(1,1)] = ImageTk.PhotoImage(self.imgs[(1,1)])
        self.cimgs[(1,1)] = self.c.create_image(self.coords[(1,1)][0],
                                                self.coords[(1,1)][1],
                                                anchor=CENTER,
                                                image=self.pimgs[(1,1)])
        
        self.imgs[(2,0)] = self.oimg
        self.angles[(2,0)] = 0
        self.pimgs[(2,0)] = ImageTk.PhotoImage(self.imgs[(2,0)])
        self.cimgs[(2,0)] = self.c.create_image(self.coords[(2,0)][0],
                                                self.coords[(2,0)][1],
                                                anchor=CENTER,
                                                image=self.pimgs[(2,0)])
        self.imgs[(2,1)] = self.oimg
        self.angles[(2,1)] = 0
        self.pimgs[(2,1)] = ImageTk.PhotoImage(self.imgs[(2,1)])
        self.cimgs[(2,1)] = self.c.create_image(self.coords[(2,1)][0],
                                                self.coords[(2,1)][1],
                                                anchor=CENTER,
                                                image=self.pimgs[(2,1)])

        self.c.bind("<Button-1>", self.click)
    
    def rotate(self,coord,_angle):
        if (self.angles[coord] % 45 == 0) and (_angle != 0):
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
        f = frozenset
        if event.y < 250:
            if event.x < 125:                      # 0,0 left
                self.rotate((0,0),45)
                self.rotate((0,1),45*self.links[f(((0,0),(0,1)))])
                self.rotate((1,0),45*self.links[f(((0,0),(1,0)))])
            elif event.x >= 125 and event.x < 250: # 0,0 right
                self.rotate((0,0),-45)
                self.rotate((0,1),-45*self.links[f(((0,0),(0,1)))])
                self.rotate((1,0),-45*self.links[f(((0,0),(1,0)))])
            elif event.x >= 250 and event.x < 375: # 1,0 left
                self.rotate((1,0),45)
                self.rotate((1,1),45*self.links[f(((1,0),(1,1)))])
                self.rotate((2,0),45*self.links[f(((1,0),(2,0)))])
            elif event.x >= 375 and event.x < 500: # 1,0 right
                self.rotate((1,0),-45)
                self.rotate((1,1),-45*self.links[f(((1,0),(1,1)))])
                self.rotate((2,0),-45*self.links[f(((1,0),(2,0)))])
            elif event.x >= 500 and event.x < 625: # 2,0 left
                self.rotate((2,0),45)
                self.rotate((2,1),45*self.links[f(((2,0),(2,1)))])
            elif event.x >= 625:                   # 2,0 right
                self.rotate((2,0),-45)
                self.rotate((2,1),-45*self.links[f(((2,0),(2,1)))])
        if event.y >= 250:
            if event.x < 125:                      # 0,1 left
                self.rotate((0,1),45)
                self.rotate((1,1),45*self.links[f(((0,1),(1,1)))])
            elif event.x >= 125 and event.x < 250: # 0,1 right
                self.rotate((0,1),-45)
                self.rotate((1,1),-45*self.links[f(((0,1),(1,1)))])
            elif event.x >= 250 and event.x < 375: # 1,1 left
                self.rotate((1,1),45)
                self.rotate((2,1),45*self.links[f(((1,1),(2,1)))])
            elif event.x >= 375 and event.x < 500: # 1,1 right
                self.rotate((1,1),-45)
                self.rotate((2,1),-45*self.links[f(((1,1),(2,1)))])
            elif event.x >= 500 and event.x < 625: # 2,1 left
                self.rotate((2,1),45)
            elif event.x >= 625:                   # 2,1 right
                self.rotate((2,1),-45)

if __name__ == "__main__":
    app = App()
    app.root.mainloop()

