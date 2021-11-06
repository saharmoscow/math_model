print('Введите количество тел')
n = int(input()) #количество тел

print('Введите скорости сначала по оси х затем по оси у')
vx = int(input()) #скорость по х
vy = int(input()) #скорость по у

print('Введите координаты сначала по оси х затем по оси у')
x = int(input()) 
y = int(input()) 

print('Введите массу')
m = int(input()) #масса

ax = [-1] * n
ay = [-1] * n

fx = [-1] * n
fy = [-1] * n

dt = 0.01 #время



while True:
    for i in range(0, n):
        fx[i] = 10
        ax[i] = fx[i] / m[i]
        vx[i] + ax[i] * dt
        x[i] = x[i] + vx[i] * dt

        fy[i] = 10
        ay[i] = fy[i] / m[i]
        vy[i] = vy[i] + ay[i] * dt
        y[i] = y[i] + vy[i] * dt
