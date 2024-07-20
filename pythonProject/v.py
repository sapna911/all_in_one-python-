import matplotlib.pyplot as plt
party=['congress','bjp','sp','bsp','other']
votes=[400,1000,300,180,55]
plt.axis("equal")
plt.pie(votes,labels=party,radius=1.5,explode=[0,0.1,0,0,.1],autopct='80.2f88',startangle=180)
plt.show()