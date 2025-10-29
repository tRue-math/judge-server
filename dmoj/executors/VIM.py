from typing import List

from dmoj.cptbox.filesystem_policies import RecursiveDir
from dmoj.executors.script_executor import ScriptExecutor
import os

class Executor(ScriptExecutor):
    ext = 'vim'
    command = 'vim-executor'
    test_program = 'ZZ'
    fsize=1000000 # input.txt用に書き込めるバイト数を設定

    def create_files(self, problem_id, source_code, *args, **kwargs) -> None:
      super().create_files(problem_id, source_code)
      self.input_file=self._file("input.txt")
      self.write_fs.append(RecursiveDir(self._dir)) # tmpディレクトリに書き込みを許可

    def get_cmdline(self, **kwargs) -> List[str]:
        command = self.get_command()
        assert command is not None
        return [command, self._code,self.input_file]

    syscalls=['vfork','execve','fchdir','chdir','wait4','pselect6']