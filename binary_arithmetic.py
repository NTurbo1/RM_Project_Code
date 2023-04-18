def add_binaries(a, b):
    sum = bin(int(a, 2) + int(b, 2))
    return sum[2:]

def subtract_binaries(a, b):
    res = bin(int(a, 2) - int(b, 2))
    return res[2:]