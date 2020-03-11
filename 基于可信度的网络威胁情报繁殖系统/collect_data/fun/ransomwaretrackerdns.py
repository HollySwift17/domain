from collect_data.fun.head import *
import time
__url__ = "http://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt"
__check__ = "questions"
__info__ = "ransomware (malware)"
__reference__ = "abuse.ch"

def fetch():
	retval = {}
	content = getcontent(__url__)
	timestr = time.strftime('%Y-%m-%d',time.localtime(time.time()))

	if __check__ in content:
		if timestr in content:
			for line in content.split('\n'):
				line = line.strip()
				if not line or line.startswith('#'):
					continue
				retval[line] = (__info__, __reference__)

	return retval
if __name__ == '__main__':
	print(fetch())
