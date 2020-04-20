# dirwatcher
Objective:
Create a long running program
Demonstrate signal handling
Demonstrate program logging
Use exception handling to keep the program running
Create and structure your own code repository using best practices
Show that you know how to read a set of requirements and deliver on them, asking for clarification if anything is unclear.
Goal
For this assessment you will create your own small long-running program named `dirwatcher.py`.  This will give you experience in structuring a long-running program, which will help you with the SlackTweet project later on. The `dirwatcher.py` program should accept some command line arguments that will instruct it to monitor a given directory for text files that are created within the monitored directory.  Your `dirwatcher.py` program will continually search within all files in the directory for a 'magic' string which is provided as a command line argument.  This can be implemented with a timed polling loop.  If the magic string is found in a file, your program should log a message indicating which file and line number the magic text was found.  Once a magic text occurrence has been logged, it should not be logged again unless it appears in the file as another subsequent line entry later on.

Files in the monitored directory may be added or deleted or appended at any time by other processes.  Your program should log a message when new files appear or other previously watched files disappear.  Assume that files will only be changed by appending to them.  That is, anything that has previously been written to the file will not change.  Only new content will be added to the end of the file.  You don't have to continually re-check sections of a file that you have already checked.

Your program should terminate itself by catching SIGTERM or SIGINT (be sure to log a termination message).  The OS will send a signal event to processes that it wants to terminate from the outside.  Think about when a sys admin wants to shutdown the entire computer for maintenance with a `sudo shutdown` command.  If your process has open file handles, or is writing to disk, or is managing other resources, this is the OS way of telling your program that you need to cleanup, finish any writes in progress, and release resources before shutting down.

NOTE that handling OS signals and polling the directory that is being watched are two separate functions of your program.  You won't be getting an OS signal when files are created or deleted.

Success Criteria
Use all best-practices that have been taught so far: docstrings, PEP8, unit tests, clean and readable code and meaningful commit messages.
Have a demonstrable OS signal handler
Log messages for files with magic text
Handle and log different exceptions such as file-not-found, directory-not-exist as well as handle and report top-level unknown exceptions so that your program stays alive.
Include a startup and shutdown banner in your logs and report the total runtime (uptime) within your shutdown log banner.  Please see the hints below if you don't understand what a logging banner is.


Useage: The user can call this program from the command line with several parameters: .txt, .log, -i, --int:, -e, --ext: extension of text file to watch. Time interval between each scan in seconds, Dir: directory to monitor magicword: the word to search for inside of the file

eg. python dirwatcher.py --ext .log --int 2 directory magicword