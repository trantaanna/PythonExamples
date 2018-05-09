def myfunc(*args):
    #example of using List comprehension and *args
    return [x for x in args if x%2==0]

    
if __name__ == '__main__':
    #return [6,8]
    myfunc(5,6,7,8)
  
    
    
