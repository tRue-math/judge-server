from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'backhand'
    command = 'backhand'
    test_program = """io"""

    syscalls = ['vfork', 'clock_nanosleep']