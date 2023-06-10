#prime number check 
def prime_checker(number):
    for i in range (2, number - 1):
        if number % i == 0:
            print (number, "is not a prime number.")
            break
    else:
        print(number, "is a prime number.")
    
n = (2, 101)
prime_checker(number=n)
        
