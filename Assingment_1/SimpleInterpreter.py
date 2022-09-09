# Interpreter for BrainFuck Language
import sys
class BrainFuck:
    def __init__(self, program):
        self.prog = program
        self.p_pointer = 0
        self.memory = [0]
        self.m_pointer = 0
        self.len_prog = len(program)
        self.stack = []

    def interperater(self):

        while self.p_pointer < self.len_prog:
            inst = self.prog[self.p_pointer]
            cell = self.memory[self.m_pointer]

            if inst == '>':
                self.m_pointer += 1
                if self.m_pointer >= len(self.memory):
                    self.memory.append(0)

            elif inst == '<':
                self.m_pointer -= 1
                if self.m_pointer < 0:
                    print("ERROR: invalid cell position. Moved out of tap")
                    sys.exit(0)

            elif inst == '+':
                if cell > 254:
                    self.memory[self.m_pointer] = 0
                else:
                    self.memory[self.m_pointer]  +=1
            
            elif inst == '-':
                if cell < 0:
                    self.memory[self.m_pointer] = 255
                else:
                    self.memory[self.m_pointer] -= 1

            elif inst == '.':
                print(chr(self.memory[self.m_pointer]), end="")
            
            elif inst == ',':
                print("\nOnly first byte will be accepted!")
                user_in = input("Input Requested: ")
                self.memory[self.m_pointer] = ord(user_in[0])

            elif inst == '[':
                self.stack.append(self.p_pointer)
                if cell == 0:
                    count = 1
                    while self.p_pointer < self.len_prog:
                        if count == 0:
                            break

                        self.p_pointer +=1
                        inst = self.prog[self.p_pointer]
                        if inst == ']':
                            count -= 1
                            if self.stack:
                                self.stack.pop()

                        elif inst == '[':
                            count +=1  
                            self.stack.append(self.p_pointer)
                                          
            elif inst == ']':
                if cell == 0:
                    self.stack.pop()
                
                elif self.stack:
                    self.p_pointer = self.stack.pop()-1

            self.p_pointer += 1


f = open('code.txt',"r")
code = f.readline()
print("\nCode in: ",code)
print("\nStart Program:")
interp = BrainFuck(code)
interp.interperater()
print("\nFinal Memory: ", interp.memory)
