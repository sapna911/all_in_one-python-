def fin():
    f = int(input("Enter the first number"))
    s = int(input("Enter the Second number"))
    n = int(input("Enter the no of terms"))

    print(f, " ", s, end="")
    i = 1
    while i <= n:
        t = f + s
        print(" ", t, " ", end="")
        f = s
        s = t
        i = i + 1
fin()







