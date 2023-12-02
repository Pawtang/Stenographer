# Stenographer

Stenographer is a note-taking application designed to be portable, hyperlight, and as time-saving as possible.

I began working on Stenographer to enable faster note taking in a business environment. The goal is  to compress common words and phrases and organize notes into a simple common structure to be shared with a team.


# How it Works

When you launch Stenographer, it will ask you for a title input and then begin listening for input.
You can leave the title blank to have the file name be a timestamp.

Notes are input one line at a time - hitting "enter" commits the note to the buffer.

There are special characters that serve certain promotion functions for an entry. The default tags are as follows: 
| Attendees: @        
| Action Item: !
| Key Takeaway: #
| Research Item: -?
| Item Priority: -1, -2, -3, etc...(Can append to any line in addition to tag)

These are processed in descending order of priority -- so a note with a @ tag and a ! tag will only process as an Attendee line.

Ending the session in the terminal with Ctrl+C will expand abbreviations of the strings in the buffer array and arrange them into a text file according to the tags in each string.

library.csv is a simple list of abbreviations and their expansions that Stenographer will recognize in the note text. 

You can clone the repository and modify the library and tags to your hearts content.

