import re
from collect_data.fun.head import *
__url__ = "http://cybercrime-tracker.net/ccam.php"
__check__ = "Atmos Strategic Monitoring"
__info__ = "atmos (malware)"
__reference__ = "cybercrime-tracker.net"
def fetch():
	retval = {}

	content = getcontent(__url__)

	if __check__ in content:
		for line in content.split('\n'):
			line = line.strip()
			if not line or line.startswith('#') or '.' not in line:
				continue
			retval[line] = (__info__, __reference__)

	return retval
