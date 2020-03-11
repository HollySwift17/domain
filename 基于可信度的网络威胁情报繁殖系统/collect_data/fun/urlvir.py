from collect_data.fun.head import *
import re
__url__ = "http://www.urlvir.com/export-hosts/"
__check__ = "Updated on"
__info__ = "malware"
__reference__ = "urlvir.com"

def fetch():
	retval = {}
	content = getcontent(__url__)

	if __check__ in content:
		for line in content.split('\n'):
			line = line.strip()
			if not line or line.startswith('#') or '.' not in line:
				continue
			if not re.search(r"[a-zA-Z]",line):
				continue
			retval[line.strip()] = (__info__, __reference__)

	return retval
if __name__ == '__main__':
	print(fetch())
