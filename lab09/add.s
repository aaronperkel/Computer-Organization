.global _start
_start:
MOV R1, #5
MOV R2, #6
MOV R3, #7
ADDS R0, R1, R2
ADDS R0, R0, R3
MOV R7, #1
SWI 0
