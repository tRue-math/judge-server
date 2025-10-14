from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'mao'
    command = 'mao'
    test_program = """\
::
"""

    syscalls = ['vfork', 'clock_nanosleep']