import hashlib

file_lines = open('testcase.csv')
i = 0
output = ''
for line in file_lines:
    if i % 2 == 1:
        third_column = line.split(',')[2]
        output += third_column
    i += 1
print(output)
output_md5_hashed = hashlib.md5(output.encode()).hexdigest().upper()
print(output_md5_hashed)
