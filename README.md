# CSC 450 Programming Assignment

You are to implement a simulator for a [deterministic push-down automata](https://learning.oreilly.com/library/view/an-introduction-to/9781284077254/ch07.html#ch7def3)
Clone this GitHub repository, create a branch within named with your Mount Union login name, and then when you are ready to turn the project in you will be given permission so that you can push your branch to the repository.


## Specifications

* The set Q will be indexed by consecutive nonnegative integers starting at 0, and is specified by placing the highest such index in a file named Q.conf.
* The set F will be represented by a comma-separated list of elements of Q in a file named F.conf
* Elements of the sets &Sigma; and &Gamma; can be any __printable__ Unicode character, excluding things such as newlines, blanks, tabs and spaces.  
The sets themselves will be specified by listing the characters desired in files named Sigma.conf and Gamma.conf respectively.
* The transition function &delta; will be specified in a file named delta.conf.
Each line of delta.conf will represent one transition.
For non-&lamba; transitions there will be five items on a line: the current state number, the next character on input, the top symbol on the stack, the new state number, and a string of stack symbols to push, terminating with the end of the line.
The five items should be separated by white space (i.e., blanks or tabs).
A &lambda; transition is specified by starting the line with a capital 'L'
followed by the current state, the top symbol on the stack, the new state number, and the string of stack symbols to push.
* The input to the pda will be entered on standard input, and the pda will simply print "Accept" or "Reject" to the standard output.

## Notes

* The program may be written in Java or Python.  You may petition to be allowed another language, but you must get permission in writing beforehand.
* If you are using Java, I recommend using the `Scanner` class for processing input.
* The program should build a transition table and then simulate what a pda would do on the input, keeping track of the current state and the current stack contents, and reading one character at a time from standard input. It will look up in the transition table what the next state should be and the next thing to push onto the stack.
When there are no more input characters, it will see whether the machine is in a final state and print a corresponding message.
* Sample .conf files are given for the deterministic pda of Example 7.10 in the folder named Example7-10-conf.

## Grading

Your score will be based on the following rubric:

| Item | Possible score |
|------|---------------:|
| Blah| 2 |
| Total | 25|

Programming Assignment 3 is due Wednesday, April 17, at class time.
You will turn the assignment in by pushing your branch to GitHub. **Note Well:** this will not be possible until class time of the day that it's due, and it will *only* be possible to do this during class that day.
