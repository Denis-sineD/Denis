'''
a = list(map(int, input().split()))
if a == []:
    print()
else:
    minium = a[0]
    for i in range(0, len(a)):
        if a[i] < minium:
            minium = a[i]
    print(minium)
'''
def minium(a):
    m = 0
    for i in range(0, len(a)):
        if a[i] < m:
            m = a[i]
    return m

def minimum2(a):
    m = None
    f = True # m не был инициализирован
    for b in a:
        if f or b < m:
            f = False
            m = b
    return m



c = list(map(int, input().split()))
print(minium(c))
