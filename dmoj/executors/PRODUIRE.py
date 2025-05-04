from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'produire'
    command = 'produire'

    test_program = """\
｢echo: Hello, World!｣を報告
"""
    syscalls = ['execve','unlink','wait4','clock_nanosleep','fork']