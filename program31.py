texts = ['php','w3r','Python','abcd','Java','aaa']
def find_palindromes(y):
    palindromes = filter(lambda x: x.lower() == x.lower()[::-1], y)
    return list(palindromes)

palindromes = find_palindromes(texts)
print(palindromes)
