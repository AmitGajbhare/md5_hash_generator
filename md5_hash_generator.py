
import hashlib

# Get rnage from user

range_start = int(input("Enter the start number: "))
range_end = int(input("Enter the end number: "))

# the numbers range

for num in range(range_start, range_end):
    
    #convert the number to a string
    num_str = str(num)

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the number
    md5_hash.update(num_str.encode('utf-8'))

    # Get the hexadecimal representation of the hash

    hash_hex = md5_hash.hexdigest()

    print(f"The MD5 hash of {num} is: {hash_hex}")

