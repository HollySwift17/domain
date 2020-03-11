import re
import time
from collect_data.fun.head import *
__url__ = "https://isc.sans.edu/feeds/suspiciousdomains_Low.txt"
__check__ = "DShield.org"
__info__ = "domain (suspicious)"
__reference__ = "dshield.org"

def fetch():
	retval = {}
	content = getcontent(__url__)
	timestr = time.strftime('%a %b %d',time.localtime(time.time()))
	if __check__ in content:
		if timestr in content:
			for line in content.split('\n'):
				line = line.strip()
				if not line or line.startswith('#') or '.' not in line:
					continue
				retval[line] = (__info__, __reference__)

	return retval
if __name__ == '__main__':
	print(fetch())
