import glob

for filename in glob.iglob("C:/Users/Szymon Mazurek/Desktop/Studia/rokIII" + '**/**', recursive=True): ## insert directory path
     print(filename)
