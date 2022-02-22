
def raise_to_power(base_num, pow_num): 
    result=1
    for index in range(pow_num):     #index in range znamena kolikrat se to bude opakovat, bude se to opakovat pow number krat
        result= result*base_num
    return result

 
print(raise_to_power(3, 3))