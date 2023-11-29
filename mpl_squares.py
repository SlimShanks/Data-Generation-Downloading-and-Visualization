import matplotlib.pyplot as plt
val = [1,2,3,4,5]
squares =[1,4,9,16,25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(val,squares, linewidth=3,c = 'red')
ax.set_xlabel("Values",fontsize = 14)
ax.set_ylabel("sq of value",fontsize = 14)
ax.tick_params(axis='both',labelsize = 14)
plt.show()

