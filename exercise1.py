number=int(input("Say a number!"))
if number<0:
    print("Come on give me something positive!")
else:
    odd = sum(range(1, number+1, 2))
    even = sum(range(2, number+1, 2))
    average= even/number
    print("Sum of odd numbers:", odd)
    print("Average of even numbers: {} / {} = {}".format(even,number,average))