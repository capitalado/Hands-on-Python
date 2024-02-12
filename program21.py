#Count lower and upper cases
sample_str = 'The quick Brown Fox'

def casecounter(s):
    countU = 0
    countL = 0
    for i in sample_str:
        if i.isupper():
            countU+=1
        elif i.islower():
            countL+=1
    print('The upper cases sum up to: ',countU,' and lower cases to: ',countL)
    
casecounter(sample_str)
            

        
