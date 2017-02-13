#How to use Git and GitHub

Git is for managing versions of your files locally, and GitHub is for keeping a synchronized set of files and a record of changes in the cloud.  It's nice to work on stuff locally and then _push_ your changes to the cloud.

1.  Sign up on[GitHub}(http:GitHub.com). This is where your cloud copy or _repo_ will live.
2.  Download, install and set up _Git_ on your computer.  Follow the Git documentation and make sure the command `git status` works and `git config user.name` and `git config user.email` return correct information about your github account.
3.  Navigate in your web browser to the homework url..
      https://github.com/SunJieMing/python-minicamp-homework-2
    and click on _Fork_ in the upper right corner.
4.  Now you have your own copy here:
      https://github.com/your-github-username/python-minicamp-homework-2
5.  While you are in your own copy, copy the URL from the browser for pasting
6.  In terminal or command window, change to the directory where you want to create a new directory for your homework, in Windows it might be `cd \Users\username\Desktop`.
7.  Run this command to create the directory and copy the files from Github..
      `git clone https://github.com/your-github-username/python-minicamp-homework-2`
8.  Change to the new directory..
      `cd python-minicamp-homework-2`
9.  Run this command to start keeping track of your files..
      `git add .`
10.  Create some python files.  You can use your virtual environment wherever you installed it, 
     no need to have it in this version-controlled directory.
11.  Run these commands
         `git add .`
         `git commit -m "some comment about whats new"`
         `git push origin master`
12.  Now you should see your new/changed files on your Github account. 
     