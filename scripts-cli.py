from scriptsapi import scriptsapi
import scriptscmd
import os
import sys
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


parser = argparse.ArgumentParser(prog='scripts-cli',description='Scalr Scripting CLI')
parser.add_argument('--env', required=True, help='Scalr Environment')
action = parser.add_mutually_exclusive_group()
action.add_argument('-ls','--listscripts', help='Lists all Scalr Scripts', action='store_const', const=True)
action.add_argument('-in', '--interactive', help='Interactive Console', action='store_const', const=True)
action.add_argument('-gs', '--getscript', help='Get Script From Scalr', nargs=2, metavar=('[Script]','[Version]'))
parser.add_argument('output', type=argparse.FileType('w'), help="Specifies the output file")
args = parser.parse_args()
cli = vars(args)
api = scriptsapi(cli['env'],SCALR_URL,SCALR_API_KEY,SCALR_SECRET_KEY)

# print cli

if cli['listscripts'] != None:
    print ('Scripts: ')
    for list in api.listScripts():
        print str(list['id']) + '. ' + list['name']
elif cli['interactive'] != None:
    cmd = scriptscmd.scriptscmd(api)
    cmd.cmdloop()
elif cli['getscript']:
    scriptName = cli['getscript'][0]
    version = cli['getscript'][1]
    if type(version) is int:
        if type(scriptName) is int:
            args.output.write(api.getScriptVersion(scriptName, version)['body'])
        elif type(scriptName) is str:
            args.output.write(api.getScriptVersion(api.getIdFromName(scriptName), version)['body'])
    elif type(version) is str and version=='latest':
        if type(scriptName) is int:
            args.output.write(api.getScriptVersion(scriptName, api.getLatestScriptVersion(scriptName))['body'])
        elif type(scriptName) is str:
            args.output.write(api.getScriptVersion(api.getIdFromName(scriptName), api.getLatestScriptVersion(api.getIdFromName(scriptName)))['body'])

