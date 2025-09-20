def   computeAndPrint(x, y):
    val =  x**4/4.0 - x**3/3.0 - 3*x*x+y
    print("You called computeAndPrint("+ str(x)+","+ str(y)+")")
    return   val

print(computeAndPrint(6,5))