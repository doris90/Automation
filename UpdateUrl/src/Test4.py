# -*- coding:utf-8 -*-  
'''
Created on 2017-6-7

@author: yushao
'''
# import urllib.request
# import os
#   
# # dict = {'pmtappsvc': 'http://monterey-9092.slc07.dev.ebayc3.com:8080/admin/v3console', 'pgwsecdas': 'http://monterey-5179.slc01.dev.ebayc3.com:8080/pgwpmtsoa/PgwServiceV1'}
# # dict = {'pmtappsvc': 'http://monterey-9092.slc07.dev.ebayc3.com:8080/admin/v3console', 'pgwsecdas': 'http://pgwsecdas-stg.stratus.qa.ebay.com/pgwsecdas/v1'}
# 
# dict = {'pmtappsvc': $pmtappsvc, 'pgwsecdas': $pgwsecdas}
# url = dict['pmtappsvc']+"/UpdateConfigCategoryXml?"+"id=org.ebayopensource.ginger.client.pgwdas.staging.PGWDasClient&ENDPOINT_URI="+dict['pgwsecdas']
# 
# 
# print (url)
# #返回一个对象
# response=urllib.request.urlopen(url)
# 
# #打印出远程服务器返回的header信息
# print(response.info()) 
# 
# #打印出来访问的网址
# print(response.geturl())
# 
# #打印出来http的状态,200就证明正常
# print(response.getcode())

# import urllib.request
# #import urllib2
# import os
# 
# dict1 = {'Pas2Pgwpmtsoa': 'http://pmtappsvc-2.stratus.qa.ebay.com/admin/v3console/UpdateConfigCategoryXml?id=com.ebay.soa.client.PgwServiceV1Client.PgwServiceV1ClientConsumer.staging.Invoker&SERVICE_URL=http%3A%2F%2Fmonterey-5432.slc01.dev.ebayc3.com%3A8080%2Fpgwpmtsoa%2FPgwServiceV1'}
# dict2 = {'Pas2Pgwsecdas': 'http://pmtappsvc-2.stratus.qa.ebay.com/admin/v3console/UpdateConfigCategoryXml?id=org.ebayopensource.ginger.client.pgwdas.staging.PGWDasClient&ENDPOINT_URI=http%3A%2F%2Fmonterey-5179.slc01.dev.ebayc3.com%3A8080%2Fpgwsecdas%2Fv1'}
# #url = dict['pmtappsvc']+"/admin/v3console" + "/UpdateConfigCategoryXml?"+"id=org.ebayopensource.ginger.client.pgwdas.staging.PGWDasClient&ENDPOINT_URI="+dict['pgwsecdas']
# dicts = [dict1['Pas2Pgwpmtsoa'] , dict2['Pas2Pgwsecdas']]
# 
# for di in dicts:
# 
#     url = di
#     print (url)
# 
#     response=urllib.request.urlopen(url)
#     
#     print(response.info()) 
#     
#     print(response.geturl())
#     
#     print(response.getcode())

