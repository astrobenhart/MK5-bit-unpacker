def first_2500(filename):
    with open(filename, 'rb') as f:
        while True:
            first = f.read()
            if first:
                for b in first:
                    #b = bin(b).strip('0b')
                    b=b
                    yield b
            else:
                break


w,h=4,10000
Matrix = [[0 for x in range(w)] for y in range(h)]

a = first_2500("data/onesec_ww_onesec.m5a")

for i in range(16):
    b = next(a)

for x in range(0,10000):
    b = next(a)
    for y in range(0, 4):
        Matrix[x][y] = b[(2*y):(2*(y+1))]
        # if len(Matrix[x][y])==1:
        #     Matrix[x][y] = '1'
        # if Matrix[x][y] in ('00',''):
        #     Matrix[x][y] = '-1'
        # if Matrix[x][y]=='10':
        #     Matrix[x][y]='1'
        # if Matrix[x][y] == '11':
        #     Matrix[x][y] = '3'
        # if Matrix[x][y] == '01':
        #     Matrix[x][y] = '-3'

        #binary output DOM format
        if len(Matrix[x][y])==1:
            Matrix[x][y] = '10'
        if Matrix[x][y] in ('00',''):
            Matrix[x][y] = '00'
        if Matrix[x][y]=='10':
            Matrix[x][y]='10'
        if Matrix[x][y] == '11':
            Matrix[x][y] = '11'
        if Matrix[x][y] == '01':
            Matrix[x][y] = '01'

twobitlist = []

for x in range(0,10000):
    for y in range(0, 4):
        twobitlist.append(Matrix[x][y])

eightbitlist = []

for x in twobitlist:
    eightbitlist.append("000000"+str(x))

# print(Matrix)
# print(twobitlist)
# print(eightbitlist)

with open("eightbitlist.txt", 'w') as output:
    for x in eightbitlist:
        output.write(str(x)+"\n")

