from vec3 import Vec3
import random

class Viewport:
    def __init__(self, aspect_ratio=1.7778, image_width=400, viewport_height=2, depth=1): # how is viewport_height 2
        self.aspect_ratio = aspect_ratio
        self.image_width = image_width
        self.image_height = max(int(self.image_width / self.aspect_ratio), 1)
        self.viewport_height = viewport_height
        self.viewport_width = self.viewport_height * float(self.image_width) / self.image_height

        self.horSpace = self.viewport_width/self.image_width
        self.verSpace = self.viewport_height/self.image_height
        self.horDir = Vec3(1, 0, 0)
        self.verDir = Vec3(0, 1, 0)
        self.depth = depth

    def getImageHeight(self):
        return self.image_height
    def getImageWidth(self):
        return self.image_width

    def getPixelLoc(self, col, row):
        """Get the pixel  coordinate using viewport_u and viewport_v."""
        topY = self.image_height/2 * self.verDir * self.verSpace
        x = self.horDir * (self.horSpace * (col-self.image_width/2)) # so that the camera is in the middle of the viewport
        y = topY - (self.verDir * (self.verSpace * row))
        # all according to the scetch in the pdf

        xSample, ySample = self.sample_square(x,y)

        return xSample + ySample + Vec3(0,0,self.depth)
        # return x =  + Vu * (deltaU * col)
        # return y =  + Vv * (deltav * row)

    def sample_square(self, x, y):
        rndY = random.random()-0.5
        rndX = random.random()-0.5
        xSample = x + self.horDir*rndX*self.horSpace
        ySample = y + self.verDir*rndY*self.verSpace
        return xSample, ySample

    def getMiddle(self):
        x = self.horDir * (self.horSpace * self.image_width/2)
        y = self.verDir * (self.verSpace * self.image_height/2)
        return x + y