#main
import tldextract
import pandas as pd
import time
import sys
sys.path.append(r'fun')
from collect_data.fun import conficker360
from collect_data.fun import cryptolocker360
from collect_data.fun import locky360
from collect_data.fun import necurs360

from collect_data.fun import bambenekconsultingc2dns
from collect_data.fun import dshielddns
from collect_data.fun import loki
from collect_data.fun import malwaredomainlistdns
from collect_data.fun import openphish
from collect_data.fun import pony
from collect_data.fun import ransomwaretrackerdns
from collect_data.fun import ransomwaretrackerurl
from collect_data.fun import sslproxies
from collect_data.fun import urlvir
from collect_data.fun import vxvault
from collect_data.fun import zeustrackerdns
from collect_data.fun import zeustrackermonitor
from os import path
import os
d = path.dirname(__file__)
parent_path = os.path.dirname(d)

def collect_main():
	result = {}
	result.update(conficker360.fetch())
	result.update(cryptolocker360.fetch())
	result.update(locky360.fetch())
	result.update(necurs360.fetch())
	result.update(bambenekconsultingc2dns.fetch())
	result.update(dshielddns.fetch())
	result.update(loki.fetch())
	result.update(malwaredomainlistdns.fetch())
	result.update(openphish.fetch())
	result.update(pony.fetch())
	result.update(ransomwaretrackerdns.fetch())
	result.update(ransomwaretrackerurl.fetch())
	result.update(sslproxies.fetch())
	result.update(urlvir.fetch())
	result.update(vxvault.fetch())
	result.update(zeustrackerdns.fetch())
	result.update(zeustrackermonitor.fetch())
	print(len(result))
	for key in list(result.keys()):
		dom = tldextract.extract(key).domain
		suf = tldextract.extract(key).suffix
		if not suf=='':
			result[dom+'.'+suf] = result.pop(key)
		else:
			result.pop(key)
	timestr = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	pd.DataFrame(result).to_csv(parent_path+ '/data_csv/'+ timestr + ".csv")
        

	file = open(parent_path +'/data_txt/'+ timestr +".txt","w",encoding='utf-8')
	for key in result.keys():
		file.write(key+'\n')
	file.close()
	print('all finished')
