import cmd
import sys


class scriptscmd(cmd.Cmd):
    def __init__(self, api, completekey='tab', stdin=None, stdout=None):
        cmd.Cmd.__init__(self, completekey='tab', stdin=None, stdout=None)
        self.api = api
        self.prompt = 'Scalr>'
        self.intro = 'Script Console\nBy Michael Chenetz\n--------------'

    def help_list(self):
        print ('Lists All Scripts')
        print ('cmd: list')

    def do_list(self, null):
        print ('Scripts: ')
        for list in self.api.listScripts():
            print str(list['id']) + '. ' + list['name']

    def help_getscript(self):
        print('Get latest version of a script')
        print('cmd: getscript')
        print('cmd: getscript [Script ID]')
        print('cmd: getscript [Script Name]')

    def do_getscript(self, cmd):
        if not cmd:
            self.do_list(self)
            cmd = input('Select Scripts: ')
        if cmd:
            if type(cmd) is int:
                print(self.api.getScriptVersion(cmd, self.api.getLatestScriptVersion(cmd))['body'])
            elif type(cmd) is str:
                print(self.api.getScriptVersion(self.api.getIdFromName(cmd), self.api.getLatestScriptVersion(self.api.getIdFromName(cmd)))['body'])

    def help_exit(self):
        print ('Exits application')

    def do_exit(self, null):
        sys.exit(0)

    def postloop(self):
        print ('Goodbye')