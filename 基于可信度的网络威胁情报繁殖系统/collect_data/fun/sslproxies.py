from collect_data.fun.head import *
__url__ = "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/sslproxies_1d.ipset"
__check__ = "sslproxies_1d"
__info__ = "proxy (suspicious)"
__reference__ = "sslproxies.org"

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
