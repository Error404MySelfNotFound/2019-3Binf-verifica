class Locker:
    def __init__(self, position,width,height,depth,material,private_key):
        self.position = position
        self.width = width
        self.height = height
        self.depth = depth
        self.material = material
        self.private_key = private_key
        self.is_bulky = (self.width * self.height * self.depth) > 2000000
        self.is_bulky = (160 * 180 * 50) > 2000000
        self.is_bulky = (self.width * self.height * self.depth) > 2000000
        
    
  
    
