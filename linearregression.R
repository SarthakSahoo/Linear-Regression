# Simple Linear Regression

# Regression line plot
plot_regression_line<-function(X,Y,b){
  y_pred = b[1]+b[2]*X
  library(ggplot2)
  ggplot()+
    geom_point(aes(x=X, y=Y), colour='red')+
    geom_line(aes(x=X, y=y_pred), colour='green')+
    xlab('x')+ylab('y')
}

# Prediction Function
predictValue<-function(val,b){
  pred = b[1]+b[2]*val
  return(pred)
}

# Coefficient estimator function
estimate_coefficient<-function(x,y){
  x_size = length(x)
  mean_x = mean(x)
  mean_y = mean(y)
  
  ss_xy = sum(y*x - x_size*mean_y*mean_x)
  ss_xx = sum(x*x - x_size*mean_x*mean_x)
  
  coeff_b_1 = ss_xy/ss_xx
  coeff_b_0 = mean_y - coeff_b_1*mean_x
  
  
  return(c(coeff_b_0, coeff_b_1))
}

X = c(0,1,2,3,4,5,6,7,8,9)
Y = c(0,2,4,6,8,10,12,14,16,18)
b = estimate_coefficient(X,Y)
cat('Coefficient B0: ',b[1])
cat('Coefficient B1: ',b[2])

value = as.integer(readline(prompt = "Enter index to predict: "))
pred_value = predictValue(value, b)
cat('Predicted value: ',pred_value)

plot_regression_line(X, Y, b)
