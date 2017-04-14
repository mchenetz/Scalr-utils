from api.client import ScalrApiClient
import os

SCALR_API_KEY = os.environ['SCALR_API_KEY']
SCALR_SECRET_KEY = os.environ['SCALR_SECRET_KEY']
url = os.environ['SCALR_URL']

client = ScalrApiClient(url.rstrip("/"),SCALR_API_KEY,SCALR_SECRET_KEY)

def getIdFromName(envId, name):
    scripts = client.fetch('/api/v1beta0/user/{envId}/scripts/'.format(envId=envId))
    for script in scripts:
        if(script['name'] == name):
            return (script['id'])
    else:
        return 0

def getScript(envId, scriptId):
    return client.fetch('/api/v1beta0/user/{envId}/scripts/{scriptid}'.format(envId=envId, scriptid=scriptId))

def listScripts(envId):
    return client.fetch('/api/v1beta0/user/{envId}/scripts/'.format(envId=envId))

def listScriptVersions(envId, scriptId):
    return client.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/'.format(envId=envId, scriptId=scriptId))

def writeScriptVersionToFile(envId, scriptId, directory):
    versions = client.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/'.format(envId=envId, scriptId=scriptId))
    for version in versions:
        path = os.path.abspath(directory) + '\\' + getScript(scriptId)['name'] + str(version['version'])
        with open(path, 'w') as write:
            write.writelines(version['body'])
            write.close()


for list in listScripts(1):
    print list['name']

## Get Script by name and display the script
## getScript(Environment, ScriptID)
## ** In This case i used getIDFromName to input the ID from a given name **
print (getScript(1, getIdFromName(1,'rundeck-install')))

## List Versions of the Script
## listScriptVersions(environment, ScriptID)
print (listScriptVersions(1, 1)[0])

## Write All Script versions of a particular Script to a directory
## writeScriptVersionToFile(Environment, ScriptID, Directory)
## writeScriptVersionToFile(1,1,'C://Users//user//Documents//sscripts//')