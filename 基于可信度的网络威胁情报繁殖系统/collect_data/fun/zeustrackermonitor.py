import re
from collect_data.fun.head import *
import time
__url__ = "https://zeustracker.abuse.ch/monitor.php?filter=all"
__check__ = "ZeuS Tracker"
__reference__ = "abuse.ch"

def fetch():
	retval = {}
	content = getcontent(__url__)
	timestr = time.strftime('%Y-%m-%d',time.localtime(time.time()))

	if __check__ in content:
		for match in re.finditer(r'<td>%s</td><td>([^<]+)</td><td><a href="/monitor.php\?host=([^"]+)'%timestr, content):
			retval[match.group(2)] = (match.group(1).lower() + " (malware)", __reference__)
	return retval
if __name__ == '__main__':
	print(fetch())
