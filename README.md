# CSC 450 Programming Assignment

You are to implement a simulator for a [deterministic push-down accepter/automaton](https://learning.oreilly.com/library/view/an-introduction-to/9781284077254/ch07.html#ch7def3) (dpda), as defined in Section 7.3 of the textbook.



## Specifications

* Elements of the set Q will be indexed by consecutive nonnegative integers starting at 0, and is specified by placing the highest such index in a file named Q.conf.  
* The initial state will always be the one with index 0.
* The set F will be represented by a comma-separated list of element indexes of Q in a file named F.conf
* Elements of the sets &Sigma; and &Gamma; can be any __printable__ Unicode character, excluding things such as newlines, blanks, tabs and spaces.  The sets themselves will be specified by listing the characters desired in files named Sigma.conf and Gamma.conf respectively.
* The __first__ symbol listed in Gamma.conf will be the initial contents of the stack.
* The transition function &delta; will be specified in a file named delta.conf.
Each line of delta.conf will represent one transition.
For non-&lambda; transitions there will be five items on a line: the current state number, the next character on input, the top symbol on the stack, the new state number, and a string of stack symbols to push, terminating with the end of the line.
The five items should be separated by white space (i.e., blanks or tabs).
A &lambda; transition is specified by starting the line with a capital 'L'
followed by the current state, the top symbol on the stack, the new state number, and the string of stack symbols to push.
* The program should allow the user to specify which directory the .conf files are in.
* The input to the dpda will be entered on standard input.
* The program will print to standard output an instantaneous description of the machine before each move. When no more moves are possible the program will print "Accept" or "Reject" to the standard output.

## Notes

* To turn in the assignment, do the following: clone this GitHub repository, create a branch within named with your Mount Union login name, and then when you are ready to turn the project in you will be given permission so that you can push your branch to the repository.
* The program may be written in Java or Python.  You may petition to be allowed another language, but you must get permission in writing beforehand.
* If you are using Java, I recommend using the `Scanner` class for processing input.
* The program should build a transition table and then simulate what a pda would do on the input, keeping track of the current state and the current stack contents, and reading one character at a time from standard input. It will look up in the transition table what the next state should be and the next thing to push onto the stack.
When there are no more input characters, it will see whether the machine is in a final state and print a corresponding message.
*  I leave it to you to decide how the program should let the user specify the directory/folder that holds the configuration files.  For example, if the program has a GUI, then you could use a text box to receive the name of the directory, or you could be a bit fancier and use a file chooser.  If the program is executed from the command line, then you could either have the program prompt for the directory, or&mdash;better yet&mdash;you could allow the directory to be specified as the program's only command-line argument.
* The program should make sure that the specification meets the requirements of a dpda and that the given input string is appropriate for the specified dpda.
* Sample configuration files are given for the deterministic pda of Example 7.10 in the folder named Example7-10-conf.
* Sample test inputs are given in the same folder.

## Grading

Your score will be based on the following rubric:

| Item | Possible score |
|------|---------------:|
| Program is well-designed and documented | 10 |
| Program allows user to specify the directory that the configuration files are in | 10 |
| Program checks for inconsistencies in the configuration/input string | 10 |
| Program prints sequence of instantaneous descriptions for the given input | 10 |
| Program prints the correct message (Accept/Reject) for the given input | 10 |
| At least two separate test machine configurations are provided&mdash;**not** including the one already provided from Example 7.10 | 10 |
| At least 5 separate test inputs for each of the machine configurations are provided | 20 |
| Program executes correctly on all test inputs&mdash;including the one already provided | 20 |
| Total | 100 |

Programming Assignment 3 is due Wednesday, April 17, at class time.
You will turn the assignment in by pushing your branch to GitHub. **Note Well:** this will not be possible until class time of the day that it's due, and it will *only* be possible to do this during class that day.
