import re
from collect_data.fun.head import *
import time
#__url__ = "http://vxvault.net/URL_List.php"
__url__ = "http://vxvault.net/ViriList.php"
__check__ = "VX Vault"
__info__ = "malware"
__reference__ = "vxvault.net"

def fetch():
    retval = {}
    content = getcontent(__url__)

    timestr = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if __check__ in content:
        for match in re.finditer(r'%s</a></TD>\s<TD class=\w+><a (class=\w+)* href=\'files/\w+\.zip\'>\[D\]</a> <a (class=\w+)* href=\'ViriFiche\.php\?ID=\d+\'>([-\w\./]+)</a>'%timestr,content):
            retval[match.group(3)] = (__info__, __reference__)

    return retval
if __name__ == '__main__':
    fetch()
