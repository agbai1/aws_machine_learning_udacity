## SOFTWARE ENGINEERING PRACTICES PT I

### Clean and Modular Code
* Production code: software that runs on a production server to handle
data of live users

* Clean Code: Code that is concise, simple, and readable.

* Modular: Breaking code into functions. This encourages code reusability,
better readability, less code writing and efficient collaboration

* Module: file or script that can be reused by encapsulating them into
files that can be imported into other files.


### Refactoring Code
* First produce a working code then go back and clean up and modularize.
* Try to see if there are better ways to change the internal structure
without affecting the external functionality of the program
* Speeds up development time in the long run
* Also a good practice in becoming a better programmer because
you are constantly looking to improve your code.

### Efficient Code
* Reduce run time and executes fasters
* Takes up less space in memory/storage
* Use vector operations over loops when possible
* Know your data structures and which methods are faster

### Why Documentation is important
* Clarifies complex parts of the program
* Navigate code easily
* Describes use and purpose of program
#### Types
* Line level : in-Line
* Function or module level: describes purpose and details
* Project level: Describes project as a whole and how files work together

#### In-line comments
* text followed by hash symbols throughout the code
* helps to explain program where code cannot

#### Docstrings
* Documentation string that explains functionality of all functions in code
*  `""" comment """`
* All functions should have docstrings
* For complicated functions: explain function arguments with `Args:` and what should
be returned using `Returns:`

### Project Documentation
* README is the first step which provides information about what the code does and
sufficient detailed instructions on how to use it
*
