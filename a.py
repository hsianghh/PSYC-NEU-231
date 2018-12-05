def sort_list(x):
    y=[]
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