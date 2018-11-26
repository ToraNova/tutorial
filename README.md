This is a tutorial repo to study and learn how to use
github as a version control tool effectively from a local computer.

git init
initializes a repo .git dir

git clone <repo/url>
clones a git repo onto a directory with the repo name

git pull <repo/url> <branch>
attempts to sync the repo, requires git init to be run first
different historical data (i.e different repos that has nothing in common)
cannot be pulled. (use a clone instead)

git push <repo/url> <branch>
sends a commit to an existing repo, this requires a git commit to be issued
first to actually update any change

git commit -m <message>
registers a 'commit' under the user found in git config --list

git config --list
use it with --global to edit global configurations

git remote add <name> <repo/url>
creates an alis for the url, allows for faster pushing via the alias
	git remote show <name>
	shows information regarding the alias

git branch <branchname>
adds a new branch, see --help for more information
