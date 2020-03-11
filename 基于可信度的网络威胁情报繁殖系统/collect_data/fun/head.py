import requests
def getcontent(url):
	try:
		hd = {'user-agent':'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0'}
		r = requests.get(url,headers = hd,timeout = 50)
	#	print(r.status_code)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(url)
		print('finished')
		return r.text
	except:
		print(url)
		print('ERROR')
		return "ERROR"
