import math
operator=input("Enter What is your Maths needs......")

if operator == "Calculator":
    num1 = int(input("First No..."))
    num2 = int(input("Second No..."))
    if operator == "+":
        result = num1 + num2
        print(result)
    elif operator == "-":
        result = num1 - num2
        print(result)
    elif operator== "*":
        result = num1 * num2
        print (result)
    elif operator== "/":
        result = num1 / num2
        print(result)   
elif operator =="area of a circle":
    radius = int(input("radius="))
    area = math.pi*pow(radius,2)
    print(f"The area of circle is {area}sq")
elif operator =="area of rectangle":
    length = int(input("Length"))
    breath = int(input("Breath"))
    area = length*breath
    print(f"The area of rectangle is {area}sq")
elif operator =="circumference of a circle":
    radius = int(input("radius="))
    circumference = 2 * math.pi*radius
    print(circumference)
elif operator =="hypotanius":
    a = int(input("Enter side A:"))
    b = int(input("Enter side A:"))
    c = math.sqrt(pow(a,2) + pow(b,2))
    print(f"The hypotanius is {c}m")
elif operator == "area of square":
    a = int(input("Enter the side a ..."))
    b = math.sqrt(pow(a,2))
    print(f"The area of square is {b}m")
elif operator == "area of triangle":
    l = float(input("Enter Length..:"))
    b = float(input("Enter breadth..:"))
    c=(l*b)/2
    print(f"The area of triangle is {c}m")
elif operator == "Temperature conversion":
    unit = input("is Temp. is in celsius or fahrenheit  (C/F)")
    temp = float(input("Enter Temperature"))

    if unit == "C":
        temp=(round(9*temp)/5+32,1)
        print(f"The temperature in fehrenheit is{temp}")
    elif temp == "F":
        temp=(round(temp-32)*5/9,1)
        print(f"The temperaure in celsius is {temp}")
    else :
        print("Invalid Unit")
        