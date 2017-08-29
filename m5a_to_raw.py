#Importing libraries
import argparse
import sys
import os
import itertools
from multiprocessing import Pool
import time

#defining the functions used in script, might be useful to have these a objects?
def read_in_bytes(filename):
    with open(filename, 'rb') as f:
        while True:
            first = f.read()
            if first:
                for b in first:
                    b = bin(b)
                    yield b
            else:
                break

def isaninteger(number):
    if number != 0:
        print("number is not an integer")
        sys.exit()

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def writetofile(list,file):
    with open(str(file) + "_raw.bin", "ab") as myfile:
        for item in list:
            myfile.write(item)

def writeheader(m5amode,filename):
    mode = str(m5amode)
    numberofchannels = 0
    for i in range(8):
        if mode[i] == "f":
            numberofchannels += 2
        elif mode[i] == "F":
            numberofchannels += 2
        elif mode[i] == "3":
            numberofchannels += 1
        elif mode[i] == "0":
            numberofchannels += 0
        else:
            print("not a recognised Mark5B mode, please only use 2-bit Hex codes (f or F), 3, and 0")
            sys.exit()

    with open(str(filename) + "_header.txt", "w") as myfile:
        myfile.write(mode + "\n")
        myfile.write("NCHAN " + str(numberofchannels))


#Can use this def by it's self or run the entire .py
@profile
def tobits(file):

    print("reading in: " + str(file))

    m5a = read_in_bytes(file)

    m5a_bytes_size = getSize(file)

    number_data_frames_float = m5a_bytes_size/10016
    number_data_frames_int = m5a_bytes_size//10016
    number_data_frames = number_data_frames_float-number_data_frames_int

    isaninteger(number_data_frames)

    print("number of data frames in " + str(file) + " = " + str(number_data_frames_int))

    progress=1

    for df in range(number_data_frames_int):
        progress2=int(100*(df/number_data_frames_int))
        if progress2 == progress:
            print("\r"+str(file) + "\tprogress:" + str(progress2) + "%" +"\t["+"-"*progress2 + " "*int(100-progress2) + "]",)
            progress +=1
        twobitlist = []
        for i in range(16):
            b = next(m5a)
        for z in range(10000):
            b = next(m5a)
            for y in range(1,5):
                bitstring = b[(2*y):(2*(y+1))]

                # binary output DOM format
                if len(bitstring) == 1:
                    bitstring = bytes([int("10",2)])
                if bitstring in ('00', ''):
                    bitstring = bytes([int("00", 2)])
                if bitstring == '10':
                    bitstring = bytes([int("10", 2)])
                if bitstring == '11':
                    bitstring = bytes([int("11", 2)])
                if bitstring == '01':
                    bitstring = bytes([int("01", 2)])

                twobitlist.append(bitstring)
        #print(len(twobitlist))

        writetofile(twobitlist,file)

#setting up command line arguments and multiprocessing
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Filename')
    parser.add_argument('m5afiles', metavar='m5a', type=str, nargs='+',
                        help='a list of m5a files to be mapped', default="*.m5a")
    parser.add_argument('-f', help="Specify the .m5a file format, e.g. FFFFFFFF")
args = parser.parse_args()

t1=time.time()
p=Pool()
p.map(tobits,args.m5afiles)
p.close()
pooltime=time.time()-t1

#using 2 (the same) m5a files
#Pool done in : 252.15410208702087 s
#Serial done in : 390.0539782047272 s

# t2 = time.time()
# for i in args.m5afiles:
#     #writeheader(args.f, i)
#     tobits(i)
# serialtime=time.time()-t2

print("processing done in : " + str(pooltime))
#print("Serial done in : " + str(serialtime))
