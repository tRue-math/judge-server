from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'fish'
    command = 'fish'
    test_program = """\
"!dlroW ,olleH :ohce"l?!;oa:+0.
"""

    syscalls = ['vfork', 'clock_nanosleep']