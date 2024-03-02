class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"

    def pokaz_informacje(self):
        print(f"x: {self.x}, y: {self.y}, z: {self.z}")


# Utworzenie obiektu klasy Vector3D
moj_Vector3D = Vector3D(23.4, 10, 0)

# Drukowanie obiektu
print(moj_Vector3D)
moj_Vector3D.pokaz_informacje()