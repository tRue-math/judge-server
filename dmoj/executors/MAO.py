from dmoj.executors.script_executor import ScriptExecutor

from typing import List

class Executor(ScriptExecutor):
    ext = 'mao'
    command = 'mao'
    test_program = """\
::echo: Hello, World!
"""

    syscalls = ['vfork', 'clock_nanosleep']