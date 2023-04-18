def fromBinaryToString(binary_string):
    binary_strings = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    bytes_array = bytearray(int(b, 2) for b in binary_strings)
    original_string = bytes_array.decode('utf-8')

    return original_string