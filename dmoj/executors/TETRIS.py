from typing import Dict, List, Optional, Tuple

from dmoj.cptbox.filesystem_policies import ExactFile, RecursiveDir
from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'tetris'
    command = 'tetris.mjs'
    nproc = -1
    syscalls = [
        'capget',
        'eventfd2',
        'shutdown',
        'pkey_alloc',
        'pkey_free',
        'execve',
    ]
    address_grace = 1048576
    fs=[ExactFile("/dev/stdin")]
    test_program = """
# EOF で終了する(È(unicode:200)以外対応の) cat プログラム例
200:
O:>>>>B
I.A>>
J:>
I:<<<
I.A>>>>
I.A>>>
I.A>>
I.A>
I.A
Z:A<
J:A<<
O.<<<<
-1:
O.
"""

    def get_env(self):
        env = super().get_env()
        # Disable io_uring due to potential security implications
        env['UV_USE_IO_URING'] = '0'
        return env

    def get_fs(self):
        return super().get_fs() + [ExactFile('/usr/lib/ssl/openssl.cnf')]
    
    def get_cmdline(self, **kwargs) -> List[str]:
        command = self.get_command()
        assert command is not None
        return [command, self._code]

    @classmethod
    def get_version_flags(cls, command):
        return ['--version']
