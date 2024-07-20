import os
print("1.press 1 to shutdown")
print("2.press 2 to restart")
print("3.press 3 to exit")
option=int(input("\n enter your option"))
if option>=1 and option<=2:
    if option==1:
        os.system("shutdown /s /t 1")


    else:
        os.system("shutdown /s /t 1")
else:
    exit()
