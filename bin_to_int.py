def binary_str_conversion(binary_str):
    # Convert binary string to integer
    integer_value = int(binary_str, 2)
    
    # Convert integer back to binary string
    converted_binary_str = format(integer_value, '0' + str(len(binary_str)) + 'b')
    
    return converted_binary_str

# Example binary string
binary_str = '001100000011000000110000001100000100001101010001111000000101100001011000001100000101010101001000010001101110000100000011111100000100100001100101011011000110110001101111001000000101011101101111011100100110110001100100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

# Convert binary string and print the result
converted_binary_str = binary_str_conversion(binary_str)

print("Original binary string:", binary_str)
print("Converted binary string:", converted_binary_str)

# Test
assert binary_str == converted_binary_str, "Test failed: the converted binary string does not match the original"

print("Test passed.")
