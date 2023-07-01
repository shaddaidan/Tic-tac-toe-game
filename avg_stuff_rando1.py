a = 0 ; b = 0 ; c = 0 ; d = 0
with open('range5.txt', 'r') as file:
    
    for line in file:
        
        if line == 'a':
            a = a + 1

        elif line == 'b':
            b = b + 1

        elif line == 'c':
            c = c + 1

        elif line == 'd':
            d = d + 1

print( str(a) + "\n" + str(b) + '\n' + str(c) + '\n' + str(d)   )
