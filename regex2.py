import re
check1 = 'phone number 590-235-8720'
re.findall('([0-9]{3}-[0-9]{3}-[0-9]{4})',check1)
re.findall('(\d{3}-\d{3}-\d{4})',check1)

pt = re.search('(\d{3}-\d{3}-\d{4})',check1)
pt.group()
pt.span() 
pt.start()
pt.end()

for match in re.finditer('(\d{3}-\d{3}-\d{4})',check1):
    print(match.span())


check2 = 'phone number 590-235-8720, 875-698-9856 and other ones'
pt = re.search('(\d{3}-\d{3}-\d{4})',check2)
pt.group()
ft = re.findall('(\d{3}-\d{3}-\d{4})',check2)
pt1 = re.search('(\d{3})-(\d{3})-(\d{4})',check2)
pt1.group()
pt1.group(1); pt1.group(2)

re.search('man|woman', 'this man was here')
re.search('man|woman', 'this woman was here')

re.findall('.at', 'the cat hat and matr')
re.findall('^\d', 'prada is a')
re.findall('^\d.*', '12prada is a')

string = 'prada is 36 in the 5 for 67'
re.findall('[^\d]+', string)
re.findall('[^\d]*', string)

test_phrase = 'this is a string! and how % are we going to @ remove?'
mytest = re.findall('[^!@?%]+', test_phrase)
''.join(mytest)
' '.join(mytest)

check = 'find hyphen-words and long-dash words in this phrase'
re.findall('[\w]+-[\w]+', check)








