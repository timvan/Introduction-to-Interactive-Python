# Collatz Conjecture
# If number is odd: 3n + 1
# If number is even: n/2
# Will always converge to 1

def run(num):
    global num_list
    if num % 2 > 0:
        num_new = 1 + num * 3
    else:
        num_new = num / 2
    
    print num_new
    num = num_new
    num_list.append(num_new)
    return num


num = 23
num_list = [num]

while num != 1:
    num = run(num)
    
    
print "max:", max(num_list)
    
 