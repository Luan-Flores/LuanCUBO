from matplotlib import pyplot as plt

x_dias=[1,5,10,15,20,25,30]
y_temp_max=[28,27,29,30,32,26,24]
y_temp_min=[18,17,19,22,24,20,13]

plt.plot(x_dias,y_temp_max)
plt.plot(x_dias,y_temp_min)

plt.title('Temperatura do mês')
plt.xlabel('Temperaturas')
plt.ylabel('Dias')
plt.legend(['Temp máx','Temp min'])
plt.grid(True)

plt.show() 