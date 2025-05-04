from typing import List

from dmoj.executors.mono_executor import MonoExecutor

class Executor(MonoExecutor):
    ext = 'produire'
    command = 'produire'

    test_program = """\
｢echo: Hello, World!｣を報告
"""
    syscalls = ['execve','unlink','wait4','clock_nanosleep','fork']

    def get_compile_args(self) -> List[str]:
        command = self.get_command()
        assert command is not None
        assert self._code is not None
        return [command, self._code, f'-out:{self.get_compiled_file()}']