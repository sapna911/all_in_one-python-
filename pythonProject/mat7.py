import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
max_t=[42,36,46,50,28,17,29]
#plt.plot(days,max_t,color='red',marker="d",markersize='20')
plt.plot(days,max_t,color="red",label="max")
plt.plot(days,max_t,color="blue",label="min")

plt.xlabel('day')
plt.ylabel('temperature')
plt.title("weather info")
plt.legend(loc="upper right")
plt.show()
