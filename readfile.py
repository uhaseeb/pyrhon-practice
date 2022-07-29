file_read = open("countries.txt", 'r')
for country in file_read:
    print(country)
file_read.close()