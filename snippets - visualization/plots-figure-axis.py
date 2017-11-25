import matplotlib.pyplot as plt 
#a container that contains all plot elements
fig = plt.figures()

#Initializes subplot
fig.add_axes()
#A subplot is an axes on a grid system, rows-cols num
a = fig.add_subplot(222)
#adds subplot
fig, b = plt.subplots(nrows=3, ncols=2)
#creates subplot
ax = plt.subplots(2,2)

