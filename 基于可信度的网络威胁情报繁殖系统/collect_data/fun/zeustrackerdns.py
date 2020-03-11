from collect_data.fun.head import *
__url__ = "https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist"
__check__ = "ZeuS"
__info__ = "zeus (malware)"
__reference__ = "abuse.ch"

def fetch():
	retval = {}
	content = getcontent(__url__)

	if __check__ in content:
		for line in content.split('\n'):
			line = line.strip()
			if not line or line.startswith('#'):
				continue
			retval[line] = (__info__, __reference__)

	return retval
