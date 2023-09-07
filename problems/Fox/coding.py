#take input string in = 'abcgh'


def check_sequence(A):

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    if alpha.__contains__(A.lower()):
          return "sequence is retained"
    return "sequence is not reatained"

print(check_sequence('ABDE'))


A = { 'assets':[
    {
    'name' : 'B',
    'time': 10.00, 
    'rating': 5
},{
  'name' : 'ABC',
    'time': 10.00, 
    'rating': 5
}, {
    'name' : 'AA',
    'time': 10.00, 
    'rating': 5
}]}

b = list()
for idx in A['assets']:
    b.append((idx['name'], idx))
print(sorted(b))

