# radius = int(input("Enter the radius of the circle: ")) #but tumi chaile eikhane floating nite paro
radius = float(input("Enter the radius of the circle"))
pi = 3.1416
Area = pi * (radius * radius) # ar eitar poriborte (r ** 2) means r^2

print("The area of the circle is : ", Area) # abar eikhaneo round figuire use korte paro.like

# first method of using round figuire
print("The area of the circle is : ", round(Area, 2))

# and the second method is by using f string
print(f"The area of the circle is : {Area:.2f}") # tahole . point er pore only 2 digit ashbe
