def fire(theta, sum):
    if sum >= theta:
        return 1
    else:
        return 0

def fireNot(theta, sum):
    if sum == theta:
        return 1
    else:
        return 0

inp = [[1,1,1], [0,0,0], [1,1,0], [0,0,1]]

# AND
for i in inp:
    sum = 0
    for j in i:
        sum+=j
    print("AND (",i,")=", fire(len(i), sum))

# OR
for i in inp:
    sum = 0
    for j in i:
        sum+=j
    print("OR (",i,")=", fire(1, sum))

# NOT
inp = [1, 0]
for i in inp:
    print("NOT(",i,")=", fireNot(0, i))
    
'''
OUTPUT :-
AND ( [1, 1, 1] )= 1
AND ( [0, 0, 0] )= 0
AND ( [1, 1, 0] )= 0
AND ( [0, 0, 1] )= 0
OR ( [1, 1, 1] )= 1
OR ( [0, 0, 0] )= 0
OR ( [1, 1, 0] )= 1
OR ( [0, 0, 1] )= 1
NOT( 1 )= 0
NOT( 0 )= 1
'''