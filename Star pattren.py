def peramid_pattren(number):
    for i in range(1,number+1):
        left_space=" "*(number-i)
        stars = '* '*i 
        print(left_space+stars)
    
    
number = int(input())
peramid_pattren(number)