#read fiel from input
import subprocess
import sys

try:
    
    domain = sys.argv[1]
    File =  sys.argv[2]
    data = open(File, "r")
    lines = data.readlines()
    for line in lines:
        cname = line.strip()
        result = subprocess.run(['dig', cname +'.'+ domain, 'cname', '+short' ], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        if (len(out) != 0):
            print("(+){0}.{1} ==> (+){2}".format(line.strip(),domain,out))

except Exception as e:
    print(e)
