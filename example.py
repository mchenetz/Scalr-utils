from scriptsapi import scriptsapi
import os

## EXAMPLES
## Define Environments so you do not have to remember ids.
env = {
    'dc-lab':1
}
SCALR_API_KEY = os.environ['SCALR_API_KEY']
SCALR_SECRET_KEY = os.environ['SCALR_SECRET_KEY']
url = os.environ['SCALR_URL']

## init API with environment
api = scriptsapi(env['dc-lab'],url,SCALR_API_KEY,SCALR_SECRET_KEY)

## Print a listing of all Scripts in an environment
for list in api.listScripts():
    print list['name']

## Get Script by name and display the script
## getScriptByName(Name)
print (api.getScriptByName('rundeck-install'))

## List Versions of the Script
## listScriptVersions(ScriptID)
print (api.listScriptVersions(api.getIdFromName('theforeman-installer'))[0])


print (api.getScriptVersionByName('rundeck-install',1))

print (api.getLatestScriptVersion(6))
## Write All Script versions of a particular Script to a directory
## writeScriptVersionToFile(Environment, ScriptID, Directory)
## api.writeScriptVersionsToFile(env['dc-lab'],api.getIdFromName('theforeman-installer'),'C://Users//user//Documents//sscripts//')
api.writeAllScriptsAndVersionsToFile('testdir')
