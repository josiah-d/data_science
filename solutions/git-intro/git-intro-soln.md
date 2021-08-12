## Solutions for git-intro assignment

### Part I
Modify haiku.txt with a text editor then in terminal:  
`$ git add haiku.txt`  
`$ git commit -m "first haiku"`  
`$ git push origin master`  

### Part II
Add another haiku with your text editor, then:  
`$ git add haiku.txt`  
`$ git commit -m "second haiku"`  
`$ git push origin master`  

See commit history in oneline format:  
`$ git log --online -2`  

Don't like the second haiku, Would rather just reset haiku.txt at the "first haiku" commit.  
Say the hash for "first commit" was `9cad586`  
`$ git checkout 9cad586 haiku.txt`  
`$ git add haiku.txt`  
`$ git commit -m "reset to first haiku"`  
`$ git push origin master`  

### Part III  
Make a `haiku-dev` branch:  
`$ git branch haiku-dev`  
`$ git checkout haiku-dev`  

Add another haiku to haiku.txt.  

Add it to the history.  
`$ git add haiku.txt`  
`$ git commit -m "Add haiku in dev branch"`  

Push branch to Github:  
`$ git push -u origin haiku-dev`

Now merge it into master:  
`$ git checkout master`  
`$ git merge haiku-dev`  
`$ git add haiku.txt`  
`$ git commit -m "additions from haiku-dev"`  
`$ git push origin master`  

Now delete the branch locally and on Github  
`$ git branch -d haiku-dev`  
`$ git push origin --delete haiku-dev`  

### Part IV  
Follow recipe in Git.pdf
