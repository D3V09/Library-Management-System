s = "b'11477'"
print(type(s))

cleaned_string = s[2:-1]

byte_string = cleaned_string.encode('utf-8')
print(type(byte_string))

regular_string = byte_string.decode('utf-8')
print(regular_string)

