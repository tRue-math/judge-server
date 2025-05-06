from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'osabie'
    command = 'osabie'
    test_program = """\
"echo: Hello, World!
"""