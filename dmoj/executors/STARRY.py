from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'starry'
    command = 'starry'
    test_program = """\
                                                                                                          + .
                                                                                                        + .
                                                                                                             + .
                                                                                                                    + .
                                                               + .
                                     + .
                                                                             + .
                                                                                                          + .
                                                                                                                 + .
                                                                                                                 + .
                                                                                                                    + .
                                                 + .
                                     + .
                                                                                            + .
                                                                                                                    + .
                                                                                                                       + .
                                                                                                                 + .
                                                                                                         + .
                                      + .
"""

    syscalls = ['vfork', 'clock_nanosleep', 'eventfd2']