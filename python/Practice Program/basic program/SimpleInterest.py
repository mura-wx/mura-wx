def simple_interest(p,t,r):
    print('The principal is ', p)
    print('The time period is', p)
    print('The rate of interest is',r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si

simple_interest(8,10,3)