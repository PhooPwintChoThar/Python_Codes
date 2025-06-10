import turtle
command=input("turtle|>  ")
command=command.lower()
while command!="quit":
    if command=="fd":
        argument=int(input("argument : "))
        turtle.forward(argument)
        command=input("turtle|>  ")
        command=command.lower()
    elif command=="back":
        argument=int(input("argument : "))
        turtle.backward(argument)
        command=input("turtle|>  ")
        command=command.lower()
    elif command=="lf":
        argument=int(input("argument(degree) : "))
        turtle.left(argument)
        command=input("turtle|>  ")
        command=command.lower()
    elif command=="rt":
        argument=int(input("argument(degree) : "))
        turtle.right(argument)
        command=input("turtle|>  ")
        command=command.lower()
    elif command=="pu":
        turtle.penup()
        command=input("turtle|>  ")
        command=command.lower()
    elif command=="pd":
        turtle.pendown()
        command=input("turtle|>  ")
        command=command.lower()
    elif command=="reset":
        turtle.reset()
        command=input("turtle|>  ")
        command=command.lower()
    elif command=="quit":
        turtle.done()
    else:
        print("Invalid command")
        command=input("turtle|>  ")
        command=command.lower()
        continue