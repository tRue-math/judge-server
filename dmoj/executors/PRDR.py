from dmoj.executors.script_executor import ScriptExecutor

from dmoj.cptbox.filesystem_policies import RecursiveDir
from dmoj.cptbox.handlers import ACCESS_EAGAIN

class Executor(ScriptExecutor):
    ext = 'rdr'
    command = 'produire'

    test_program = """\
｢echo: Hello, World!｣を報告
"""
    
    nproc = -1
    fs = [RecursiveDir('/etc/mono')]
    syscalls = [
        'wait4',
        'rt_sigsuspend',
        'msync',
        'fadvise64',
        'clock_nanosleep',
        ('fork', ACCESS_EAGAIN),
        'execve','fstatfs','chdir'
    ]