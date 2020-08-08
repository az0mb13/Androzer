import subprocess
import os

portfw = subprocess.run(["adb", "forward", "tcp:31415", "tcp:31415"], stdout=subprocess.DEVNULL)

def runall_scans(apkname):
    commands = ['app.activity.info -a', 'app.package.attacksurface', 'app.package.launchintent']
    #console connect
    for command in commands:
        os.system('drozer console connect -c "run ' + command + " " + apkname + '"')

def main():
    print('test')
    runall_scans('com.mwr.example.sieve')

if __name__ == "__main__":
    main()