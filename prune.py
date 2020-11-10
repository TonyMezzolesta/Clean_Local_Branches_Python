import subprocess
import sys
import os

from argument_reader import PruneArgumentReader


parser = PruneArgumentReader()
directory, dry_run = parser.get_parsed()

if directory is not None:
    print(directory)
    os.chdir(directory)

if dry_run:
    print("Running dry run.")

# Prune branches first
subprocess.run(["git", "remote", "update", "--prune"])

local_branches = subprocess.check_output(["git", "branch"])

leftover_branches = []
newline_separator = ",\n"

each_branch = local_branches.splitlines()
# Loop though local branches
for line_local in each_branch:
    current = line_local.decode('utf-8')

    if current[:1] == "*":
        print(f"Skipped current branch: '{current}'")
        leftover_branches.append(current)
        continue

    current = current[2:]  # Remove spacing used for markings

    # Skip master branch
    if "master" in current:
        leftover_branches.append(current)
        continue

    # Check remote repo to see if branch exists
    remote_branch = subprocess.check_output(["git", "ls-remote", "--heads", "origin", current])

    # Remove it from local if it does not exist on remote
    if not remote_branch:
        if dry_run:
            print(f"(Dry-Run) Removing branch: '{current}'")
        else:
            print(f"Removing branch: '{current}'")
            subprocess.run(["git", "branch", "-D", current])
        continue
    else:
        leftover_branches.append(current)

print(f"""
-------------------------
    process completed
-------------------------

Started with {len(each_branch)} branches. Remaining {len(leftover_branches)} branches: 
{newline_separator.join(leftover_branches)}
""")
