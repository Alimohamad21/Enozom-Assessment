import hashlib

file_lines = open('annual-enterprise-survey-2020-financial-year-provisional-csv.csv')
i = 0
output = ''
for line in file_lines:
    if i % 2 == 1:
        third_column = line.split(',')[2]
        output += third_column
    i += 1
print(f'Output String:{output}')
output_md5_hashed = hashlib.md5(output.encode()).hexdigest().upper()
print(f'MD5 Hashed Output String:{output_md5_hashed}')