from scriptsapi import scriptsapi
import scriptscmd
import os
from os.path import expanduser
import argparse
import ConfigParser

home = expanduser("~")
configfile = '.scalr.cfg'
homeconfig = os.path.join(home,configfile)

if os.path.isfile(configfile) or os.path.isfile(homeconfig):
    config = ConfigParser.ConfigParser()
    if os.path.isfile(configfile):
        config.read(configfile)
    elif os.path.isfile(homeconfig):
        config.read(homeconfig)
    SCALR_API_KEY = config.get('Scalr','key')
    SCALR_SECRET_KEY = config.get ('Scalr','secret')
    SCALR_URL = config.get('Scalr','url')
else:
    SCALR_API_KEY = os.environ['SCALR_API_KEY']
    SCALR_SECRET_KEY = os.environ['SCALR_SECRET_KEY']
    SCALR_URL = os.environ['SCALR_URL']

print ('Scalr Scripting CLI - Michael Chenetz 2017')
print ('------------------------------------------')
parser = argparse.ArgumentParser(prog='scripts-cli',description='Scalr Scripting CLI')
parser.add_argument('--env', required=True, help='Scalr Environment')
action = parser.add_mutually_exclusive_group()
action.add_argument('-ls','--listscripts', help='Lists all scripts', action='store_const', const=True)
action.add_argument('-in', '--interactive', help='Interactive console', action='store_const', const=True)
action.add_argument('-gs', '--getscript', help='Get specific script', nargs=2, metavar=('[Script]','[Version]'))
action.add_argument('-gasv','--getallscriptversions', help='Get all script versions', nargs=1, metavar=('[Script]'))
action.add_argument('-wasv','--writeallscriptversions', help='write all script versions to directory', nargs=2, metavar=('[Script]', '[directory]'))
action.add_argument('-wasd', '--writeallscriptstodirectory', help='Writes all scripts and versions to directory', nargs=1, metavar=('[Directory]'))
action.add_argument('-le', '--listenvironment', help='List all available environments', action='store_const', const=True)
parser.add_argument('output', type=argparse.FileType('w'), help="Specifies the output file", nargs='?', const='-')
args = parser.parse_args()
cli = vars(args)
api = scriptsapi(cli['env'],SCALR_URL,SCALR_API_KEY,SCALR_SECRET_KEY)

# print cli
if cli['listenvironment'] !=None:
    args.output.write('Environments: ')
    for env in api.listEnvironments():
        args.output.write (str(env['id']) +'. '+env['name'])
elif cli['listscripts'] != None:
    args.output.write ('Scripts: ')
    for list in api.listScripts():
        args.output.write (str(list['id']) + '. ' + list['name'])
elif cli['interactive'] != None:
    cmd = scriptscmd.scriptscmd(api)
    cmd.cmdloop()
elif cli['getscript']:
    scriptName = cli['getscript'][0]
    version = cli['getscript'][1]
    if version.isdigit():
        if scriptName.isdigit():
            args.output.write(api.getScriptVersion(scriptName, version)['body'])
        else:
            args.output.write(api.getScriptVersion(api.getIdFromName(scriptName), version)['body'])
    else:
        if scriptName.isdigit():
            args.output.write(api.getScriptVersion(scriptName, api.getLatestScriptVersion(scriptName))['body'])
        else:
            args.output.write(api.getScriptVersion(api.getIdFromName(scriptName), api.getLatestScriptVersion(api.getIdFromName(scriptName)))['body'])
elif cli['getallscriptversions']:
    scriptName = cli['getallscriptversions'][0]
    if scriptName.isdigit():
        print ('number')
        scriptVersions = api.listScriptVersions(scriptName)
    else:
        print('name')
        scriptVersions = api.listScriptVersions(api.getIdFromName(scriptName))
    if scriptVersions:
        for version in scriptVersions:
            print (version['body'])
elif cli['writeallscriptversions']:
    scriptName = cli['writeallscriptversions'][0]
    directory = cli['writeallscriptversions'][1]
    if scriptName.isdigit():
        scriptId = scriptName
    else:
        scriptId = api.getIdFromName(scriptName)
    if scriptId:
        api.writeScriptVersionsToFile(scriptId, directory)
elif cli['writeallscriptstodirectory']:
    directory = cli['writeallscriptstodirectory'][0]
    print ('Writing All Scripts and Versions to: ', directory)
    api.writeAllScriptsAndVersionsToFile(directory)
    print ('Completed!')