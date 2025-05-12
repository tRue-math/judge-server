from typing import List

from dmoj.cptbox.filesystem_policies import ExactFile
from dmoj.executors.compiled_executor import CompiledExecutor

class Executor(CompiledExecutor):
    ext = 'bf'
    command = 'bf-esomer'
    test_program = """,+[-.,+]"""

    syscalls = ['vfork']

    compiler_read_fs = [
        ExactFile('/var/lib/gems/3.3.0/gems/esomer-0.1.0/lib/esomer.rb')
    ]
    compiler_write_fs = [
        ExactFile('/var/lib/gems/3.3.0/gems/esomer-0.1.0/lib/esomer.rb')        
    ]

    def get_compile_args(self) -> List[str]:
        command = self.get_command()
        assert command is not None
        assert self._code is not None
        return [command, self._code]