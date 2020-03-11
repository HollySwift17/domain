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
		for match in re.finditer(r">([^<]+\.[a-zA-Z]+)</td>\s*<td style=\"background-color: rgb\(11, 11, 11\);\"><a href=\"ccamdetail\.php\?hash=", content):
			if "www." in match.group(1):
				string = match.group(1)[4:]
			else:
				string = match.group(1)
			retval[string] = (__info__, __reference__)

	return retval
#done
if __name__ == '__main__':
	print(fetch())
