prime = []
limit_number = int(input("enter a limit number :"))
for number in range(2, limit_number+1):
    status = True
    for i in range(2, number):
        if number % i == 0: status = False
    if status:
        prime.append(number)
    
print(prime)
