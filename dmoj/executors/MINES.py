from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'mines'
    command = 'mines'
    test_program = """\
***.*..
*..**..
****...
3,0 #push4
2,1 #push6
6,2 #push6
1,1 #push7
3,0 #sub
3;0 #in(c)
5,0 #dup
2;1 #out(c)
5,2 #positive
1;1 #skip
4,2 #push3, exit
4;2 #flag, swap
5;2 #reset(r)
"""

    syscalls = ['mkdir','execve']