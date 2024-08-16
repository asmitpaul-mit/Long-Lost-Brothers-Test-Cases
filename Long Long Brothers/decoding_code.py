# Sample code to decode the encoded string
# Use this example to read the encoded string from stdin decode it

import base64
import lzma

def decompress_matrix(string):
    decoded = base64.b64decode(string)
    matrix_str = lzma.decompress(decoded)

    matrix_str = matrix_str.decode('utf-8')

    return matrix_str
    
compressed = input("Enter the compressed string:")
decompressed = decompress_matrix(compressed)
print(decompressed)
