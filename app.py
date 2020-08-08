#from androzer import *
import subprocess
from subprocess import PIPE
import os
from flask import Flask, render_template
app = Flask(__name__)



def runall_scans(apkname):
    subprocess.run(["adb", "forward", "tcp:31415", "tcp:31415"], stdout=subprocess.DEVNULL)

    #Creating results directory if not exists
    if os.path.isdir(apkname + '_results') == False:
        os.mkdir(apkname + '_results')

    #Speficy commands to run here    
    commands = [
        'app.activity.info -a', 'app.package.attacksurface', 'app.package.launchintent'
        ]
    dconcon = 'drozer console connect -c "run ' #Initiating command

    #Running them in a loop
    to_return = []
    for command in commands:
        runme = subprocess.Popen([dconcon + command + ' ' + apkname + '"'], stdout=PIPE, universal_newlines=True, shell=True)
        (output, err) = runme.communicate()
        runme.wait()
        
        to_return.append(output)
      
    print(to_return)
    return to_return


@app.route('/')
def index():
    sub_out=runall_scans('com.mwr.example.sieve')
    return render_template('report.html', v1=sub_out[0], v2=sub_out[1], v3=sub_out[2] )


if __name__ == '__main__':
   app.run(debug = True)