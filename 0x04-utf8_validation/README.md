# UTF-8 Validation
This programming challenge focuses on UTF-8 encoding. The main goal is
to write a program that validates a given dataset if it is valid UTF-8.
The requirements and the assumptions are:
* Prototype: def validUTF8(data)
* Return: True if data is a valid UTF-8 encoding, else return False
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer