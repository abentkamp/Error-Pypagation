import shlex, subprocess


def plot(quantity_pairs, sym_functions, unit_system, show=True):
    plotfile = 'tmp/gnuplot_tmp.plt'


    code = r'''
reset
set term pngcairo enhanced
set output '%(output)s'
#set xlabel
#set ylabel
%(varDef)s
%(function)s
%(fit)s
%(plot)s
%(printParams)s
'''

    with open(dataFile,'w') as f:
        f.write(data)

    proc=subprocess.Popen(shlex.split('gnuplot '+plotfile))
    proc.communicate()


"""
import subprocess as s
import os
import time


f=open("gnutest","w")
gp = s.Popen(["gnuplot"],stdout=s.PIPE)
time.sleep(1)
gp.stdout.write(bytes('m=2','UTF-8'))
gp.stdout.write(bytes('print m','UTF-8'))
#print(gp.stdout.read())
time.sleep(1)
#print(gp.stdout.read())
gp.terminate()
"""
"""
import subprocess
proc = subprocess.Popen(['gnuplot','-p'],
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE
                        )
proc.stdin.write(b'set term pngcairo\n')
proc.stdin.write(b'set xrange [0:10]; set yrange [-2:2]\n')
image=proc.communicate(b'plot sin(x)\nquit\n')
"""
#print("test")
#image = proc.stdout.readline()
#proc.communicate(b'quit\n')
#print("test2")

#image_file = open('output.png', 'w')
#for line in image:
#    if isinstance(line,bytes):
#        image_file.write(str(line+b"\n"))
#image_file.close()
