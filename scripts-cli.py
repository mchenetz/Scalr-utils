from scriptsapi import scriptsapi
import scriptscmd
import os
import argparse


env = {
    'dc-lab':1
}
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

print cli

if cli['listscripts'] != None:
    print ('Scripts: ')
    for list in api.listScripts():
        print str(list['id']) + '. ' + list['name']

elif cli['interactive'] != None:
    cmd = scriptscmd.scriptscmd(api)
    cmd.cmdloop()



