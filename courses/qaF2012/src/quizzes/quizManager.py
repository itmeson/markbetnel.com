def checkStatus(filename):
    f = open(filename, 'rU')
    text = f.readlines()
    f.close()
    status = 0 #default is to go to both places
    for line in text:
        if ":donow: no" in line:
            status = 1
    return status


import glob, os, sys

start = sys.argv[1]
ME = sys.argv[2]
THEM = sys.argv[3]

print os.getcwd()
quizzes = glob.glob(start  + 'quizzes/q*.rst')

for q in quizzes:
    if checkStatus(q):
        print q, "going to munge"
        #copy to srcME ->  remove draft status
        newname = q + ".tmp"
        os.system('cp '+ q  + ' ' + newname)
        sedcmd = """sed '/:status: draft/d' """ + newname + " >> " + newname + "2"
        os.system(sedcmd)
        os.rename(newname + "2", 
        #copy to srcTHEM ->remove solutions       

    else:
        os.system("cp " + q  + " ../../srcTHEM/quizzes/")
        print q, "leaving alone"



