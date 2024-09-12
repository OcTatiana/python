fin = open('source_leetcode_data.txt', 'r')
foutread = open('intervals.md', 'r')
s = foutread.read().split('[comment]: <> (Stop)')
fout = open('intervals.md', 'w')

name = fin.readline().split(". ")[1]
link = fin.readline()

fout.write(s[0])
fout.write('+ [{}](#{})\n\n'.format(name[:-1], link[30:-2]))
fout.write('[comment]: <> (Stop)')
fout.write(s[1])
fout.write('\n## {}\n{}\n'.format(name, link))
fout.write('```python\n')
fin.readline()
for line in fin:
    fout.write(line[4:])

fout.write('```')

fin.close()
fout.close()
