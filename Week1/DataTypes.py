"""
Text type: str
Numeric Datatypes: int, float, complex
Sequence: list, tuple, range
Mapping: dict
set type: set, frozenset
Boolean: bool
Binary: bytes, bytearray, memoryview
None type: NoneType

"""

complex_type = 1j
print(type(complex_type))
bytes_type = b"HEllo"
print(type(bytes_type))

bytearray_type = bytearray(5)
print(bytearray_type)
print(type(bytearray_type))

x = memoryview(bytes(4))
print(x)
print(x)


