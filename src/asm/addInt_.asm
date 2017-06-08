	.model flat,c

	.code

addInt_  proc
	push ebp
	mov  ebp,esp

	mov  eax,[ebp+8]
	add  eax,[ebp+12]

	pop  ebp
	ret
addInt_  endp
	end