import urllib2
import os
import sys

def initiateString(input):
    reSet = {}
    inputSet = input.split("\n");
    print(inputSet)
    for i in inputSet:
        ins = i.strip().split(" ");
        reSet.setdefault(ins[0] , ins[1])
    return reSet

if __name__ == '__main__':
    
    pools = {}
    pro = {}
    Pools = os.environ["pools"]
    relationship = os.environ["relationship"]
    inner = "/admin/v3console/UpdateConfigCategoryXml?id="
    Id = os.environ["ids"]
    properties = os.environ["properties"]
    
    
    ids = initiateString(Id)
    pro = initiateString(properties)     
    pools = initiateString(Pools)
  
    
    relas = relationship.split("\n")
        
    for i in range(0, len(relas)):
        res = relas[i].strip().split("->")
        porperty = pro.get(str(i))
        for j in range(0, len(relas)-1, 2):
            res1 = res[j]
            res2 = res[j+1]
            list = [pools[res1] , inner , ids.get(str(i)) , "&", porperty , "=", pools[res2]]
            response=urllib2.urlopen("".join(list))
            print(response.geturl())  
            print(response.getcode())
            print(response.info())