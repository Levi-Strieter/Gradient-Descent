from numpy import *
import matplotlib.pyplot as plt
import pandas as pd 

def computer_error_for_given_points(b, m, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b))**2
    return totalError / float(len(poinnts))


def step_gradient(b_current, m_current, points, learning_rate):
    #gradient descent
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - (m_current * x) + b_current)
        m_gradient += -(2/N) * x * (y - (m_current * x) + b_current)
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b,  m = step_gradient(b, m, array(points), learning_rate)
        return [b,m]


def run():

    points = pd.read_csv('data.csv')

    x_axis = points['x']
    y_axis = points['y']

    #tuning knobs/how fast things can learn
    learning_rate = 0.0001
    #slope and y intercept/ start with 0 to learn values
    initial_b = 0
    initial_m = 0
    #small dataset so run small number of times
    num_iterations = 1000
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate,  num_iterations)
    print("Y intracept {}".format(b))
    print("Slope {}".format(m))
    
    x_line = [b, m]
    y_line = [0, b]

    plt.scatter(x_axis, y_axis)
    plt.plot(x_line, y_line)
    plt.show()
    

if __name__ == '__main__':
    run()
