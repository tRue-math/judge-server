from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'osabie'
    command = 'osabie'
    test_program = """\
"echo: Hello, World!
"""
    nproc = -1
    address_grace = 5000000
    data_grace = 1000000
    syscalls = ['execve','wait4','memfd_create','ftruncate','socketpair','setsid','pselect6',
                'timerfd_settime','readv','getsockopt']