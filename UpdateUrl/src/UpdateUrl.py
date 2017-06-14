'''
Created on 2017-6-14

@author: yushao
'''
# import urllib2
# import os
# 
# dict1 = {'Pmtappsvc2Pgwpmtsoa': os.environ["Pmtappsvc2Pgwpmtsoa"]}
# dict2 = {'Pmtappsvc2Pgwsecdas': os.environ["Pmtappsvc2Pgwsecdas"]}
# dicts = [dict1['Pmtappsvc2Pgwpmtsoa'] , dict2['Pmtappsvc2Pgwsecdas']]
# 
# for di in dicts:
#   
#   url = di
#   print (url)
#   
#   response=urllib2.urlopen(url)
#   
#   print(response.info())   
#   print(response.geturl())  
#   print(response.getcode())

import urllib.request
# import os
   
dict = {'pmtappsvc': 'http://monterey-9092.slc07.dev.ebayc3.com:8080/admin/v3console', 'pgwsecdas': 'http://monterey-5179.slc01.dev.ebayc3.com:8080/pgwpmtsoa/PgwServiceV1'}
# dict = {'pmtappsvc': 'http://monterey-9092.slc07.dev.ebayc3.com:8080/admin/v3console', 'pgwsecdas': 'http://pgwsecdas-stg.stratus.qa.ebay.com/pgwsecdas/v1'}
 
# dict = {'pmtappsvc': $pmtappsvc, 'pgwsecdas': $pgwsecdas}
url = dict['pmtappsvc']+"/UpdateConfigCategoryXml?"+"id=org.ebayopensource.ginger.client.pgwdas.staging.PGWDasClient&ENDPOINT_URI="+dict['pgwsecdas']
 
 
print (url)

response=urllib.request.urlopen(url)
 

print(response.info()) 

print(response.geturl())
 
print(response.getcode())