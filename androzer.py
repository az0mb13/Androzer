import subprocess
from subprocess import PIPE
import os

portfw = subprocess.run(["adb", "forward", "tcp:31415", "tcp:31415"], stdout=subprocess.DEVNULL)

def gen_report():
    print()

def runall_scans(apkname):

    #Creating results directory if not exists
    if os.path.isdir(apkname + '_results') == False:
        os.mkdir(apkname + '_results')

    #Speficy commands to run here    
    commands = [
        'app.activity.info -a', 'app.package.attacksurface', 'app.package.launchintent'
        ]
    dconcon = 'drozer console connect -c "run ' #Initiating command

    #Running them in a loop
    for command in commands:
        runme = subprocess.Popen([dconcon + command + ' ' + apkname + '"'], stdout=PIPE, universal_newlines=True, shell=True)
        (output, err) = runme.communicate()
        runme.wait()
        print(output)

        #Report generation
        gen_report()

def main():
    runall_scans('com.mwr.example.sieve')

if __name__ == "__main__":
    main()