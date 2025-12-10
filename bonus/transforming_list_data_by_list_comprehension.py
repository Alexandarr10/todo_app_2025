filenames = ['1.doc', '1.report', '1.presentation']

filenames = [filename.replace('.', '-') for filename in filenames]

print(filenames)