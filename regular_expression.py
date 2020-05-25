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

