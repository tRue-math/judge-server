from dmoj.executors.script_executor import ScriptExecutor

from dmoj.cptbox import TracedPopen
from dmoj.cptbox.filesystem_policies import RecursiveDir
from dmoj.cptbox.handlers import ACCESS_EAGAIN


class MonoTracedPopen(TracedPopen):
    def _cpu_time_exceeded(self) -> None:
        pass

class Executor(ScriptExecutor):
    ext = 'rdr'
    command = 'produire'

    test_program = """\
｢echo: Hello, World!｣を報告
"""
    
    nproc = -1
    address_grace = 262144
    data_grace = 65536
    cptbox_popen_class = MonoTracedPopen
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