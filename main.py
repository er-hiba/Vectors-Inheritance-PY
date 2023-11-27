from Vectors import Vector2D
from Vectors import Vector3D

# Creating objects of Vector2D and Vector3D classes
v1 = Vector2D()
v2 = Vector2D(-1, 0)
v3 = Vector3D()
v4 = Vector3D(1.5, 2, -2)

# Displaying coordinates of the vectors
print("Coordinates:")
print("Vector 2D 1:", v1.to_string())
print("Vector 2D 2:", v2.to_string())
print("Vector 3D 1:", v3.to_string())
print("Vector 3D 2:", v4.to_string())

# Testing for vectors with identical coordinates
print("\nChecking for vectors with matching coordinates:")
print("Vector 2D 1 and Vector 2D 2:", v1.equals(v2)) 
print("Vector 3D 1 and Vector 3D 2:", v3.equals(v4))

# Getting the norms of vectors
print("\nNorms of vectors:")
print("Norm of Vector 2D 1:", v1.norm())
print("Norm of Vector 3D 2:", v2.norm())

# Setting new values to vectors
v1.set_x(5)
v1.set_y(7)
v4.set_z(4)

# Displaying updated coordinates
print("\nUpdated vectors:")
print("Vector 2D 1:", v1.to_string())
print("Vector 3D 2:", v4.to_string())

# Displaying the total count of vectors created
print("\nTotal count of vectors created:", Vector2D.get_counter())
