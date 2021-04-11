# Simple Linear Regression

# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt

# Co-Efficient estimation Function
def estimate_coefficent(x,y):
    x_size = np.size(x)
    
    mean_x, mean_y = np.mean(x), np.mean(y)
    
    SS_xy = np.sum(y*x - x_size*mean_y*mean_x)
    SS_xx = np.sum(x*x - x_size*mean_x*mean_x)
    
    coeff_b_1 = SS_xy / SS_xx
    coeff_b_0 = mean_y - coeff_b_1*mean_x

    return (coeff_b_0, coeff_b_1)
    
# Function to plot the regression Line
def plot_regressor_line(x, y, b):
    plt.scatter(x, y, color = "m", marker = "x", s = 20)
    y_pred = b[0] + b[1]*x
    print(y_pred)
    plt.plot(x, y_pred, color = 'g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Prediction Function which takes Value and predict by using our calculated coefficients    
def pred_value(val, b):
    ypred = b[0] + b[1]*val
    return ypred

if __name__ == "__main__":
    # Series of data point. This could be taken from csv file by reading and making a dataframe
    X = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([0,2,4,6,8,10,12,14,16,18])
    
    # Calculating the coefficients
    b = estimate_coefficent(X,y)
    
    # checking the coefficient values
    print('Co-efficient B0: ',b[0])
    print('Co-efficient B1: ',b[1])
    
    # Visualizing Regression Line with the data points 
    plot_regressor_line(X, y, b)
    
    # Predicting another data point entered by user
    value = int(input('Enter index to predict:'))
    pred_val = pred_value(value, b)
    print(pred_val)
