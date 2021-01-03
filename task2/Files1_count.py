import os
file_count=0
for root, dirs, files in os.walk("/", topdown=False):
    file_count=file_count+1

print(file_count)


#path, dirs, files = (os.walk("A"))
#print (files)
