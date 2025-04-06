
.text

.globl main

main:
la $a0, input_msg1 
li $v0 4 #print input_msg1
syscall

li $v0 5 #save n in v0
syscall
add $s0,$v0,$zero #save n in s0

li $t0, 0 #counter1 in t0
la $t1, array #array starts in t1

loop1:
	beq $t0, $s0, loop2
	la $a0, input_msg2
	li $v0, 4  #print input_msg2
	syscall
	li $v0, 5
	syscall
	sw $v0, ($t1) #save number to array
	addi $t0,$t0,1 #counter++
	addi $t1,$t1,4 #array address + 1 byte
	j loop1 #back to loop1

loop2:	
	beq $t0, $zero, exit
	subi $t1, $t1, 4 #array address -1 byte
	lw $t2, ($t1)
	li $v0, 1
	add $a0, $t2, $zero #print array
	syscall
	la $a0, space
	li $v0, 4 #print space
	syscall
	
	subi $t0, $t0, 1 #counter--
	j loop2 #back to loop2
	
exit:
la $a0, newline
li $v0, 4 
syscall

la $a0, small_3rd
li $v0, 4 
syscall

la $t1, array
li $t0, 0 #counter
li $t2, 99997 #smallest
li $t3, 99998 #2nd
li $t4, 99999 #3rd

finding:
	beq $t0,$s0,exit2
	lw $t5, ($t1)#get num
	slt $t6,$t5,$t4 #t6 is true value
	beq $t6,1,check1
	j counter_plus
	
check1:
	slt $t6,$t5,$t3
	beq $t6,1,check2
	
	add $t4,$t5,$zero
	j counter_plus	
check2:
	slt $t6,$t5,$t2	
	beq $t6,1,check3
	
	add $t4,$t3,$zero
	add $t3,$t5,$zero
	j counter_plus
check3:
	add $t4,$t3,$zero
	add $t3,$t2,$zero
	add $t2,$t5,$zero
	j counter_plus
	

counter_plus:
	addi $t0,$t0,1
	addi $t1,$t1,4
	j finding
	
	
exit2:	
li $v0, 1
add $a0, $t4, $zero
syscall

la $a0, newline
li $v0, 4 #print space
syscall

la $a0, big_3rd
li $v0, 4 
syscall


j exit3
#

exit3:
la $t1, array
li $t0, 0 #counter
li $t2, -99997 #biggest
li $t3, -99998 #2nd
li $t4, -99999 #3rd
j finding3

finding3:
	beq $t0,$s0,exit4
	lw $t5, ($t1)#get num
	slt $t6,$t5,$t4 #t6 is true value
	beq $t6,0,check4
	j counter_plus2
	
check4:
	slt $t6,$t5,$t3
	beq $t6,0,check5
	
	add $t4,$t5,$zero
	j counter_plus2	
check5:
	slt $t6,$t5,$t2	
	beq $t6,0,check6
	
	add $t4,$t3,$zero
	add $t3,$t5,$zero
	j counter_plus2
check6:
	add $t4,$t3,$zero
	add $t3,$t2,$zero
	add $t2,$t5,$zero
	j counter_plus2
	

counter_plus2:
	addi $t0,$t0,1
	addi $t1,$t1,4
	j finding3
	
	
exit4:	
li $v0, 1
add $a0, $t4, $zero
syscall


#	
.data
array: .space 40
n: .word 0

small_3rd: .asciiz "3rd smallest: "
big_3rd: .asciiz "3rd biggest: "
newline: .asciiz "\n"
input_msg1: .asciiz "Input n(array size) :"
space: .asciiz " "
input_msg2: .asciiz "Input numbers :"
output_msg: .asciiz "Output :" 