import re
from collect_data.fun.head import *
__url__ = "http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt"
__check__ = "Master Feed"
__reference__ = "bambenekconsulting.com"
def fetch():
	retval = {}

	content = getcontent(__url__)

	if __check__ in content:
		for match in re.finditer(r"(?m)^([^,#]+),Domain used by ([^,/]+)", content):
			retval[match.group(1)] = ("%s (malware)" % match.group(2).lower().strip(), __reference__)

	return retval
if __name__ == '__main__':
	print(fetch())
