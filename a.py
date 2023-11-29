import matplotlib.pyplot as plt

sq = [1,4,9,16,25]
q = [1,2,3,4,5]

fig,ab = plt.subplots()
ab.scatter(q,sq,s=5)
plt.show()