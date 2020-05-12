# matplotlib module / pip install matplotlib
import matplotlib.pyplot as plt

percent = [75, 22, 3]
colour = ['#36bfc9', '#f0b43c', '#fa6956']
label =['Nitrogen', 'Oxygen', 'Co2']

plt.pie(percent, labels=label, colors=colour)
plt.show()