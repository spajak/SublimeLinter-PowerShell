from SublimeLinter.lint import Linter
from base64 import b64encode

class pwsh(Linter):
    analyzer_cmd = (
        'Invoke-ScriptAnalyzer -ScriptDefinition ($input | Out-String) | '
        'Select-Object -Property Line,Message,Severity,Column,RuleName | '
        'ConvertTo-Csv -Delimiter "\t" -QuoteFields False | '
        'Select-Object -Skip 1'
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
        '-EncodedCommand',
        b64encode(analyzer_cmd.encode('utf_16_le')).decode('ascii')
    ]
    def split_match(self, match):
        result = super().split_match(match)
        if result.rule:
            result.message += ' (Rule: {0})'.format(result.rule)
        return result
