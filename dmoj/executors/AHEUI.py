from dmoj.executors.script_executor import ScriptExecutor


class Executor(ScriptExecutor):
    ext = 'aheui'
    command = 'aheui'
    test_program = """\
밯뻬뵛봣놰댜햬차뮇
"""

    syscalls = ['vfork', 'clock_nanosleep']