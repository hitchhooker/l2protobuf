# l2protobuf
This repo is learning practice to understand protobuf.

## Intro
Protocol Buffers (protobuf) is a language-agnostic binary serialization format developed by Google.
It allows you to define data structures called "messages" and then serialize these structures into
a compact binary format. The primary benefits of using protobuf are smaller message size and faster
serialization/deserialization compared to other formats like JSON or XML.

## Example
Here's an example of how you can define a protobuf message and use it to serialize and deserialize
data in both compressed and uncompressed formats.

1. Define a .proto file:
Suppose we want to define a simple "Person" message with some basic information. We create a file
called "person.proto" with the following content:

```proto
syntax = "proto3";

message Person {
  string name = 1;
  int32 age = 2;
  string email = 3;
}
```

2. Compile the .proto file:
Use the protoc compiler to generate language-specific code. For example, to generate Python 
code, run:

```bash
protoc --python_out=. person.proto
```

This will generate a file called "person_pb2.py" containing the Python code for the Person message.

3. Serialize and deserialize the message:

Create a Python script to serialize and deserialize the Person message. Here's an example:
```python
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
print(person_read)
```

This script creates a Person object, serializes it to binary format, compresses the binary data using gzip,
and saves the compressed data to a file. Then, it reads the compressed data from the file, decompresses it,
and deserializes it back into a Person object.

For the uncompressed version, you can simply skip the gzip compression and decompression steps, like this:
```
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
print(person_read_uncompressed)
```

## Conclusions

### Advantages of protobuf:

- ***Language-agnostic***: Protobuf has support for multiple languages, including C++, Java, Python, Ruby, and more. This makes it a great choice for communication between services written in different programming languages.

- ***Compact binary format***: Protobuf messages are serialized to a compact binary format, which can result in smaller message sizes compared to text-based formats like JSON or XML.

- ***Schema evolution***: Protobuf allows you to evolve your data structures without breaking compatibility with older clients or servers. You can add new fields or deprecate existing ones without affecting existing serialized data.

- ***Widespread adoption***: Protobuf is widely used in industry, and there are numerous tools, libraries, and resources available to work with it.

### Disadvantages of protobuf:

- ***Binary format***: Protobuf's binary format can be more difficult to debug and inspect compared to human-readable formats like JSON or XML.

- ***Compilation step***: Protobuf requires a compilation step to generate language-specific code from the .proto files. This can add complexity to your build process.

In our testing compressed file end up being larger than the uncompressed file in this specific case
because the original data is very small, and the compression algorithm (gzip) adds some overhead for
storing metadata and maintaining the compressed file structure. For very small data, this overhead can
result in a compressed file that is larger than the original data.

In general, compression algorithms like gzip work better with larger datasets where there are more
opportunities for identifying and removing redundancy. In those cases, you would typically see a significant
reduction in the file size after compression. However, when working with small data like the example provided,
the compression overhead can outweigh the benefits, leading to a larger compressed file.
