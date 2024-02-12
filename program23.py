#Accept string, count vowels and consonants
myString = input('Enter the string: ')
vowels = 'aeiouAEIOU'
def vowcons(s):
    vowel = 0 
    consonants = 0
    for i in s:
        if i in vowels:
            vowel+=1
        elif i not in vowels:
            consonants+=1       
    print('The vowels count is:',vowel," ",'Consonants are: ',consonants)
    
vowcons(myString)