from scriptsapi import scriptsapi
import os
import argparse

env = {
    'dc-lab':1
}
SCALR_API_KEY = os.environ['SCALR_API_KEY']
SCALR_SECRET_KEY = os.environ['SCALR_SECRET_KEY']
url = os.environ['SCALR_URL']

## init API with environment
api = scriptsapi(env['dc-lab'],url,SCALR_API_KEY,SCALR_SECRET_KEY)

args = argparse.ArgumentParser(prog='scripts-cli',description='Scalr Scripting CLI')
args.add_argument('--env', required=True, help='Scalr Environment')
action = args.add_mutually_exclusive_group()
action.add_argument('--listScripts', help='Lists all Scalr Scripts', action='store_const', const=True)
cli = vars(args.parse_args())

print cli

if cli['listScripts'] != None:
    print ('Scripts: ')
    for list in api.listScripts():
        print str(list['id']) + '. ' + list['name']
