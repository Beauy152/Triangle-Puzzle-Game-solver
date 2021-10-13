


#

def getBoard():
    return [
        'a','b','c','d','e','f','g'
    ]

#
def rec(i,b=None,depth=0):
    if b is None: b = getBoard()
    b.remove(i.lower())
    print(depth,i,b)
    depth += 1
    
    if depth == 2: return "max depth"

    for letter in b:
        print( rec(letter,b[:],depth) )



#main
b = ['A','B','C','D','E','F','G']

for letter in b:
    rec(letter)
