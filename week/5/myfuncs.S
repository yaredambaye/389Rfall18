section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous functions stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov     QWORD [rbp-24], rdi
        mov     eax, esi
        mov     DWORD  [rbp-32], edx
        mov     BYTE  [rbp-28], al
        mov     DWORD  [rbp-4], 0
        jmp     .L2
.L3:
        mov     eax, DWORD [rbp-4]
        cdqe
        add     rax, QWORD [rbp-24]
        movzx   edx, BYTE  [rbp-28]
        mov     BYTE  [rax], dl
        add     DWORD  [rbp-4], 1
.L2:
        mov     eax, DWORD  [rbp-4]
        cmp     eax, DWORD  [rbp-32]
        jl      .L3



        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous functions stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov     QWORD  [rbp-24], rdi
        mov     QWORD  [rbp-32], rsi
        mov     DWORD  [rbp-36], edx
        mov     DWORD  [rbp-4], 0
        jmp     .L2
.L3:
        mov     eax, DWORD  [rbp-4]
        cdqe
        add     rax, QWORD  [rbp-24]
        mov     edx, DWORD  [rbp-4]
        movsx   rdx, BYTE [edx]
        add     rdx, QWORD  [rbp-32]
        movzx   edx, BYTE  [rdx]
        mov     BYTE [rax], dl
        add     DWORD  [rbp-4], 1
.L2:
        mov     eax, DWORD  [rbp-4]
        cmp     eax, DWORD  [rbp-36]
        jl      .L3              

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
