from numpy import sign
from tkinter import *
import PIL
from PIL import Image, ImageTk
from random import choice
from time import sleep
import sys

class HButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground


class App:
    def __init__(self):
        self.colorscheme = {"bg":"#073642",
                            "fg":"#eee8d5",
                            "button":"#586e75",
                            "gamebg":"#268bd2"}
        
        f = frozenset

        self.root = Tk()
        self.root.config(bg=self.colorscheme["bg"])
        self.root.title("Puzzle")
        self.root.protocol("WM_DELETE_WINDOW", self.quitwin)
        
        self.title1 = Label(self.root, text="Clock Hand Puzzle", font=("ShureTechMono Nerd Font Mono",32), bg=self.colorscheme["bg"], fg=self.colorscheme["fg"])
        self.title2 = Label(self.root, text="By Oliver Gaskell", font=("ShureTechMono Nerd Font Mono",24), bg=self.colorscheme["bg"], fg=self.colorscheme["fg"])
        
        self.about        = Button(self.root, text="About",        command=self.aboutwin,        highlightbackground=self.colorscheme["button"], bg=self.colorscheme["bg"], fg=self.colorscheme["fg"], activebackground=self.colorscheme["fg"], activeforeground=self.colorscheme["bg"])
        self.instructions = Button(self.root, text="Instructions", command=self.instructionswin, highlightbackground=self.colorscheme["button"], bg=self.colorscheme["bg"], fg=self.colorscheme["fg"], activebackground=self.colorscheme["fg"], activeforeground=self.colorscheme["bg"])
        self.quit         = Button(self.root, text="Quit",         command=self.quitwin,         highlightbackground=self.colorscheme["button"], bg=self.colorscheme["bg"], fg=self.colorscheme["fg"], activebackground=self.colorscheme["fg"], activeforeground=self.colorscheme["bg"])

        self.c_width  = 750
        self.c_height = 500

        self.c = Canvas(self.root,
                        width=self.c_width,
                        height=self.c_height,
                        bg=self.colorscheme["gamebg"])

        self.title1.grid      (row=0,column=0,columnspan=4)
        self.title2.grid      (row=1,column=0,columnspan=4)
        self.about.grid       (row=2,column=0)
        self.instructions.grid(row=2,column=1,columnspan=2)
        self.quit.grid        (row=2,column=3)
        self.c.grid           (row=3,column=0,columnspan=4)
        
        self.c.create_rectangle(3,3,self.c_width-3,self.c_height-3,outline="#000000",width=8)

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
    
    def aboutwin(self):
        self.about_root = Tk()
        self.about_root.title("About")
        self.about_root.config(bg=self.colorscheme["bg"])
        
        self.about_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nVel orci porta non pulvinar neque laoreet suspendisse."
        
        self.about_title = Label(self.about_root, text="About", font=("ShureTechMono Nerd Font Mono", 24), bg=self.colorscheme["bg"], fg=self.colorscheme["fg"])
        self.about_text =  Label(self.about_root, text=self.about_content, font=("ShureTechMono Nerd Font Mono", 16), bg=self.colorscheme["bg"], fg=self.colorscheme["fg"])
        self.about_quit =  HButton(self.about_root, text="Close", font=("ShureTechMono Nerd Font Mono", 12), command=self.about_root.destroy, highlightbackground=self.colorscheme["button"], bg=self.colorscheme["bg"], fg=self.colorscheme["fg"], activebackground=self.colorscheme["fg"], activeforeground=self.colorscheme["bg"])
        
        self.about_title.pack()
        self.about_text.pack()
        self.about_quit.pack()
    
    def instructionswin(self):
        pass
    
    def quitwin(self):
        self.quit_root = Tk()
        self.quit_root.title("Quit")
        self.quit_root.config(bg=self.colorscheme["bg"])
        
        self.quit_title = Label(self.quit_root, text="Are you sure you\nwant to quit?", font=("ShureTechMono Nerd Font Mono", 12), bg=self.colorscheme["bg"], fg=self.colorscheme["fg"])
        self.quit_yes   = HButton(self.quit_root, text="Yes", command=sys.exit, highlightbackground=self.colorscheme["button"], bg=self.colorscheme["bg"], fg=self.colorscheme["fg"], activebackground=self.colorscheme["fg"], activeforeground=self.colorscheme["bg"])
        self.quit_no    = HButton(self.quit_root, text="No",  command=self.quit_root.destroy, highlightbackground=self.colorscheme["button"], bg=self.colorscheme["bg"], fg=self.colorscheme["fg"], activebackground=self.colorscheme["fg"], activeforeground=self.colorscheme["bg"])
        
        self.quit_title.grid(row=0,column=0,columnspan=2)
        self.quit_yes.grid  (row=1,column=0)
        self.quit_no.grid   (row=1,column=1)
    
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

