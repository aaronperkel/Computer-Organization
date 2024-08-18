.global _start
_start:
MOV R7, #4      @ syscall number
MOV R0, #1      @ stdout
MOV R2, #34     @ string is 34 characters long
LDR R1, =string @ string located at 'string:'
SWI 0

_exit:
MOV R7, #1      @ exit syscall
SWI 0

.data
string:
.ascii "Hello World, this is Aaron Perkel\n"
