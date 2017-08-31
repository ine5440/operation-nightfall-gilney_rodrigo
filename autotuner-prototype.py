#!/usr/bin/python3
# Auto-tuner prototype
# Built for INE5540 robot overlords

import subprocess # to run stuff
import sys # for args, in case you want them
import time # for time


def tuner(argv):
    start = 1
    n = 9
    best_time = 99999
    for value in range(start, n):
        for var in range(4):
            tempo = test(value, var, n)
            if best_time > tempo:
                best_var = var
                index = value
                best_time = tempo
    print()
    print(best_var, " - ", index, " - ", best_time)


def test(value=1, var=0, n=9):
    exec_file = 'matmult'
    compilation_line = ['gcc', '-o', exec_file, 'mm.c']
    steps = ['-DSTEP=' + str(value)]
    flags = ['-O' + str(var)]

    # Compile code
    compilation_try = subprocess.run(compilation_line+steps+flags)
    if (compilation_try.returncode == 0):
        print("Happy compilation - ", value)
    else:
        print("Sad compilation")

    # Run code
    input_size = str(n)
    t_begin = time.time()  # timed run
    run_trial = subprocess.run(['./'+exec_file, input_size])
    t_end = time.time()
    if (run_trial.returncode == 0):
        tempo = t_end-t_begin
        print("Happy execution in "+str(tempo))
        return tempo
    else:
        print("Sad execution")
    return



if __name__ == "__main__":
    tuner(sys.argv[1:]) # go auto-tuner
