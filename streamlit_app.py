import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import matplotlib.pyplot as plt
import numpy as np

L = 1
c = 1
mu = 1

N = 100				# number of intervals
x = np.linspace(0, L, N)
u = np.zeros(N)
u[0] = 1
u[N-1] = 0

nu = 0.005			# Courant number, nu = c*dt/dx
dx = L/N
dt = nu*dx/c 		# from Courant number, nu = cdt/dx
t_end = 500*dt


r = mu*dt/dx/dx		# Fourier number

# is stability condition, nu^2 <= 2r, satisfied?
print('stability condition, nu^2 = ', nu*nu, '<= 2r = ', 2*r)

for t in np.arange(0, t_end, dt):
	for i in range(1, N-2):
		u[i] = u[i]-nu/2*(u[i+1]-u[i-1])+r*(u[i+1]-2*u[i]+u[i-1])
	if t == 1*dt:
		plt.plot(x,u,label='dt')		
	if  t == 50*dt:
		plt.plot(x,u,label='50dt')		
	if  t == 400*dt:
		plt.plot(x,u,label='400dt')
		plt.xlabel("x")
		plt.ylabel("u")
		plt.legend()
		plt.title('LINEAR BURGERS EQ. BY FTCS METHOD')

		plt.show()
