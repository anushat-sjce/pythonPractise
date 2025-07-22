import matplotlib.pyplot as plt
%matplotlib inline 

class Rectangle:

    def __init__(self, width = 2, height = 4, color = 'r'):
        self.width = width
        self.height = height
        self.color = color

    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()

    def addMeasurements(self, width, height, color):
        self.width = self.width + width
        self.height = self.height + height
        self.color = color

#greenRectangle = Rectangle(2,2,'Green')
greenRectangle.drawRectangle()

greenRectangle2 = Rectangle(1,1,'Blue')
greenRectangle2.addMeasurements(1,1,'Orange')
greenRectangle2.drawRectangle()
