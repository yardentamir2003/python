# line = "Superman 1978 1980 1983 1987 2006"
# line = line.split()
# print(line)

import re
words_list = ["babon", "1", "45"]
words_list = re.sub('[^/d]', '', words_list)
print(words_list)