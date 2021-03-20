from SublimeLinter.lint import Linter
import os.path
import re
import logging
from base64 import b64encode

logger = logging.getLogger('SublimeLinter.plugins.PSScriptAnalyzer')

class PSScriptAnalyzer(Linter):
    analyzer_cmd_template = (
        'Invoke-ScriptAnalyzer -Settings:{0} -ScriptDefinition ($INPUT | Out-String) | '
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
        'selector': 'source.powershell',
        'settings': None
    }
    def cmd(self):
        settings = self.analyzer_settings() or '$false'
        logger.info("PSScriptAnalyzer settings: " + settings)
        analyzer_cmd = self.analyzer_cmd_template.format(settings)
        return [
            'pwsh',
            '-NoProfile',
            '-OutputFormat',
            'Text',
            '-EncodedCommand',
            b64encode(analyzer_cmd.encode('utf_16_le')).decode('ascii')
        ]
    def analyzer_settings(self):
        settings = self.settings['settings']
        if settings:
            if re.match(r'^[\w-]+$', settings):
                return settings
            settings = os.path.expandvars(settings)
        else:
            settings = os.path.join(
                os.path.expanduser("~"),
                'PSScriptAnalyzerSettings.psd1'
            )
        return settings if os.path.isfile(settings) else None
    def split_match(self, match):
        result = super().split_match(match)
        if result.rule:
            result.message += ' (Rule: {0})'.format(result.rule)
        return result
