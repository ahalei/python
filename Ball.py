class Ball:
    def __init__(self, canvas, color, x, y):
        self.canvas = canvas
        self.color = color
        self.x = x
        self.y = y
        self.id = self.canvas.create_oval(self.x*20, self.y*20, (self.x+1)*20,(self.y+1)*20,fill=self.color)
    
        
    def draw(self):
        #self.canvas.move(self.id,-1,0)
        self.id = self.canvas.create_oval(self.x*20,self.y*20,(self.x+1)*20,(self.y+1)*20,fill=self.color)