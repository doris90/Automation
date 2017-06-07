'''
Created on 2017-6-7

@author: yushao
'''
import urllib.request
url = "http://monterey-9092.slc07.dev.ebayc3.com:8080/admin/v3console/UpdateConfigCategoryXml?id=com.ebay.soa.client.PgwServiceV1Client.PgwServiceV1ClientConsumer.staging.Invoker&SERVICE_URL=http%3A%2F%2Fmonterey-5432.slc01.dev.ebayc3.com%3A8080%2Fpgwpmtsoa%2FPgwServiceV1"


#返回一个对象
response=urllib.request.urlopen(url)

#打印出远程服务器返回的header信息
print(response.info()) 

#打印出来访问的网址
print(response.geturl())

#打印出来http的状态,200就证明正常
print(response.getcode())

