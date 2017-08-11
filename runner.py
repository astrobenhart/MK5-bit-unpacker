w,h=4,(10015-16)
Matrix = [[0 for x in range(w)] for y in range(h)]

a = first_2500("data/onesec_ww_onesec.m5a")

for x in range(0,(10015-16)):
    b = next(a)
    for y in range(0, 4):
        Matrix[x][y] = b[(2*y):(2*(y+1))]
        if len(Matrix[x][y])==1:
            Matrix[x][y] = '2'
        if Matrix[x][y] in ('00',''):
            Matrix[x][y] = '0'
        if Matrix[x][y]=='10':
            Matrix[x][y]='2'
        if Matrix[x][y] == '11':
            Matrix[x][y] = '3'
        if Matrix[x][y] == '01':
            Matrix[x][y] = '1'

print(Matrix)