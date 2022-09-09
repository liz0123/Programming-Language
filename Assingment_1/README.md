## BrainFuck

### Background

Brainfuck is a esteric programming languages created by Urban Müller in 1993 in an attempt to create a language 
with the smallest possible compiler. It consist of eight simple commands: <, >, +, -, [, ], . and ,. 
Which can get quite confussing due to the massive amount of code needed to execute a simple 
program or task. 


### Character Meaning
Each command consists of a single character:
```
1. '>' increment the data pointer (to point to the next right cell in memory).
2. '<' decrement the data pointer (to point to the next left cell in memory).
3. '+' increment the value in the memory cell by 1.
4. '-' decrement the value in the memory cell by 1.
5. '.' output the current cell in memory.
6. ',' accept one byte of input to storing in the current cell.
7. '[' if the current cell is zero, the instruction pointer will jump to the matching ']' (think while loop) 
8. ']' if the current cell is nonzero, jump back to the matching '[' in the instructions. 
```
## About Interpreter

This is a simple interpreter created with Python 3 on Visual Studio Code.

##### Things To Keep in Mind:
- All memory cells will start at zero
- Any characters not listed above will be ignored by the interpretor and be treated like comments
- Loops can be nested as many times as you like and any brackets with out a match will be ignored (but please check your instructions!) 

### Examples

#### Move Value
This code increases the first cell to 3 and moves that value two cells to the right:
```
+++>>[-]<<[->>+<<]
```

This code can be translated as:
```
Code:   Pseudo code:
+++     Increase value of cell 0 by 3
>>      Move the pointer to cell 2
[-]     Set cell 2 to 0 
<<      Move the pointer back to cell 0
[       While cell 0 is not 0
  -       Subtract 1 from cell 0
  >>      Move the pointer to cell 2
  +       Add 1 to cell 2
  <<      Move the pointer back to cell 0
]       End while
```

#### Print Hello World
This program will print "Hello World!"
```
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```

This is a slightly more complex program to print "Hello World!". It'll lower cell values below zero, so it's great to trigger bugs

```
>++++++++[-<+++++++++>]<.>>+>-[+]++>++>+++[>[->+++<<+++>]<<]>-----.>->
+++..+++.>-.<<+[>[+>+]>>]<--------------.>>.+++.------.--------.>+.>+.
```



