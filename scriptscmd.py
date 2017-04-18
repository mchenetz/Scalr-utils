import cmd
import sys
from scriptsapi import scriptsapi

class scriptscmd(cmd.Cmd):
    def __init__(self, api, completekey='tab', stdin=None, stdout=None):
        cmd.Cmd.__init__(self, completekey='tab', stdin=None, stdout=None)
        self.api = api
        self.prompt = 'Scalr>'

    def help_list(self):
        print ('Lists All Scripts')

    def do_list(self, null):
        print ('Scripts: ')
        for list in self.api.listScripts():
            print str(list['id']) + '. ' + list['name']

    def do_getscript(self, null):
        self.do_list(self)
        cmd = input('Select Scripts: ')
        print(self.api.getScriptVersion(cmd, self.api.getLatestScriptVersion(cmd))['body'])

    def postloop(self):
        print