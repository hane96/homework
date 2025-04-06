.text

.globl main

main:
################################################################# Q1
la $a0, input_msg1 
li $v0 4 #print input_msg1
syscall

li $v0 5 #save size1 in v0
syscall
add $s0,$v0,$zero #save size1 in s0

li $t0, 0 #counter1 in t0
la $t1, array1 #array starts in t1

loop1:
	beq $t0, $s0, exit1
	la $a0, input_msg2
	li $v0, 4  #print input_msg2
	syscall
	li $v0, 5
	syscall
	sw $v0, ($t1) #save number to array
	addi $t0,$t0,1 #counter++
	addi $t1,$t1,4 #array address + 1 byte
	j loop1 #back to loop1
exit1:
	la $a0, input_msg3
	li $v0 4 #print input_msg3
	syscall
	
	li $v0 5 #save size2 in v0
	syscall
	add $s1,$v0,$zero #save size2 in s1
	
	li $t0, 0 #counter1 in t0
	la $t2, array2 #array starts in t1
	
loop2:
	beq $t0, $s1, exit2
	la $a0, input_msg4
	li $v0, 4  #print input_msg4
	syscall
	li $v0, 5
	syscall
	sw $v0, ($t2) #save number to array
	addi $t0,$t0,1 #counter++
	addi $t2,$t2,4 #array address + 1 byte
	j loop2 #back to loop2
### bubble sort array1
exit2: #s0 s1 =>array_size
	
	li $t0 , 1 #outside_counter
	li $t1 , 1 #inside_counter 
	la $t3,array1 #t3 <- array1
loop3:
	beq $t0,$s0,exit3
	
	loop4:
		beq $t1,$s0,exit4
		lw $t4, ($t3)#arr[i]
		addi $t3,$t3,4 #i++
		lw $t5, ($t3)#arr[i+1]
		slt $t6,$t5,$t4 #t6==1 => swap
		
		addi $t1,$t1,1#counter+1 before swap
		
		beq $t6,1,swap
		
		j loop4
		
	exit4:
	li $t1 , 1 #inside_counter 
	la $t3,array1 #t3 <- array1
	addi $t0,$t0,1
	j loop3
	
swap:
	sw $t4,($t3) ##swap
	addi $t3,$t3,-4
	sw $t5,($t3)
	addi $t3,$t3,4
j loop4	
### bubble sort array2 (same as array1
exit3:

	li $t0 , 1 #outside_counter
	li $t1 , 1 #inside_counter 
	la $t3,array2 #t3 <- array2
loop33:
	beq $t0,$s1,merge
	
	loop44:
		beq $t1,$s1,exit44
		lw $t4, ($t3)#arr[i]
		addi $t3,$t3,4 #i++
		lw $t5, ($t3)#arr[i+1]
		slt $t6,$t5,$t4 #t6==1 => swap
		
		addi $t1,$t1,1#counter+1 before swap
		
		beq $t6,1,swap2
		
		j loop44
		
	exit44:
	li $t1 , 1 #inside_counter 
	la $t3,array2 #t3 <- array1
	addi $t0,$t0,1
	j loop33
	
swap2:
	sw $t4,($t3) ##swap
	addi $t3,$t3,-4
	sw $t5,($t3)
	addi $t3,$t3,4
j loop44		
	
	
merge:	
	la $s3,merged_array #t3 <- merged_array
	la $s4,array1 #s4 <-array1
	la $s5,array2 #s5 <-array2
	li $t0,0 #count (merge)
	li $t1,0 #count (arr1)
	li $t2,0 #count (arr2)
	add $t3,$s0,$s1
	add $s2,$t3,$zero #s2 size of merge array
	loop6:
		beq $t0,$s2,exitt
		
		beq $t1,$s0,input_arr2 #arr1 full
		beq $t2,$s1,input_arr1 #arr2 full
		
		lw $t7,($s4) #t7 <-arr1
		lw $t8,($s5) #t8 <-arr2
		
		slt $t9,$t7,$t8
		beq $t9,1,input_arr1 #if array2 full
		beq $t9,0,input_arr2 #if array1 full
		
		
		back: #after put value in merge array
		addi $t0,$t0,1
		addi $s3,$s3,4
		j loop6
	input_arr1:
		addi $t1,$t1,1
		lw $t7,($s4) #t7 <-arr1
		sw $t7,($s3) #store in merge array
		addi $s4,$s4,4
		
		j back
	input_arr2:
		addi $t2,$t2,1
		lw $t8,($s5)#t8 <-arr2
		sw $t8,($s3)#store in merge array
		addi $s5,$s5,4
		
		j back
	
##output array
exitt:
	li $t0,0
	la $t1,merged_array
	la $a0, output_msg1
	li $v0, 4  #print input_msg4
	syscall
loop5:	
	beq $t0, $s2, exit6
	
	lw $t2, ($t1)
	li $v0, 1
	add $a0, $t2, $zero #print array
	syscall
	la $a0, space
	li $v0, 4 #print space
	syscall
	addi $t1, $t1, 4 #array address +1 byte
	addi $t0, $t0, 1 #counter++
	j loop5 #back to loop3
################################################################# Q1
################################################################# Q2
exit6:
la $a0, newline
li $v0 4 #print newline
syscall

la $a0, input_msg5
li $v0 4 #print input_msg5
syscall

li $v0 5 #save x in v0
syscall
add $s0,$v0,$zero #save x in s0

la $a0, input_msg6
li $v0 4 #print input_msg5
syscall

li $v0 5 #save n in v0
syscall
add $s1,$v0,$zero #save n in s1

add $a0,$s1,$zero #put n in a0
jal pow #jump and link to pow
addi $s2,$v0,0 #get return value to s2
j final #go to output

pow:
	addi $sp, $sp, -8 #2 items
	sw $ra, 4($sp) #save ra
	sw $a0, 0($sp) #save x
	
	slti $t0, $a0, 1 #test if finish
	beq $t0, $zero, ELSE 
	
	addi $v0, $zero, 1 
	addi $sp, $sp, 8 #restore stack
	jr $ra 
	ELSE: 
	addi $a0, $a0, -1 
	jal pow 
	lw $a0, 0($sp) 
	lw $ra, 4($sp) 
	addi $sp, $sp, 8 #restore stack
	mul $v0, $s0, $v0 
	jr $ra 

final:

la $a0, output_msg2
li $v0 4 #print output_msg2
syscall

li $v0, 1
add $a0, $s2, $zero #print s2
syscall

################################################################# Q2	
.data
array1: .space 40
array2: .space 40
merged_array: .space 80
n: .word 0

newline: .asciiz "\n"
space: .asciiz " "
input_msg1: .asciiz "Input first array size :"
input_msg2: .asciiz "Input numbers(first array) :"

input_msg3: .asciiz "Input second array size :"
input_msg4: .asciiz "Input numbers(second array) :"
output_msg1: .asciiz "Merged array : " 

input_msg5: .asciiz "Input x :"
input_msg6: .asciiz "Input n :"
output_msg2: .asciiz "x^n : " 
