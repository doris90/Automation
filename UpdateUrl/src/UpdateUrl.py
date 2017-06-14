'''
Created on 2017-6-14

@author: yushao
'''
import urllib2
import os

dict1 = {'Pmtappsvc2Pgwpmtsoa': os.environ["Pmtappsvc2Pgwpmtsoa"]}
dict2 = {'Pmtappsvc2Pgwsecdas': os.environ["Pmtappsvc2Pgwsecdas"]}
dicts = [dict1['Pmtappsvc2Pgwpmtsoa'] , dict2['Pmtappsvc2Pgwsecdas']]

for di in dicts:
  
  url = di
  print (url)
  
  response=urllib2.urlopen(url)
  
  print(response.info())   
  print(response.geturl())  
  print(response.getcode())