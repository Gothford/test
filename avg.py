def average(a = []):
    sm = 0
    count = 0
    
    for i in a:
        sm+=i
        count+=1
    return sm/count
    

print(average([1,2,3,4]))
