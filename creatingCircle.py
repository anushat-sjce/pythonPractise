import matplotlib.pyplot as plt
%matplotlib inline

class Circle:
    
    def __init__(self,radius = 3, color='blue'):
        self.radius = radius
        self.color = color
        
        
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius
        
    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
        
        
RedCircle = Circle(3, 'red')
print(RedCircle.radius)
RedCircle.add_radius(5)
print(RedCircle.radius)
#RedCircle2 = Circle(5, 'red')
BlueCircle = Circle(2, 'Blue')

#dir(RedCircle)
#RedCircle.radius
#RedCircle.color 

RedCircle.draw_circle()
#RedCircle2.draw_circle()
