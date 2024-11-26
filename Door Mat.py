n,m = map(int,input("Enter n & m like(n,m) : ").split(","))
#print(n,m)
if (n>1 and n%2==1 and m==3*n):
    a = int((m - 3) / 2)
    b = 1
    round = int((n - 1) / 2)
    if n % 2 != 0 and m == (3 * n):
        for i in range(0, round):
            p = ""
            for j in range(0, a):
                p = p + "-"
            a = a - 3
            # print(p)

            q = ""
            for j in range(0, b):
                q = q + ".|."
            b = b + 2
            print(p + q + p)
        z = int((m - 7) / 2)
        r = ""
        for i in range(0, z):
            r = r + "-"
        print(r + "welcome" + r)

        a = a + 3
        b = b - 2
        for i in range(0, round):
            s = ""
            for j in range(0, a):
                s = s + "-"
            a = a + 3
            # print(s)

            t = ""
            for j in range(0, b):
                t = t + ".|."
            b = b - 2
            print(s + t + s)
else:
    print("n should be odd number as well as m should equal three time of n")
