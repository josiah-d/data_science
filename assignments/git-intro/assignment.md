# Intro to git and Github

## Introduction

 #### Note: `Master` used to be the standard for the `main` branch.  `Main` is now becoming the new standard.  There is currently a transition going on so know whenever people refer to a `master` branch they are talking about the `main` branch

The `haiku.txt` file is supposed to contain haikus, preferably of the data 
science variety.  However, `haiku.txt` is an empty file presently.

A haiku is a three-line poem with seventeen syllables, written in a 5/7/5 syllable
count, though liberty is often taken with both these requirements.  It's derived
from Japanese poetry.

A couple examples:

```
An old silent pond...
A frog jumps into the pond,
splash! Silence again.
```
-- Matsuo Basho
<br>
<br>
```
Nightfall,
Too dark to read the page
Too cold.
```
-- Jack Kerouac

Parts I - III of this assignment are done individually.  In Part IV you'll pick a partner and work with them.

## Basic

### Part 1: Modify the history of a repository and save it
1. Fork then clone this repo locally.
2. Add your own haiku to `haiku.txt`
3. Add, commit, and push it to your forked Github repo.  When you commit it, use a message like "first haiku", i.e. `$ git commit -m "first haiku"`
4. View `haiku.txt` on your Github and verify that it has been updated.  Verify that you see the commit message on Github.


### Part 2: Further modify the history, then revert to an old version (an old commit)
1. Open up your `haiku.txt` file again and add another haiku underneath the first one.
2. Add, commit, and push it.  When you commit it, use a different message than the first, e.g. `$ git commit -m "second haiku"`
3. Verify that the modified file and the second commit message are visible on your Github.
4. At this time, you should have added two commits to this repository.  View the commits to the history of the repository using [git log](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History).  Note that the repository has more commits than just yours (Galvanize has modified it since its creation).  If you just want to see the last 2 commits, type `$ git log -2`
5. Note the **hash** (the long sequence of characters) that follows the word 'commit' for each of your commits.  This is the unique identifier for the state of the respository at that commit. The commit that you are presently using is called the `HEAD`. Luckily, you don't need to write down all those characters and remember them to reference each commit.  Try this command: `git log --oneline -2`.  You should be seeing the same commits, and the **first seven characters of the hash that uniquely identify the commit**.
6. You've decided that you don't like your second haiku.  So you want to switch back to the commit that only had your first haiku using `$ git checkout`. See an example of `git checkout` usage to switch to an older commit in this [blog post](https://opensource.com/life/16/7/how-restore-older-file-versions-git) in the **Restore a file** section. After checkout, make sure you add, commit, and push it so that the old version is contained in the current HEAD of the project. 
7. FYI, there's often more than one way to do things:  check out the use of `$ git reset` and `$ git revert` [here](https://stackabuse.com/git-revert-to-a-previous-commit/).

### Part 3: Using branches
In software development, often the code associated with the version that is being used commercially is in the `main` branch.  If you were to modify that code and add and commit it, it may break a currently deployed piece of software, upsetting users and the company.  To safeguard against this, you make a new **branch**, say `dev` (short for development), and work in that instead of the `main` branch. Then, when you are ready, you can **merge** the `dev` branch into the `main` branch so that the main branch incorporates the new development effort.  

So, what is a **branch** in git?  As shown in Figure 11 [in this blog](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell), a branch is simply a pointer to a commit.  In Figure 11, the `main` branch points to commit `f30ab` (which points to commit `34ac2`, which points to `98ca9` etc.). `HEAD` in Figure 11 points to `main`, signifying which branch the user is presently working on.  Figure 12 shows the addition of another branch (called `testing`) that also points to commit `f30ab`.  In Figure 13, the `testing` branch exists but the user is still on the `main` branch (as indicated by `HEAD`), while in Figure 14 the user has switched to the `testing` branch.  Figure 15 indicates that in the `testing` branch the user has done some work and added and commited it, so that the `testing` branch is now 1 commit ahead of `main`.
1. Replicate this process for your haikus (a `haiku-dev` branch?) using git commands in the [blog](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell), starting at the **Creating a New Branch** section.  
2. Add and commit a new haiku on your `haiku-dev` branch.  You can push this branch to Github using [this syntax](https://stackoverflow.com/questions/2765421/how-do-i-push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too).  Go to your Github and verify that your new branch exists there, too.
3. You like the haiku you made in the `haiku-dev` branch.  You think it should be included in the haikus that you present on the `main` branch.  So you want to **merge** it into main. As explained in step-by-step detail in this [blog](https://stackabuse.com/git-merge-branch-into-master/), the steps are to 1) make sure you are on the `main` branch using `$ git checkout main`, then 2) merge the branch you created (`haiku-dev`) into main using `git merge haiku-dev`.
4. After material in branches has been merged into main, it's considered best practice to delete the branch locally and remotely (on Github).  Locally: `$ git branch -d localbranchname`, remotely (Github): `$ git push origin --delete remotebranchname`.  Do yourself a favor and keep your branch names consistent locally and on Github (don't call it `haiku-dev` locally and `haiku-development` on Github).

## Advanced

### Part 4: Git with a partner
There's a [Git quick reference guide in the reference folder.](https://github.com/GalvanizeDataScience/git-intro/blob/master/reference/Git.pdf) There's a section on pair programming.  Even though you're pair "haikuing" at this point, it should help with the steps below.  
1. Pick a partner to write some haiku with you. For now, decide to work out of the `main` branch.
2. Decide whose repo to work out of.  Call this person `A`.  `A` will need to add the other (`B`)
   as a collaborator on `A's` repo.  [Here's how.](https://help.github.com/articles/inviting-collaborators-to-a-personal-repository/)
3. `B` needs to add `A's` repo as a remote in `B`'s repo.  [Here's how.](https://help.github.com/articles/adding-a-remote/)
4. Now take turns writing lines of haiku.  Only one person should be typing at a time on his/her laptop. Generally the steps should be:
   * `git pull ...`
   * type some haiku...
   * `git add ...`
   * `git commit ...`
   * `git push ...`
   * ...and then other person starts with `git pull ...` <br>
   You should both be pushing and pulling to the *same* repository.  Otherwise it would be hard to collaborate, neh?  For one person it will be `origin`, for the other it will the name they give that person's remote.  See the Git quick reference guide for more on this.
5. If you run into a Merge Conflict (and you should), resolve it.  [Here's how.](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/)
6. Merge conflicts can be a pain.  This could have been avoided if each person that was writing haikus branched off of main, wrote their haikus, and then the branches with the new haikus were sequentially merged into main.  This is how you'll be working in git on case studies.
