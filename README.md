SublimeLinter-contrib-PSScriptAnalyzer
======================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-PSScriptAnalyzer.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-PSScriptAnalyzer)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [PowerShell](https://github.com/PowerShell/PowerShell)'s [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer) module. It will be used with files that have the “PowerShell” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that:
 - `pwsh` is installed on your system ([PowerShell Core](https://github.com/PowerShell/PowerShell)).
 - Module [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer) is installed. If not, install it from PowerShell:

```powershell
Install-Module -Name PSScriptAnalyzer
```

In order for `pwsh` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## PSScriptAnalyzer settings

If a file named `PSScriptAnalyzerSettings.psd1` exists in the user's home directory it's used as PSScriptAnalyzer's settings file when calling `Invoke-ScriptAnalyzer` cmdlet. Please refer to [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer#explicit) for details.

Example `PSScriptAnalyzerSettings.psd1` content:
```
@{
    # Select which diagnostic records to show.
    # Valid values are: ParseError, Error, Warning, Information
    Severity = @('ParseError', 'Error', 'Warning')

    ExcludeRules = @(
        'PSUseApprovedVerbs'
    )

    IncludeDefaultRules = $true
}
```

PSScriptAnalyzer's settings path/name can be customized:

```
    "psscriptanalyzer": {
        // full path
        "settings": "D:\\Scripts\\CustomSettings.psd1"
        // environment variables will be expanded
        "settings": "%SCRIPTS_DIR%\\CustomSettings.psd1"
        // or preset name (beware that linting fails if the name is not a valid preset name)
        "settings": "PSGallery"
        // default - remove or set to null
        "settings": null
    }
```

### General Settings

- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

## TODO

 - Handle the case when given [Built-in Preset](https://github.com/PowerShell/PSScriptAnalyzer#built-in-presets) is not found by PSScriptAnalyzer.
