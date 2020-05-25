"""
In regex terms:
a* means 0 or more occurances of a. 0 or more occurances of the literal that immediately precedes the astericks.
in the above case it would be foo a* bar

. is the wildcard that represents any character - but that has to be a character
\s represents single white space
[] use this to put the character
^ is the negation
"""

import pandas as pd
import re

x1 = pd.read_csv('./original/regex01.txt', header=None)
x1 = list(x1[0])
# find a pattern in x1
# [re.match('fooa*bar',i) for i in x1]
# [re.search('fooa*bar',i) for i in x1]
[re.findall('fooa*bar', i) for i in x1]
[re.findall('fooa+bar', i) for i in x1]

# second example
x2 = pd.read_csv('./original/regex02.txt', header=None)
x2 = list(x2[0])
[re.findall('foo.bar', i) for i in x2]

# third example
x3 = pd.read_csv('./original/regex03.txt', header=None)
x3 = list(x3[0])
[re.findall('foo.*bar', i) for i in x3]

# fourth example
x4 = pd.read_csv('./original/regex04.txt', header=None)
x4 = list(x4[0])
x4
[re.findall('foo\s*bar', i) for i in x4]

# fifth example
x5 = pd.read_csv('./original/regex05.txt', header=None)
x5 = list(x5[0])
x5
[re.findall('[fcl]oo', i) for i in x5]

# fifth example ^ class is the negation
x6 = pd.read_csv('./original/regex06.txt', header=None)
x6 = list(x6[0])
x6
[re.findall('[^mh]oo', i) for i in x6]

# fifth example ^ class is the negation
x8 = pd.read_csv('./original/regex08.txt', header=None)
x8 = list(x8[0])
x8
[re.findall('[j-m]oo', i) for i in x8]
[re.findall('[j-mz]oo', i) for i in x8]
[re.findall('[zj-m]oo', i) for i in x8]

# sixth example
x10 = pd.read_csv('./original/regex10.txt', header=None)
x10 = list(x10[0])
x10
[re.findall('[j-m]oo', i) for i in x10]
[re.findall('[j-mJ-Mz]oo', i) for i in x10]
[re.findall('[zj-mJ-M]oo', i) for i in x10]

# seventh example
x11 = pd.read_csv('./original/regex11.txt', header=None)
x11 = list(x11[0])
x11
[re.findall('x*\.y*', i) for i in x11]
[re.findall('x+\.y+', i) for i in x11]
[re.findall('x+[.]y+', i) for i in x11]

# eighth example
x12 = pd.read_csv('./original/regex12.txt', header=None)
x12 = list(x12[0])
x12
[re.findall('x[.#:]y', i) for i in x12]

# ninth example
x13 = pd.read_csv('./original/regex13.txt', header=None)
x13 = list(x13[0])
x13
[re.findall('x[:#\^]y', i) for i in x13]

# ninth example
x14 = pd.read_csv('./original/regex14.txt', header=None)
x14 = list(x14[0])
x14
[re.findall('x[#\\\^]y', i) for i in x14]

# ninth example
x15 = pd.read_csv('./original/regex15.txt', header=None)
x15 = list(x15[0])
x15
[re.findall('^foo.*', i) for i in x15]

# 10th example
x16 = pd.read_csv('./original/regex16.txt', header=None)
x16 = list(x16[0])
x16
[re.findall('.*bar$', i) for i in x16]


# 10th example
x17 = pd.read_csv('./original/regex17.txt', header=None)
x17 = list(x17[0])
x17
[''.join(re.findall('^foo$', i)) for i in x17]


# 11th example
x18 = pd.read_csv('./original/regex18.txt', header=None)
x18 = list(x18[0])
x18
[''.join(re.findall('^[0-9][0-9][0-9]$',str(i))) for i in x18]
[''.join(re.findall('^[0-9]{3}$',str(i))) for i in x18]


