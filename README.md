# Clean_Local_Branches_Python
Python script that will prune branches and delete any local branches that do not exist in origin.

## Command
To initiate, simply run command: 
```
$ python %file_directory%/prune.py
```
or run with arguments:
```
$ python %file_directory%/prune.py C:\git\repo
```

## Arguments
1. arg[0] = File location of script.  This is added by default
2. arg[1] = Directory workspace (optional).  Leave blank if script is in local workspace.

## Steps
1. Runs the prune command against origin
2. Gets list of local branches
3. Loops through local branches
4. Checks each local branch against remote to see if it exists
5. If not exists, run delete on local branch

## Exceptions
The script will skip the current branch you are on (*) and the master branch.  This can be adjusted per your liking by the if statements in the for loop.
