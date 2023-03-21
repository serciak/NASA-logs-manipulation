import sys
sys.path.append('../')
from util import regex_matches as rm
from util import get_file_extension as gfe

line = 'rose.glg.ed.ac.uk - - [27/Jul/1995:08:30:56 -0400] "GET /images/NASA-logosmall align=left HTTP/1.0" 200 786'
line2 = '155.78.101.61 - - [25/Jul/1995:14:12:43 -0400] "GET /pub/winvn/readme.txt HTTP/1.0" 404 -'

match = rm.get_regex_match(line)

fe = gfe.get_file_extension(match)

print(fe)

print(match.groups())
