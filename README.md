Hi!  Welcome to "Should You Contribute"!

This is a proof-of-concept site meant to help people decide if they should contribute
to projects -- and give me practice using jQuery and making API calls.  :)

The main limitation right now is that unauthenticated users can only query the GitHub
API 60 times an hour.  Since each use requires a half dozen API calls, this thing runs
out of juice pretty quickly.

This means you have three options!

1.  Wait an hour.  Boring!
2.  Fork the repository, change the name so it matches the user or organization name it was
forked to, and wait a few minutes for github to display the page at $username.github.io.  This
should allow you to get a new set of 60 requests per hour.  :)
3.  Clone the repository to your desktop.  In "contribute.js", in the function makeCorsRequest,
after the xhr.open lines, add the line:
<pre>xhr.setRequestHeader("Authorization", "Basic " + btoa($githubusername+ ":" + $githubpassword))</pre>

If you choose the third option _remember to remove the information_ before pushing any changes
back to GitHub!

#### Contributing

You are welcome to submit changes to this repository, although I can't make any promises with
regard to how quickly I'll respond to pull requests, issues, etc.

If you do submit changes, please also add a test or tests!
