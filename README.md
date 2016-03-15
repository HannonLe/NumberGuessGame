# Number Guess Game

## Introduction

*A* small __number guessing game__.
    
In the beginning of the game, a random n-digit number is randomly generated. The number satisfies:

1. n = 10
2. repetition allowed
3. may start with zeros


Now the player can make a guess on what the number is, and a result like "pAqB" will be given.

For example, suppose now we are playing a n = 4 game. A number "5789" was generated. We make a guess "5678" and get a result "1A2B". That means our guess has __one digit with both number and location correct__ (the first digit "5"), and two digits with __number correct and location incorrect__ ("7" and "8").

Then we can make further guess on the number.
The game is over when the player makes the right guess.



## update log

### 20160314

* The initial version was created in late 2015. This is the first upload.
* This is also a small test of applying HTML syntax into Markdown file.
* More features of number guessing game will be added later.
* Failure. Writing in Markdown gives HTML output. So we don't want to include HTML in Markdown.