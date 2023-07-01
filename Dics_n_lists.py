picnic_items = { 'sam' : { 'salmon' : 2 , 'spaghetti' : 4 , 'soda' : 2},
                 'reg' : { 'sandwitch' : 3 , 'onions' : 6 , 'oranges' : 9} ,
                 'woody' : { 'yam' : 4 , 'chicken' : '7' , 'rice' : 9 }} 

# print(picnic_items)

# print(picnic_items['sam']['salmon'])

for k,v in picnic_items['sam'].items():
    print(k , v)


print(picnic_items['sam']['spaghetti'] ) 

print( 'sam is really cool' + "\n" + 'yeah he is')

stuff_shaddai_wants = {'macbook' : 1 , 'vans' : 1 , 'suit' : 2 ,
                       'jacket' : 3 , 'earphone' : 1 , }