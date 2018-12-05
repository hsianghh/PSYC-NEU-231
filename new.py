
def sort_list(x):
    y=[]
    if (type(x[0]) is not int or type(x[1])) is not int:
        print('please enter two numbers') 
    elif type(x[0]) is int and type(x[1]) is int:   
        if x[0] < x[1]:
            return x
        elif x[0] > x[1]:
            y.append(x[1])
            y.append(x[0])
            return y
    
    
def product_list(x):
    y=1
    for i in x:
        y*=i
    return y