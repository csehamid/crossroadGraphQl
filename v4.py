import requests
import json


f1=open('./output.txt', 'w+')

def getcommits(owner , repoName ):

    
    f1.write ("-------------------------------------------------------------------------------------------------");
    f1.write( "The first 100 Commits for Repository " + repoName + " owned by " + owner + "\n")
    
    query =('{repository(name: "' + repoName +'", owner: "'+owner+'") { ref(qualifiedName: "master") { target { ... on Commit { id history(first: 100) { pageInfo { hasNextPage } edges { node { message}}}}}}}}')
    
    headers = {'Authorization': 'token XXXX'}
    
    r1=requests.post('https://api.github.com/graphql', json.dumps({"query": query}), headers=headers)
    
    
    result= r1.json()
    
    i=0
    jsonSize=len(result[u'data'] [u'repository'] [u'ref'][u'target'][u'history'][u'edges'])
    while (i<jsonSize):     
               
        f1.write( str(jsonSize-i) +"  "+ result[u'data'] [u'repository'] [u'ref'][u'target'][u'history'][u'edges'][i][u'node'][u'message']+ "\n")
        i=i+1               
    

getcommits("csehamid" , "crossroad")
getcommits("onlydole","learnjs")

f1.close()