from api.client import ScalrApiClient

import os

class scriptsapi(ScalrApiClient):

    def __init__(self, env, api_url, key_id, key_secret):
        super(scriptsapi, self).__init__(api_url, key_id, key_secret)
        self.env = env

    def getEnv(self):
        return self.env

    def getIdFromName(self, name):
        scripts = self.fetch('/api/v1beta0/user/{envId}/scripts/'.format(envId=self.env))
        for script in scripts:
            if(script['name'] == name):
                return (script['id'])
        else:
            return 0

    def getScript(self, scriptId):
        return self.fetch('/api/v1beta0/user/{envId}/scripts/{scriptid}'.format(envId=self.env, scriptid=scriptId))

    def listScripts(self):
        return self.fetch('/api/v1beta0/user/{envId}/scripts/'.format(envId=self.env))

    def listScriptVersions(self, scriptId):
        return self.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/'.format(envId=self.env, scriptId=scriptId))

    def writeScriptVersionsToFile(self, scriptId, directory):
        versions = self.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/'.format(envId=self.env, scriptId=scriptId))
        for version in versions:
            path = os.path.abspath(directory) + '\\' + self.getScript(scriptId)['name'] + str(version['version'])
            with open(path, 'w') as write:
                write.writelines(version['body'])
                write.close()

