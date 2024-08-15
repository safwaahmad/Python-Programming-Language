print("----------for condition--------")
for i in range(5):
    print(i)
print("--------------------------------")
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
print("------while condition---------")
#1.initilization 
#2.condition
#3.itration/incrament-decrement
total =4
i=1
while i>total:
 print("helo")
 i = i+1
 
 #1.   
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        
        
        
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number:",num)
        continue
    print("Found an odd number:",num)
