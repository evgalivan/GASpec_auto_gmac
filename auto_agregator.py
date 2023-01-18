from pathlib import Path
from time import sleep

sign = 'Заголовок'
sign2 = '\t'
len_sign = len(sign)
#print(len_sign)
p = Path.cwd()

list_text_file = list(Path.cwd().glob('0*.txt'))

file = open('MyFile.txt', 'w')

for text_file in list_text_file:
    with text_file.open() as f:
        list_readlines = f.readlines()
        print(list_readlines[0], list_readlines[1], list_readlines[2], list_readlines[3], end='')
        for line in list_readlines:
            if sign in line:                
                line = line.split(' ')[1]
                file.write(line + '\t')
                print(line, end='\t')
            if sign2 in line:
                line = line.split(sign2)[1]
                line = line.split(' ')[0]
                line = line.replace('.', ',')
                file.write(line + '\n')
                print(line + '\n')
file.close()