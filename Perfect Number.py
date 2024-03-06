def perfect_number(number):
    sum_divi=0
    for i in range(1,number):
        if number%i==0:
            sum_divi+=i 
        
    if sum_divi == number:
        return ('{} is a perfect number'.format(number))
    else:
        return ('{} is not a perfect'.format(number))


    
number = int(input())
print(perfect_number(number))