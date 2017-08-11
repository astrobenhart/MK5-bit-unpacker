def simp_bytes(filename):
    with open(filename, 'rb') as f:
        while True:
            byte = f.read(2)[0:25]