# __Scalr-utils__
---
##  This repo will contain various scripts related to [Scalr.com](https://www.scalr.com).

### **scriptsapi.py** - This API includes functionality that will allow you to work with scripts within Scalr. Take a look at the example.py for usage.

### **scripts-cli.py** - Main CLI - See direction below

### **scriptcmd.py** - Interactive Console Commands for Scipting CLI. Launched by scripts CLI

## Direction ##
---
### Launch: ###
`scripts-cli.py --env [environment] [action]`

Example:

`scripts-cli.py --env 1 -in`

The above launches an interactive console.

`scripts-cli.py --env 1 -gs [Scriptname or ID] [Version or latest] [output file or '-' for stdout]`

`scripts-cli.py --env 1 -gs rundeck-install latest rundeck.sh`

The above will get a specific script version to a file or standard output.

`scripts-cli.py`

The above line will display all CLI options

# Import and Export #
### There is now the ability to import and export all scripts from a Scalr environment ###

`scripts-cli.py --env 1 -ex [directory]`

The above line will export all scripts to the specified directory

`scripts-cli.py --env 1 -im [directory]`

The above line will import the previously exported scripts from the specified directory.

**Note:** All script imports create a new version


## Config File ##

---
The config file can be placed in the program directory or your home directory

File: .scalr.cfg

```
[Scalr]
key: [Scalr key]
secret: [Scalr secret]
url: [http://Scalr URL]
```
