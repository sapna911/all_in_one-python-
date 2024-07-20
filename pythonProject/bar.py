import matplotlib.pyplot as plt
import numpy as np
company=['techsrijan','google','tcs','microsoft']
revenue=[500,10000,2000,1500]
profit=[200,8000,1500,900]
xpos=np.arange(len(company))
print(xpos)
plt.bar(xpos-0.2,revenue,label="revenue",color="red",width=0.4)
plt.bar(xpos+0.2,profit,label="profit",color="green",width=0.4)
plt.xticks(xpos,company)
plt.ylabel("revenue in million")
plt.title("company profit loss")
plt.legend()
plt.show()