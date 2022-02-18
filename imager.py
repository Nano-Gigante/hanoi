from cmath import pi
import math
from PIL import Image
import video

pixels = None
class imager:

    def __init__(self,diskn,res=50) -> None:
        self.res = res # 1 unit in the framstruct image = res pixels
        self.frames = 0 #number of frames rendered (needed to make the video)

        # horizontal and vertical res
        self.hres = 14*res
        self.vres = res*(diskn+3)
        
        #disk number
        self.diskn = diskn
        
        #bitmap shit
        self.img  = Image.new( 'RGB', (self.hres,self.vres), "cyan")  
        self.pixels = self.img.load()

        
    def save(self,filename):
        self.img.save(filename)

    def makevideo(self,fps):
        video.makevideo(self.frames,(self.hres,self.vres),fps)

    #shitty math
    def render(self,board):
        #creates new images
        self.img  = Image.new( 'RGB', (self.hres,self.vres), "cyan")  
        self.pixels = self.img.load()
        
        #draw base
        self.fillrect(0,self.vres-self.res,self.hres,self.res,(153,90,0))
        lhres = self.hres - 2 * self.res

        #draw sticks
        for i in range(3):
            self.fillrect( 
                self.res + lhres / 3 * (i + 0.5) - self.res / 4,self.res,
                self.res // 2, (self.diskn + 1) * self.res,
                (0,0,0)            
            )

        #draw disks
        for stick in range(3):
            for disk in range(len(board[stick])):
                n = board[stick][disk]
                
                posx = self.res + (lhres / 3 * stick) + (lhres / (6 * self.diskn) * (self.diskn - n)) 
                posy = (self.diskn - disk + 1) * self.res
                
                width = (lhres / 3) / self.diskn * n
                
                color = (255,0,0)
                lw = 4
                self.fillrect(posx,posy,width,self.res, self.rainbow(n / self.diskn))
                self.drawrect(posx,posy,width,self.res,4, (0,0,0) , True)

        #save before incrementing fram number because you will want a frame0 that represents the initial state
        self.save(f'frames/frame{self.frames}.png')
        
        self.frames += 1

    def getheight(self,board) -> int:
        cnt=0
        for i in board:
            for j in i:
                cnt+=1
    
        return cnt

    #BITMAP UTILITIES
    def fillrect(self,x,y,w,h,color):
        for ox in range(int(w)):
            for oy in range(int(h)):
                try:
                    self.pixels[x+ox,y+oy]= color
                except:
                    yolo : str

    def drawrect(self,x,y,w,h,lw,color,linecentered = False):
        if linecentered:
            self.drawrect(x-lw/2,y-lw/2,w+lw,h+lw,lw,color)
            return
        
        #top line
        self.fillrect(
            x,y,
            w,lw,color)
        #bottom line
        self.fillrect(
            x,y+h-lw,
            w,lw,color)
        #left
        self.fillrect(
            x,y,
            lw,h,color)
        #right
        self.fillrect(x+w-lw,y,lw,h,color) 

    def rainbow(self,seed : float):
        r = math.sin(2 * pi * seed) * 127 + 127
        g = math.sin(2 * pi * (seed + 1 / 3)) * 127 + 127
        b = math.sin(2 * pi * (seed + 2 / 3)) * 127 + 127
        return (int(r) , int(g) , int(b))
