from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'fernando'
    command = 'fernando'
    test_program = """\
1 1
0 1 1 0 0 1 0 1
0 1 1 0 0 0 1 1
0 1 1 0 1 0 0 0
0 1 1 0 1 1 1 1
0 0 1 1 1 0 1 0
0 0 1 0 0 0 0 0
0 1 0 0 1 0 0 0
0 1 1 0 0 1 0 1
0 1 1 0 1 1 0 0
0 1 1 0 1 1 0 0
0 1 1 0 1 1 1 1
0 0 1 0 1 1 0 0
0 0 1 0 0 0 0 0
0 1 0 1 0 1 1 1
0 1 1 0 1 1 1 1
0 1 1 1 0 0 1 0
0 1 1 0 1 1 0 0
0 1 1 0 0 1 0 0
0 0 1 0 0 0 0 1
"""

    syscalls = ['vfork', 'clock_nanosleep']