# __Scalr-utils__
---
##  This repo will contain various scripts related to [Scalr.com](https://www.scalr.com).

### **scriptsapi.py** - This API includes functionality that will allow you to work with scripts within Scalr. Take a look at the example.py for usage.

### **scripts-cli.py ** - Main CLI - See direction below

### **scriptcmd.py ** - Interactive Console Commands for Scipting CLI. Launched by scripts CLI

## Direction ##
---
### Launch: ###
`scripts-cli.py --env [environment] [action]`

Example:

`scripts-cli.py --env 1 -in`

The above launches an interactive console.

`scripts-cli.py`

The above line will display all CLI options

## Config File ##

---
The config file can be placed in the directory with all of the python files or your home directory

File: .scalr.cfg

```
[Scalr]
key: [Scalr key]
secret: [Scalr secret]
url: [http://Scalr URL]
```
