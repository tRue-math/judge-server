from typing import List

from dmoj.executors.compiled_executor import CompiledExecutor

class Executor(CompiledExecutor):
    ext = 'bf'
    command = 'bf-esomer'
    test_program = """,+[-.,+]"""

    syscalls = ['vfork']

    def get_compile_args(self) -> List[str]:
        command = self.get_command()
        assert command is not None
        assert self._code is not None
        return [command, self._code]