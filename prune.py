import subprocess
import sys
import os

#sys.argv[0] = script location
#sys.argv[1] = working directory (optional)
if len(sys.argv) >= 2:
    print(sys.argv[1])
    os.chdir(sys.argv[1])

#prune branches first
subprocess.run(["git", "remote", "update", "--prune"])

localbranches = subprocess.check_output(["git", "branch"])
#remotebranches = subprocess.check_output(["git", "branch", "-r"])

#loop though local branches
for lineLocal in localbranches.splitlines():
    #skip the current branch you are sitting on
    if lineLocal[:1].decode('utf-8') == "*":
        #on current branch, dont delete it
        print("skipping current branch")
        continue

    #skip master branch
    if "master" in lineLocal.decode('utf-8'):
        print("skipping local master branch")
        continue

    #check remote repo to see if branch exists
    remoteBranch = subprocess.check_output(["git", "ls-remote", "--heads", "origin", lineLocal[2:].decode('utf-8')])

    #remove it from local if it does not exist on remote
    if not remoteBranch:
        print(lineLocal.decode('utf-8'))
        subprocess.run(["git", "branch", "-D", lineLocal[2:].decode('utf-8')])
        continue

print("completed process")
