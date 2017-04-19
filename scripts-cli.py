from scriptsapi import scriptsapi
import scriptscmd
import os
from os.path import expanduser
import argparse
import ConfigParser

env = {
    'dc-lab':1
}
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

## init API with environment
api = scriptsapi(env['dc-lab'],SCALR_URL,SCALR_API_KEY,SCALR_SECRET_KEY)

args = argparse.ArgumentParser(prog='scripts-cli',description='Scalr Scripting CLI')
args.add_argument('--env', required=True, help='Scalr Environment')
action = args.add_mutually_exclusive_group()
action.add_argument('-ls','--listscripts', help='Lists all Scalr Scripts', action='store_const', const=True)
action.add_argument('-in', '--interactive', help='Interactive Console', action='store_const', const=True)
cli = vars(args.parse_args())

# print cli

if cli['listscripts'] != None:
    print ('Scripts: ')
    for list in api.listScripts():
        print str(list['id']) + '. ' + list['name']

elif cli['interactive'] != None:
    cmd = scriptscmd.scriptscmd(api)
    cmd.cmdloop()



