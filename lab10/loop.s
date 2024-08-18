.text
 .global _start
 _start:
     MOV R1, #0
     MOV R2, #1
 loop:
     CMP R2, #22
     BGT end
     ADD R1, R1, R2
     ADD R2, R2, #1
     B loop
 end:
     MOV R0, R1
     MOV R7, #1
     SWI 0
