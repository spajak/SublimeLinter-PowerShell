from SublimeLinter.lint import Linter
from base64 import b64encode

class pwsh(Linter):
    analyzer_cmd = (
        '$p = Join-Path $HOME ".pwshlintrc"; $p = (Test-Path $p) ? $p : $false;'
        'Invoke-ScriptAnalyzer -Settings:$p -ScriptDefinition ($INPUT | Out-String) | '
        'Select-Object -Property Line,Message,Severity,Column,RuleName | '
        'ConvertTo-Csv -Delimiter "\t" -QuoteFields False | Select-Object -Skip 1;'
    )
    regex = (
        r'(?P<line>\d+)\t(?P<message>[^\t]+)\t'
        r'((?P<error>ParseError|Error)|(?P<warning>Warning|Information))\t'
        r'(?P<col>\d*)\t(?P<rule>[^\t]*)'
    )
    multiline = False
    defaults = {
        'selector': 'source.powershell'
    }
    cmd = [
        'pwsh',
        '-NoProfile',
        '-OutputFormat',
        'Text',
        '-EncodedCommand',
        b64encode(analyzer_cmd.encode('utf_16_le')).decode('ascii')
    ]
    def split_match(self, match):
        result = super().split_match(match)
        if result.rule:
            result.message += ' (Rule: {0})'.format(result.rule)
        return result
