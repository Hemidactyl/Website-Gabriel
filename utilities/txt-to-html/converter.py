#this little thing just takes a .txt file and makes it so that each line-break is replaced with HTML paragraph tags


print('Enter file name (must be *.txt):')
filename = input()
write_filename = filename[:-4]

print(write_filename)


read_path = '/root/projects/mysite/utilities/txt-to-html/to-convert/' + filename
write_path = '/root/projects/mysite/utilities/txt-to-html/converted/' + write_filename + '.html'

#open the file
try:
    fr = open(read_path, 'r')
except:
    print('No such file exists!')

#print(fr.read())
fw = open(write_path, 'w+')

#write <p> at the beginning
fw.write('<p>\n')

#copy all the lines from the original file and add paragraph end+beginning between them
for line in fr:
    fw.write(line)
    fw.write('</p>\n')
    fw.write('<p>\n')

fr.close()
fw.close()