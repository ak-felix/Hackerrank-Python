def print_formatted(number):
    # your code goes here
    width=len(bin(n))-2
    for i in range(1,n+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width)        
        
   
