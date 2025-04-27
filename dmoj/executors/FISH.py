from dmoj.cptbox.filesystem_policies import RecursiveDir
from dmoj.executors.script_executor import ScriptExecutor

from typing import List

class Executor(ScriptExecutor):
    ext = 'fish'
    command = 'fish'
    test_program = """\
"!dlroW ,olleH :ohce"l?!;oa:+0.
"""

    syscalls = ['fork', 'vfork', 'clock_nanosleep']

    def get_cmdline(self, **kwargs) -> List[str]:
        command = self.get_command()
        assert command is not None
        assert self._code is not None
        return [command, self._code]