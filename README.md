# Number Guess Game

## Introduction

<p style="font-size: 20px; font-family: Times">
	<span style="color:red; font-size:26px">*A*</span> small __number guessing game__.
    
    In the beginning of the game, a random n-digit number is randomly generated. The number satisfies:
</p>

<ol style="font-size: 20px; font-family: Times">
    <li>n $\leqslant$ 10</li>
    <li>repetition allowed</li>
    <li>may start with zeros</li>
</ol>

Now the player can make a guess on what the number is, and a result like "pAqB" will be given.

For example, suppose now we are playing a n = 4 game.
A number "5789" was generated.
We make a guess "5678" and get a result "1A2B".
That means our guess has <span style="font-size:22px">__one digit with both number and location correct__</span> (the first digit "5"), and two digits with <span style="font-size:22px">__number correct and location incorrect__</span> ("7" and "8").

Then we can make further guess on the number.
The game is over when the player makes the right guess.


## update log

### 20160314

* The initial version was created in late 2015. This is the first upload.
* This is also a small test of applying HTML syntax into Markdown file.
* More features of number guessing game will be added later.