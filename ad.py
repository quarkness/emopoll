import requests
import re
import argparse
import simplejson

parser = argparse.ArgumentParser()
parser.add_argument('url', action="store")
parser.add_argument('mening', action="store")
args = parser.parse_args()

match = re.match('.*detail/(\d+)/.*', args.url)
componentId = match.group(1)

# print componentId

smaakjes = {
	'fascinerend': '1',
	'grappig': '2',
	'hartverwarmend': '3',
	'ergerlijk': '4',
	'beangstigend': '5',
	'deprimerend': '6',
}

smaakjes_reverse = dict((v,k) for k,v in smaakjes.items())

if args.mening not in smaakjes:
	raise Exception('mening moet 1 van %s zijn' % smaakjes.keys())

vote = smaakjes[args.mening]

headers = {
	'Accept':'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11',
	'Origin': 'http://www.ad.nl',
	'Referer': args.url,
	}

payload = {
	'vote': vote, 
	'componentId': componentId,
	'language': 'nl',
	}

r = requests.post("http://www.ad.nl/ad/article/emoVotes.do", data=payload, headers=headers)

# print r.status_code
# print r.headers

tussenstand = simplejson.loads(r.content)
print tussenstand

for k,v in tussenstand.items()
match = re.match('emo(.)percent', args.url)
smaaknummer = match.group(1)




