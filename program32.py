sample_names = ['sally','Dylan','rebecca','Diana','Joanne','keith']
counter = list(filter(lambda el: el[0].isupper() and el[1:].islower(), sample_names))
print("Result:",end=' ')
print(len(''.join(counter)))