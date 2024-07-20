import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
max_t=[42,36,46,50,28,17,29]
plt.plot(days,max_t,"r+--")
plt.xlabel('day')
plt.ylabel('temperature')
plt.title("weather info")
plt.show()