import matplotlib.pyplot as plt
rectangle = plt.Rectangle((1,1), 4, 4,fc='white',ec="black" )
plt.gca().add_patch(rectangle)
plt.axis('scaled')
plt.show()