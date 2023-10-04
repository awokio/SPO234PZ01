import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    :param x: np.array(np.float) вектор длины 2
    :return: np.float
    """
    return np.sum(np.cos(x)**2 - np.sin(x)/3)


def grad_f(x):
    """
    Градиент функциии f, определенной выше.
    :param x: np.array[2]: float вектор длины 2
    :return: np.array[2]: float вектор длины 2
    """
    return ((-8/3) * np.sin(x) * np.cos(x))



def grad_descent_2d(f, grad_f, lr, num_iter=100, x0=None):
    """
    функция, которая реализует градиентный спуск в минимум для функции f от двух переменных.
        :param f: скалярная функция двух переменных
        :param grad_f: градиент функции f (вектор размерности 2)
        :param lr: learning rate алгоритма
        :param num_iter: количество итераций градиентного спуска
        :return: np.array[num_iter, 2] пар вида (x, f(x))
    """
    if x0 is None:
        x0 = np.random.random(2)

    # будем сохранять значения аргументов и значений функции
    # в процессе град. спуска в переменную history
    history = []

    # итерация цикла -- шаг градиентнго спуска
    curr_x = x0.copy()
    for iter_num in range(num_iter):
        entry = np.hstack((curr_x, f(curr_x)))
        history.append(entry)

        curr_x -= lr * grad_f(curr_x)

    return np.vstack(history)



steps = grad_descent_2d(f, grad_f, lr=0.1, num_iter=20)
steps
array = ([[4.88425603e-01, 8.70891284e-01, 8.05259722e-01],
       [4.05551673e-01, 7.72349540e-01, 6.42603421e-01],
       [3.33046924e-01, 6.72383592e-01, 4.94824604e-01],
       [2.71254971e-01, 5.74927194e-01, 3.67482062e-01],
       [2.19626254e-01, 4.83656749e-01, 2.63708328e-01],
       [1.77099949e-01, 4.01320343e-01, 1.83632866e-01],
       [1.42415945e-01, 3.29401006e-01, 1.24782462e-01],
       [1.14316333e-01, 2.68184005e-01, 8.32262182e-02],
       [9.16517345e-02, 2.17082263e-01, 5.47656449e-02],
       [7.34238658e-02, 1.75017004e-01, 3.57008577e-02],
       [5.87918134e-02, 1.40724029e-01, 2.31253707e-02],
       [4.70605270e-02, 1.12949327e-01, 1.49164496e-02],
       [3.76623121e-02, 9.05510992e-02, 9.59489465e-03],
       [3.01369706e-02, 7.25397136e-02, 6.16074901e-03],
       [2.41132253e-02, 5.80826113e-02, 3.95113269e-03],
       [1.92924495e-02, 4.64921977e-02, 2.53211993e-03],
       [1.54349169e-02, 3.72071516e-02, 1.62195116e-03],
       [1.23484238e-02, 2.97725872e-02, 1.03862089e-03],
       [9.87899009e-03, 2.38215879e-02, 6.64951986e-04],
       [7.90332062e-03, 1.90590725e-02, 4.25665439e-04]])


# %matplotlib osx
from matplotlib import cm
path = []
X, Y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(projection = '3d')
zs = np.array([f(np.array([x,y]))
              for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, zorder=2)
ax.plot(xs=steps[:, 0], ys=steps[:, 1], zs=steps[:, 2],
        marker='.', markersize=20, zorder=3,
        markerfacecolor='y', lw=3, c='black')
ax.set_zlim(0, 5)
ax.view_init(elev=60)
plt.show()


plt.figure(figsize=(14,7))
plt.xlabel('grad descent step number')
plt.ylabel('$f(x)$')
plt.title('Значение функции на каждом шаге градиентного спуска.')

f_values = list(map(lambda x: x[2], steps))
plt.plot(f_values, label='gradient descent result')
plt.legend()
plt.show()














