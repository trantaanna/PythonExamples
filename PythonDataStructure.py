def pair_sum():
    array = [1,2,3,2]
    k = 4
    result = []
    for i in array:
        print(f'outer{i}')
        for x in array:
            print(f'inner {x}')
            if i + x == k:
                print(f'-----i:{i} x:{x}')
                result.append((i,x))
                
    print(result)
    newresult = set(result)
    print(newresult)
    

def compress(array):
    out=""
    d={}
    for w in array:
        print(w)
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    for key, value in d.items():
        print(key)
        print(value)
        out=out+key+str(value)
        
    print(out)

def sum_f(n):
    if len(n)==1 : return int(n)
    else: return int(n[0]) + int(sum_f(n[1:]))
    
def reverse(s):
    
    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return s[-1]+reverse(s[:-1])  
    
if __name__ == "__main__":
    pair_sum()
    compress('AAAAABBBBCCCC') #A5B4C4
    sum_f('4502') #11
    reverse('hello world') #'dlrow olleh'
