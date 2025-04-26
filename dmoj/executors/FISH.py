from dmoj.cptbox.filesystem_policies import RecursiveDir
from dmoj.executors.script_executor import ScriptExecutor


class Executor(ScriptExecutor):
    ext = 'fish'
    command = 'fish'
    fs = [RecursiveDir('~')]
    test_program = """\
"!dlrow ,olleH"l?!;oe0.
"""
