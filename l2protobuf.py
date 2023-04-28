#!/bin/python3

import person_pb2
import gzip

# Create a Person object and set some fields
person = person_pb2.Person()
person.name = "Alice"
person.age = 30
person.email = "alice@example.com"

# Serialize the Person object to a binary format
serialized_data = person.SerializeToString()

# Compress the serialized data using gzip
compressed_data = gzip.compress(serialized_data)

# Save the compressed data to a file
with open("person_compressed.bin", "wb") as f:
    f.write(compressed_data)

# Read the compressed data from the file
with open("person_compressed.bin", "rb") as f:
    compressed_data_read = f.read()

# Decompress the data using gzip
decompressed_data = gzip.decompress(compressed_data_read)

# Deserialize the decompressed data back into a Person object
person_read = person_pb2.Person()
person_read.ParseFromString(decompressed_data)

# Print the deserialized Person object
print("deserialized data: ")
print(person_read)

#
# Save the serialized data to a file
with open("person_uncompressed.bin", "wb") as f:
    f.write(serialized_data)

# Read the serialized data from the file
with open("person_uncompressed.bin", "rb") as f:
    serialized_data_read = f.read()

# Deserialize the data back into a Person object
person_read_uncompressed = person_pb2.Person()
person_read_uncompressed.ParseFromString(serialized_data_read)

# Print the deserialized Person object
print("Uncompressed data: ")
print(person_read_uncompressed)
