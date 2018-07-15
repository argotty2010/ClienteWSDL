import hashlib
import os
import datetime, time
from hashlib import sha1

identificador= '6dd490faf9cb87a9862245da41170ff2'
tranKey=u'024h1IlD'


def seed():	
	import datetime, time
	utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
	utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
	return(datetime.datetime.now().replace(microsecond=0).replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat())

def make_sha1(cadena, encoding='utf-8'):
    return sha1(cadena.encode(encoding)).hexdigest()


#imprimir algunas variables
print(seed())
print(make_sha1(str(seed())+tranKey))
print(len(make_sha1(seed()+tranKey)))



import zeep

transport = zeep.Transport(operation_timeout=10000)
wsdl='https://test.placetopay.com/soap/pse/?wsdl'
client = zeep.Client(wsdl=wsdl)

semilla=str(seed())
result = client.service.getBankList([identificador,make_sha1(semilla+tranKey),semilla,'',''])

