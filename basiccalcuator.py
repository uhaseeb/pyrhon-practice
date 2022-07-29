while(True):
    num1 = int(input("Enter the First Number:"))
    num2 = int(input("Enter the Second Number"))
    operator = input("Enter the operator:")

    def add(num1,num2):
        sum=num1 + num2
        print("The Sum is" + str(sum))

    def subtract(num1,num2):
        diff=num1 - num2
        print("The Diff is:" + str(diff))

    def multiply(num1,num2):
        product=num1 * num2
        print("The Product is:" + str(product))
    def division(num1,num2):
        divide=num1/num2
        print("The division gives:" + str(divide))

    if operator=="+":
        add(num1,num2)

    elif operator=="-":
        subtract(num1,num2)

    elif operator=="*":
        multiply(num1,num2)

    elif operator=="/":
        division(num1,num2)