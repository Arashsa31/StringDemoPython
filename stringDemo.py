#This demonstrates a variety of string formats
from decimal import Decimal

print(f'{17.489:.2f}')
print(f'{17.489:.3f}')

#c prints character code
print(f'{65:c} {97:c}')

#demonstrates the use of Decimal
print(f'{Decimal("10000000000000000000000000.0"):.3f}')
print(f'{Decimal("10000000000000000000000000.0"):.3e}')

#aligning text to the left, center, middle
print(f'[{27:10d}]')
print(f'[{"hello":10}]')
print(f'[{"Amanda":>10}]\n[{"Amanda":^10}]\n[{"Amanda":<10}]')

#positive and negative numbers are aligned
print(f'{27:d}\n{27: d}\n{-27: d}')

#additional string formats
print('{:.2f}'.format(17.489))
print('{0} {0} {1}'.format('Happy', 'Birthday'))

#reference words
print('{last} {first}'.format(first='Amanda', last='Gray'))

#repeating symbols
symbol = '>'
symbol *= 5
print(symbol)

#additional example of repeating symbol
name = 'Pam'
name += ' Black'
bar = '*'
bar *= len(name)
print(f'{bar}\n{name}\n{bar}')

#stripping white spaces
sentence = '\t \n This is a test string. \t\t \n'
sentence.strip()
print(sentence)

#lstrip removes only leading whitespace
sentence = '\t \n This is a test string. \t\t \n'
sentence.lstrip()
print(sentence)

#rstrip removes only trailing whitespace
sentence = '\t \n This is a test string. \t\t \n'
sentence.rstrip()
print(sentence)

#word split
for word in 'to be or not to be that is the question'.split():
    if word.startswith('t'):
        print(word, end=' ')