# 12th example
x19 = pd.read_csv('./original/regex19.txt', header=None)
x19 = list(x19[0])
x19
[''.join(re.findall('^[a-z]{4,6}$',str(i))) for i in x19]


# 12th example
x20 = pd.read_csv('./original/regex20.txt', header=None)
x20 = list(x20[0])
x20
print([i for i in x20 if bool(re.search('(ha){4,}',i))])


# 13th example
x21 = pd.read_csv('./original/regex21.txt', header=None)
x21 = list(x21[0])
x21
print([i for i in x21 if bool(re.search('^(ha){1,2}$',i))])
print([i for i in x21 if bool(re.search('^(ha){,2}$',i))])


# 22th example
x22 = pd.read_csv('./original/regex22.txt', header=None)
x22 = list(x22[0])
x22
print([i for i in x22 if bool(re.search('fooa+bar',i))])

# 23th example
x23 = pd.read_csv('./original/regex23.txt', header=None)
x23 = list(x23[0])
x23
print([i for i in x23 if bool(re.search('^http[s]{0,1}://website',i))])
print([i for i in x23 if bool(re.search('^https?://website',i))])
print([i for i in x23 if bool(re.search('^(https:|http:)//website',i))])


# 24th example
x24 = pd.read_csv('./original/regex24.txt', header=None)
x24 = list(x24[0])
x24
print([i for i in x24 if bool(re.search('(log|ply)wood',i))])
print([i for i in x24 if bool(re.search('^(log|ply)wood$',i))])


# 25th example
x25 = pd.read_csv('./original/regex25.txt', header=None)
x25 = list(x25[0])
x25
print([re.sub('x(0-9){3}]',' pix by (0-9){3} pix',i) for i in x25])
print([re.sub('x',' pix by ',i) for i in x25])
# Answer
print([re.sub('([0-9]+)x([0-9]+)','\\1 pix by \\2 pix',i) for i in x25])


# 26th example
x26 = pd.read_csv('./original/regex26.txt', header=None)
x26 = list(x26[0])
x26
print([re.sub('([a-zA-Z]+) ([a-zA-Z]+)','\\2,\\1' ,i) for i in x26])
print([re.sub('([a-zA-Z]+)\s([a-zA-Z]+)','\\2,\\1' ,i) for i in x26])


# 27th example
x27 = pd.read_csv('./original/regex27.txt', header=None)
x27 = list(x27[0])
x27
print([re.sub('([0-9]{,2}):([0-9]{,2})','\\2 mins past \\1' ,i) for i in x27])
print([re.sub('([0-9]{1,2}):([0-9]{2})','\\2 mins past \\1' ,i) for i in x27])
print([re.sub('([0-9]{,2}):([0-9]{2})','\\2 mins past \\1' ,i) for i in x27])

# 28th example
x28 = pd.read_csv('./original/regex28.txt', header=None)
x28 = list(x28[0])
x28
print([re.sub('([0-9]{3})\.([0-9]{3})\.([0-9]{4})','xxx.xxx.\\3' ,i) for i in x28])
print([re.sub('[0-9]{3}\.[0-9]{3}\.([0-9]{4})','xxx.xxx.\\1' ,i) for i in x28])

# 29th example
x29 = pd.read_csv('./original/regex29.txt', header=None)
x29 = list(x29[0])
x29
print([re.sub('([a-zA-Z]{3})\s([0-9]{1,2}).+\s[0-9]{2}([0-9]{2})','\\2-\\1-\\3' ,i) for i in x29])
print([re.sub('([a-zA-Z]{3})\s([0-9]{1,2})[a-zA-Z]{2}\s[0-9]{2}([0-9]{2})','\\2-\\1-\\3' ,i) for i in x29])


# 30th example
x30 = pd.read_csv('./original/regex30.txt', header=None)
x30 = list(x30[0])
x30
print([re.sub('\\((.*)\\)','\\1' ,i) for i in x30])


