import re
from collect_data.fun.head import *
__url__ = "http://data.netlab.360.com/feeds/dga/locky.txt"
__check__ = "netlab 360"
__info__ = "locky dga (malware)"
__reference__ = "360.com"
def fetch():
	retval = {}

	content = getcontent(__url__)

	if __check__ in content:
		for match in re.finditer(r"(?m)^([\w.]+)\s+2\d{3}\-", content):
			retval[match.group(1)] = (__info__, __reference__)

	return retval
#done
