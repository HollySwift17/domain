import re
from collect_data.fun.head import *
__url__ = "https://openphish.com/feed.txt"
__check__ = "http://"
__info__ = "phishing"
__reference__ = "openphish.com"

def fetch():
    retval = {}
    content = getcontent(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '://' in line:
                line = re.search(r"://(.*)", line).group(1)
            line = line.rstrip('/')
            retval[line] = (__info__, __reference__)

    return retval
if __name__ == '__main__':
    print(fetch())
