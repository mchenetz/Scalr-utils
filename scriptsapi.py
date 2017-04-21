from api.client import ScalrApiClient

import os


class scriptsapi(ScalrApiClient):
    def __init__(self, env, api_url, key_id, key_secret):
        super(scriptsapi, self).__init__(api_url, key_id, key_secret)
        self.env = env

    def getCurrentEnv(self):
        return self.env

    def listEnvironments(self):
        return self.fetch('/api/v1beta0/account/environments/')

    def getIdFromName(self, name):
        scripts = self.fetch('/api/v1beta0/user/{envId}/scripts/'.format(envId=self.env))
        for script in scripts:
            if(script['name'] == name):
                return (script['id'])
        else:
            return 0

    def getScript(self, scriptId):
        return self.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}'.format(envId=self.env, scriptId=scriptId))

    def getScriptByName(self, name):
        return self.getScript(self.getIdFromName(name))

    def getScriptVersion(self, scriptId, scriptVersionNumber):
        return self.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/{scriptVersionNumber}/'.format(envId=self.env, scriptId=scriptId, scriptVersionNumber=scriptVersionNumber))

    def getScriptVersionByName(self, name, scriptVersionNumber):
        return self.getScriptVersion(self.getIdFromName(name), scriptVersionNumber)

    def listScripts(self):
        return self.fetch('/api/v1beta0/user/{envId}/scripts/'.format(envId=self.env))

    def listScriptVersions(self, scriptId):
        return self.fetch('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/'.format(envId=self.env, scriptId=scriptId))

    def listScriptVersionsByName(self, name):
        return self.listScriptVersions(self.getIdFromName(name))

    def getLatestScriptVersion(self, scriptId):
        versions = self.listScriptVersions(scriptId)
        id = 0
        for version in versions:
            id = version['version']
        return id

    def writeScriptVersionsToFile(self, scriptId, directory):
        versions = self.listScriptVersions(scriptId)
        for version in versions:
            path = os.path.join(os.path.abspath(directory), self.getScript(scriptId)['name'] + str(version['version']))
            with open(path, 'w') as write:
                write.writelines(version['body'])
                write.close()

    def writeScriptVersionsByNameToFile(self, name, directory):
        self.writeScriptVersionsToFile(self.getIdFromName(name),directory)

    def writeScriptVersionToFile(self, scriptId, scriptVersion, directory):
        version = self.getScriptVersion(scriptId, scriptVersion)
        path = os.path.join(os.path.abspath(directory), self.getScript(scriptId)['name'] + str(version['version']))
        with open(path, 'w') as write:
            write.writelines(version['body'])
            write.close()

    def writeScriptVersionByNameToFile(self, name, scriptVersion, directory):
        self.writeScriptVersionToFile(self.getIdFromName(name),scriptVersion, directory)

    def createScript(self, name, osType):
        json = {
            'name': name,
            'osType': osType
        }
        request = self.post('/api/v1beta0/user/{envId}/scripts/'.format(envId=self.env), json=json)
        return request

    def createScriptVersion(self, script, body):
        if type(script) is int:
            scriptId = script
        if type(script) is str:
            scriptId = self.getIdFromName(script)

        json = {
            'script': scriptId,
            'body': body
        }
        request = self.post('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/'.format(envId=self.env, scriptId=scriptId), json=json)
        return request

    def deleteScript(self, script):
        if type(script) is int:
            request = self.delete('/api/v1beta0/user/{envId}/scripts/{scriptId}/'.format(envId=self.env, scriptId=script))
        if type(script) is str:
            request = self.delete('/api/v1beta0/user/{envId}/scripts/{scriptId}/'.format(envId=self.env, scriptId=self.getIdFromName(script)))
        return request

    def deleteScriptVersion(self, script, scriptVersionNumber):
        if type(script) is int:
            request = self.delete('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/{scriptVersionNumber}/'.format(envId=self.env, scriptId=script, scriptVersionNumber=scriptVersionNumber))
        if type(script) is str:
            request = self.delete('/api/v1beta0/user/{envId}/scripts/{scriptId}/script-versions/{scriptVersionNumber}/'.format(envId=self.env, scriptId=self.getIdFromName(script), scriptVersionNumber=scriptVersionNumber))
        return request