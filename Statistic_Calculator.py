import numpy as np
from scipy import stats
while True:
    print("Statistic calculator\n 1.Mean\n 2. Mode\n 3. Median\n 4. Variance\n 5. Standard deviation\n 6. Correlation matrix\n 7. Covariance\n 8. Percentile\n 9. Quartile\n 10. Sum\n 11. Minimum\n 12. Maximum\n 13. Product\n 14. End")
    cal= int(input("enter the number of the operation you want to carry out:"))
    
    if cal == 1:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        mean_value= np.mean(number)
        print("the mean value is", mean_value)
    elif cal == 2:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        mode_value=  stats.mode(number)
        print('the mode value is', mode_value)
    elif cal ==3:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        median_value= np.median(number)
        print('the median value', median_value)
    elif cal ==4:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        variance_value= np.var(number)
        print('the variance value', variance_value)
    elif cal ==5:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        standard_value= np.std(number)
        print('the standard deviation value', standard_value)
    elif cal ==6:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        correlation_value= np.corrcoef(number)
        print('the correlarion matrix value', correlation_value)
    elif cal ==7:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        covariance_value= np.cov(number)
        print('the covariance value', covariance_value)
    elif cal ==8:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        percentile_value= np.percentile(number, 25)
        print('the percentile value', percentile_value)
    elif cal ==9:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        fquartile_value= np.percentile(number, 25)
        squartile_value= np.percentile(number, 50)
        tquartile_value= np.percentile(number, 75)
        print('the first quartile value', fquartile_value)
        print('the second quartile value', squartile_value)
        print('the third quartile value', tquartile_value)
    elif cal == 10:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        sum_value= np.sum(number)
        print("the sum is", sum_value)
    elif cal == 11:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        min_value= np.min(number)
        print("the Minimum is", min_value)
    elif cal == 12:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        max_value= np.max(number)
        print("the Maximum is", max_value)
    elif cal == 13:
        user_input= input("enter the number and seperate with space:")
        number= np.array(list(map(int, user_input.split())))
        prod_value= np.prod(number)
        print("the product is", prod_value)
    elif cal == 14:
        print("Goodbye")
        break
    else:
        print("pick the correct number")