<h1>BrainFuck-Interpreter</h1>
<p>A simple BrainFuck Interpreter in Python created using Visual Studio Code.</p>


<p>Brainfuck was created by Urban Müller in 1993 in an attempt to create a language 
with the smallest possible compiler. The compiler for this language takes only 240 bytes 
and it achieves this by only using eight simple commands: <, >, +, -, [, ], . and ,
</p>
Despite the simplicity of the Brainfuck lexicon, it is one of the most confusing programming 
languages out there due to the massive amount of code needed to execute a simple 
program or task.

<h2>Commands</h2>

Each commands consist of a single charaacter:

#### Character Meaning

1. <p> > increment the data pointer (to point to the next right cell in memory).</p>
2. <p> < decrement the data pointer (to point to the next left cell in memory).</p>
3. <p> '+' increment the data pointer by 1.</p>
4. <p> '-' decrement the data pointer by 1.</p>
5. <p> . output the current pointed cell in memory.</p>
6. <p> , accept one byte of input to storing in memory.</p>
7. <p> [  if the current cell is zero, the instruction pointer will jump to the matching ] (think while loop) </p>
8. <p> ] if the current cell is nonzero, jump back to the matching ] in the instructions. </p>
