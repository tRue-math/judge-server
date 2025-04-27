from dmoj.cptbox.filesystem_policies import RecursiveDir
from dmoj.executors.script_executor import ScriptExecutor

from typing import List

class Executor(ScriptExecutor):
    ext = 'fish'
    command = 'fish'
    test_program = """\
"!dlrow ,olleH"l?!;oe0.
"""

    syscalls = ['vfork']

    def get_cmdline(self, **kwargs) -> List[str]:
        command = self.get_command()
        assert command is not None
        assert self._code is not None
        return [command, self._code]