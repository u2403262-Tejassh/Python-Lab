while True :
    print("\n'1' Area of rectangle\n'2' Area of square\n'3' Area of triangle\n'4' Exit")
    choice = int(input("Enter choice: "))
    if choice==1:
        length = int(input("\nEnter length: "))
        breadth = int(input("Enter breadth: "))
        area = length*breadth
        print("\nArea =",area)
    elif choice==2:
        length = int(input("\nEnter length: "))
        area = length*length
        print("\nArea =",area)
    elif choice==3:
        breadth = int(input("\nEnter breadth: "))
        height = int(input("Enter height: "))
        area = 0.5*breadth*height
        print("\nArea =",area)
    elif choice==4:
        break
