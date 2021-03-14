SublimeLinter-contrib-pwsh
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-pwsh.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-pwsh)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer) that runs on [pwsh](https://github.com/PowerShell/PowerShell). It will be used with files that have the “PowerShell” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that:
 - `pwsh` is installed on your system (version >=7, [pwsh](https://github.com/PowerShell/PowerShell)).
 - [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer) module is installed. If not, install it:

```powershell
Install-Module -Name PSScriptAnalyzer
```

In order for `pwsh` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## PSScriptAnalyzer settings

If file `.pwshlintrc` exists in user's home directory (PowerShell $HOME variable) it is used as PSScriptAnalyzer's configuration file when calling `Invoke-ScriptAnalyzer`.

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

## TODO

 - Allow specifying [Built-in Presets](https://github.com/PowerShell/PSScriptAnalyzer#built-in-presets) instead of only explicit settings.
 - Add option to change settings' file name and/or location.
