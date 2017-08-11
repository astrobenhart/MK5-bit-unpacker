def first_2500(filename):
    with open(filename, 'rb') as f:
        while True:
            first = f.read()
            if first:
                for b in first:
                    b = bin(b).strip('0b')
                    yield b
            else:
                break

w,h=4,10016
Matrix = [[0 for x in range(w)] for y in range(h)]

a = first_2500("data/onesec_ww_onesec.m5a")

y=1
while y <= 16:
   b = next(a)
   y=y+1

for x in range(0,10016):
    b = next(a)
    for y in range(0, 4):
        Matrix[x][y] = b[(2*y):(2*(y+1))]
        #DOM
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

        #Offset Binary
        # if len(Matrix[x][y])==1:
        #     Matrix[x][y] = '1'
        # if Matrix[x][y] in ('00',''):
        #     Matrix[x][y] = '-3'
        # if Matrix[x][y]=='10':
        #     Matrix[x][y]='1'
        # if Matrix[x][y] == '11':
        #     Matrix[x][y] = '3'
        # if Matrix[x][y] == '01':
        #     Matrix[x][y] = '-1'

        #Twos Compliment
        if len(Matrix[x][y])==1: #i.e 10 -> 1 if followed by 00
            Matrix[x][y] = '-3'
        if Matrix[x][y] in ('00',''):
            Matrix[x][y] = '1'
        if Matrix[x][y]=='10':
            Matrix[x][y]='-3'
        if Matrix[x][y] == '11':
            Matrix[x][y] = '-1'
        if Matrix[x][y] == '01':
            Matrix[x][y] = '3'

        #Binary
        # if len(Matrix[x][y])==1:
        #     Matrix[x][y] = '10'
        # if Matrix[x][y] in ('00',''):
        #     Matrix[x][y] = '00'
        # if Matrix[x][y]=='10':
        #     Matrix[x][y]='10'
        # if Matrix[x][y] == '11':
        #     Matrix[x][y] = '11'
        # if Matrix[x][y] == '01':
        #     Matrix[x][y] = '01'

print(Matrix)

file = open('onesec_ww_onesec_2scomp.txt','w')
file.write("\n".join([" ".join([str(n) for n in item]) for item in Matrix]))
file.close()