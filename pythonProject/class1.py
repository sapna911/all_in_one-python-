a = int(input("enter the first  number"))
b = int(input("enter the second  number"))
c = int(input("enter the third  number"))
d = int(input("enter the fourth  number"))
e = int(input("enter the five  number"))
avg= (a + b + c + d + e) / 5
if avg >= 90:
    print("grade :A")
elif avg >= 80 and avg < 90:
    print("grade: B")
elif avg >= 70 and avg < 80:
    print("grade: C")
elif avg >= 60 and avg < 700:
    print("grade: D")

else:
    print("grade:F")
