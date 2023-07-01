
with open('range5.txt', 'r') as file:
    a = 0 
    b = 0 
    c = 0 
    d = 0
    
    for line in file:
        
        if line.strip() == 'a':
            a = a + 1

        elif line.strip() == 'b':
            b = b + 1

        elif line.strip() == 'c':
            c = c + 1

        elif line.strip() == 'd':
            d = d + 1

print( str(a) + "\n" + str(b) + '\n' + str(c) + '\n' + str(d)   )

# notes to remember
# point 1
# first remember global and local variables local variables are lost after each iteration and the values
# fo back to zero hence why we used global variables here  (a,b,c,d)
# point 2
# we used line == 'a' which gives fales due to the fact that the value for line contain '\n' newlines
# hence the use of line.strip() it removes the new lines and makes our statement true.

