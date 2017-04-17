from api.client import ScalrApiClient
import os

## Set Scalr keys and URL. I have them set in the environment for development purposes.
SCALR_API_KEY = os.environ['SCALR_API_KEY']
SCALR_SECRET_KEY = os.environ['SCALR_SECRET_KEY']
url = os.environ['SCALR_URL']

## Define Environments so you do not have to remember ids.
env = {
    'dc-lab':1
}

client = ScalrApiClient(url.rstrip("/"),SCALR_API_KEY,SCALR_SECRET_KEY)

class scriptsapi(object):

    def __init__(self, env):
        self.env = env

    def getIdFromName(self, name):
        scripts = client.fetch('/api/v1beta0/user/{envId}/scripts/'.format(envId=self.env))
        for script in scripts:
            if(script['name'] == name):
                return (script['id'])
        else:
            return 0

    def getScript(self, scriptId):
        return client.fetch('/api/v1beta0/user/{envId}/scripts/{scriptid}'.format(envId=self.env, scriptid=scriptId))

    def listScripts(self):
        return client.fetch('/api/v1beta0/user/{envId}/scripts/'.format(envId=self.env))

    def listScriptVersions(self, scriptId):
        return client.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/'.format(envId=self.env, scriptId=scriptId))

    def writeScriptVersionToFile(self, scriptId, directory):
        versions = client.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/'.format(envId=self.env, scriptId=scriptId))
        for version in versions:
            path = os.path.abspath(directory) + '\\' + getScript(scriptId)['name'] + str(version['version'])
            with open(path, 'w') as write:
                write.writelines(version['body'])
                write.close()


## init API with environment
api = scriptsapi(env['dc-lab'])

## Print a listing of all Scripts in an environment
for list in api.listScripts():
    print list['name']

## Get Script by name and display the script
## getScript(ScriptID)
## ** In This case i used getIDFromName to input the ID from a given name **
print (api.getScript(api.getIdFromName('rundeck-install')))

## List Versions of the Script
## listScriptVersions(ScriptID)
print (api.listScriptVersions(api.getIdFromName('theforeman-installer'))[0])

## Write All Script versions of a particular Script to a directory
## writeScriptVersionToFile(Environment, ScriptID, Directory)
## writeScriptVersionToFile(env['dc-lab'],getIdFromName(env['dc-lab'],'theforeman-installer'),'C://Users//user//Documents//sscripts//')