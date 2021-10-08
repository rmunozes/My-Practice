import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1) #subplto(r, c, n) r=row, c=column, r=subplot number)
v0 = 5
g = 9.81
t = np.linspace(0, 1, 11)
y = v0*t - 0.5*g*t**2
plt.plot(t, y, '*')
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.title('ball moving vertically')

plt.subplot(2, 1, 2)
t = np.linspace(-2, 2, 100)
f_values = t**2
g_values = np.exp(t)
plt.plot(t, f_values, 'r', t, g_values, 'b--')
plt.xlabel('t')
plt.ylabel('f and g')
plt.legend(['t**2', 'e**t'])
plt.title('Plotting of two functions (t**2 and e**t)')
plt.grid('on')
plt.axis([-3, 3, 0, 10])

plt.tight_layout()
plt.savefig('my_plot4.pdf')

print('y is{long}\g_values is{gravity}'.format(long=y, gravity=g_values))

Grade_of_difficult = int(input('what do you think is grade of difficult of this program [0-5]?'))

if Grade_of_difficult > 2:
    print('ohh my god, with the value of {} you are more foolish than DONALD TRUMP '.format(Grade_of_difficult))
else:
    print('not bad for you ... Baby coder')
print(""".
.
.""")

plt.show()


