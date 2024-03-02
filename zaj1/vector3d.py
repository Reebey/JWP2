class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self): 
        return self.x 

    def set_x(self, x): 
        self.x = x

    def get_y(self): 
        return self.y 

    def set_y(self, y): 
        self.y = y 
    
    def get_z(self): 
        return self.z 

    def set_z(self, z): 
        self.z = z 

    def norm():
        return self.x**2 + self.y**2 + self.z**2

    def __add__(self, v):
        return Vector3D(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vector3D(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, v):
        return Vector3D(self.x * v.x, self.y * v.y, self.z * v.z)

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def pokaz_informacje(self):
        print(f"x: {self.x}, y: {self.y}, z: {self.z}")



# Utworzenie obiektu klasy Vector3D
moj_Vector3D = Vector3D(23.4, 10, 0)

# Drukowanie obiektu
print(moj_Vector3D)
moj_Vector3D.pokaz_informacje()