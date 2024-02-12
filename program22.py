#distinct elements of two lists
samplelist = [1,2,3,3,3,3,4,5]

def uniquelist(x):
    x = list(set(x))
    print(x)
    
uniquelist(samplelist)