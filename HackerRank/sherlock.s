	.file	"sherlock.c"
# GNU C17 (GCC) version 8.1.1 20180502 (Red Hat 8.1.1-1) (x86_64-redhat-linux)
#	compiled by GNU C version 8.1.1 20180502 (Red Hat 8.1.1-1), GMP version 6.1.2, MPFR version 3.1.6-p2, MPC version 1.0.2, isl version none
# GGC heuristics: --param ggc-min-expand=97 --param ggc-min-heapsize=126051
# options passed:  sherlock.c -mtune=generic -march=x86-64 -O2
# -fverbose-asm
# options enabled:  -faggressive-loop-optimizations -falign-labels
# -fasynchronous-unwind-tables -fauto-inc-dec -fbranch-count-reg
# -fcaller-saves -fchkp-check-incomplete-type -fchkp-check-read
# -fchkp-check-write -fchkp-instrument-calls -fchkp-narrow-bounds
# -fchkp-optimize -fchkp-store-bounds -fchkp-use-static-bounds
# -fchkp-use-static-const-bounds -fchkp-use-wrappers -fcode-hoisting
# -fcombine-stack-adjustments -fcommon -fcompare-elim -fcprop-registers
# -fcrossjumping -fcse-follow-jumps -fdefer-pop
# -fdelete-null-pointer-checks -fdevirtualize -fdevirtualize-speculatively
# -fdwarf2-cfi-asm -fearly-inlining -feliminate-unused-debug-types
# -fexpensive-optimizations -fforward-propagate -ffp-int-builtin-inexact
# -ffunction-cse -fgcse -fgcse-lm -fgnu-runtime -fgnu-unique
# -fguess-branch-probability -fhoist-adjacent-loads -fident -fif-conversion
# -fif-conversion2 -findirect-inlining -finline -finline-atomics
# -finline-functions-called-once -finline-small-functions -fipa-bit-cp
# -fipa-cp -fipa-icf -fipa-icf-functions -fipa-icf-variables -fipa-profile
# -fipa-pure-const -fipa-ra -fipa-reference -fipa-sra -fipa-vrp
# -fira-hoist-pressure -fira-share-save-slots -fira-share-spill-slots
# -fisolate-erroneous-paths-dereference -fivopts -fkeep-static-consts
# -fleading-underscore -flifetime-dse -flra-remat -flto-odr-type-merging
# -fmath-errno -fmerge-constants -fmerge-debug-strings
# -fmove-loop-invariants -fomit-frame-pointer -foptimize-sibling-calls
# -foptimize-strlen -fpartial-inlining -fpeephole -fpeephole2 -fplt
# -fprefetch-loop-arrays -free -freg-struct-return -freorder-blocks
# -freorder-blocks-and-partition -freorder-functions -frerun-cse-after-loop
# -fsched-critical-path-heuristic -fsched-dep-count-heuristic
# -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
# -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
# -fsched-stalled-insns-dep -fschedule-fusion -fschedule-insns2
# -fsemantic-interposition -fshow-column -fshrink-wrap
# -fshrink-wrap-separate -fsigned-zeros -fsplit-ivs-in-unroller
# -fsplit-wide-types -fssa-backprop -fssa-phiopt -fstdarg-opt
# -fstore-merging -fstrict-aliasing -fstrict-volatile-bitfields
# -fsync-libcalls -fthread-jumps -ftoplevel-reorder -ftrapping-math
# -ftree-bit-ccp -ftree-builtin-call-dce -ftree-ccp -ftree-ch
# -ftree-coalesce-vars -ftree-copy-prop -ftree-cselim -ftree-dce
# -ftree-dominator-opts -ftree-dse -ftree-forwprop -ftree-fre
# -ftree-loop-if-convert -ftree-loop-im -ftree-loop-ivcanon
# -ftree-loop-optimize -ftree-parallelize-loops= -ftree-phiprop -ftree-pre
# -ftree-pta -ftree-reassoc -ftree-scev-cprop -ftree-sink -ftree-slsr
# -ftree-sra -ftree-switch-conversion -ftree-tail-merge -ftree-ter
# -ftree-vrp -funit-at-a-time -funwind-tables -fverbose-asm
# -fzero-initialized-in-bss -m128bit-long-double -m64 -m80387
# -malign-stringops -mavx256-split-unaligned-load
# -mavx256-split-unaligned-store -mfancy-math-387 -mfp-ret-in-387 -mfxsr
# -mglibc -mieee-fp -mlong-double-80 -mmmx -mno-sse4 -mpush-args -mred-zone
# -msse -msse2 -mstv -mtls-direct-seg-refs -mvzeroupper

	.text
	.p2align 4,,15
	.globl	countLetterMap
	.type	countLetterMap, @function
countLetterMap:
.LFB25:
	.cfi_startproc
	pushq	%r12	#
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	movq	%rdi, %r12	# map, map
	pushq	%rbp	#
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movq	%rsi, %rbp	# string, string
	pushq	%rbx	#
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
# sherlock.c:34:     for(i = 0; i < strlen(string); i++) {
	xorl	%ebx, %ebx	# ivtmp.4
	jmp	.L2	#
	.p2align 4,,10
	.p2align 3
.L3:
# sherlock.c:35:         map[string[i] - 'a'].count += 1;
	movsbq	0(%rbp,%rbx), %rax	# MEM[base: string_14(D), index: ivtmp.4_20, offset: 0B], MEM[base: string_14(D), index: ivtmp.4_20, offset: 0B]
	addq	$1, %rbx	#, ivtmp.4
	addl	$1, -388(%r12,%rax,4)	#, _6->count
.L2:
# sherlock.c:34:     for(i = 0; i < strlen(string); i++) {
	movq	%rbp, %rdi	# string,
	call	strlen	#
# sherlock.c:34:     for(i = 0; i < strlen(string); i++) {
	cmpq	%rbx, %rax	# ivtmp.4, tmp102
	ja	.L3	#,
# sherlock.c:37: }
	popq	%rbx	#
	.cfi_def_cfa_offset 24
	popq	%rbp	#
	.cfi_def_cfa_offset 16
	popq	%r12	#
	.cfi_def_cfa_offset 8
	ret	
	.cfi_endproc
.LFE25:
	.size	countLetterMap, .-countLetterMap
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"Map %c is %d\n"
.LC1:
	.string	"YES"
.LC2:
	.string	"NO"
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB24:
	.cfi_startproc
	pushq	%rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
# sherlock.c:18:     memset(map, 0, sizeof(map));
	xorl	%eax, %eax	# tmp105
	movl	$13, %ecx	#, tmp106
# sherlock.c:13: int main(int argv, char** argc) {
	pushq	%rbx	#
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
# sherlock.c:19:     countLetterMap(map, stringInput);
	xorl	%ebx, %ebx	# ivtmp.18
# sherlock.c:13: int main(int argv, char** argc) {
	subq	$120, %rsp	#,
	.cfi_def_cfa_offset 144
# sherlock.c:16:     char * stringInput = argc[1];
	movq	8(%rsi), %rsi	# MEM[(char * *)argc_7(D) + 8B], stringInput
# sherlock.c:18:     memset(map, 0, sizeof(map));
	movq	%rsp, %rbp	#, tmp112
	movq	%rbp, %rdi	# tmp112, tmp104
	rep stosq
# sherlock.c:19:     countLetterMap(map, stringInput);
	movq	%rbp, %rdi	# tmp112,
	call	countLetterMap	#
	.p2align 4,,10
	.p2align 3
.L7:
# sherlock.c:22:         printf("Map %c is %d\n", i+'a', map[i].count);
	movl	0(%rbp,%rbx,4), %edx	# MEM[symbol: map, index: ivtmp.18_22, step: 4, offset: 0B], MEM[symbol: map, index: ivtmp.18_22, step: 4, offset: 0B]
	leal	97(%rbx), %esi	#, tmp110
	movl	$.LC0, %edi	#,
	xorl	%eax, %eax	#
	addq	$1, %rbx	#, ivtmp.18
	call	printf	#
# sherlock.c:21:     for(i = 0; i < 26; i++) {
	cmpq	$26, %rbx	#, ivtmp.18
	jne	.L7	#,
	movq	%rbp, %rdi	# tmp112, ivtmp.16
	leaq	104(%rbp), %rax	#, _4
# sherlock.c:57:     int offByOne = 0;
	xorl	%edx, %edx	# offByOne
	jmp	.L11	#
	.p2align 4,,10
	.p2align 3
.L8:
	addq	$4, %rdi	#, ivtmp.16
# sherlock.c:58:     for(i = 0; i < 26; i++) {
	cmpq	%rdi, %rax	# ivtmp.16, _4
	je	.L10	#,
.L11:
# sherlock.c:63:                 if(freq - 1 == map[i].count) {
	cmpl	$-1, (%rdi)	#, MEM[base: _3, offset: 0B]
	jne	.L8	#,
# sherlock.c:64:                     if(offByOne++) {
	testl	%edx, %edx	# offByOne
	jne	.L9	#,
	addq	$4, %rdi	#, ivtmp.16
# sherlock.c:58:     for(i = 0; i < 26; i++) {
	cmpq	%rdi, %rax	# ivtmp.16, _4
	je	.L10	#,
# sherlock.c:63:                 if(freq - 1 == map[i].count) {
	cmpl	$-1, (%rdi)	#, MEM[base: _39, offset: 0B]
	je	.L9	#,
	addq	$4, %rdi	#, ivtmp.16
	movl	$1, %edx	#, offByOne
# sherlock.c:58:     for(i = 0; i < 26; i++) {
	cmpq	%rdi, %rax	# ivtmp.16, _4
	jne	.L11	#,
.L10:
# sherlock.c:25:         printf("YES\n");
	movl	$.LC1, %edi	#,
	call	puts	#
.L15:
# sherlock.c:30: }
	addq	$120, %rsp	#,
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	xorl	%eax, %eax	#
	popq	%rbx	#
	.cfi_def_cfa_offset 16
	popq	%rbp	#
	.cfi_def_cfa_offset 8
	ret	
.L9:
	.cfi_restore_state
# sherlock.c:27:         printf("NO\n");
	movl	$.LC2, %edi	#,
	call	puts	#
	jmp	.L15	#
	.cfi_endproc
.LFE24:
	.size	main, .-main
	.text
	.p2align 4,,15
	.globl	compareFrequencies
	.type	compareFrequencies, @function
compareFrequencies:
.LFB26:
	.cfi_startproc
	leaq	104(%rdi), %rcx	#, _14
# sherlock.c:40:     int temp = 0, i = 0;
	xorl	%edx, %edx	# temp
	.p2align 4,,10
	.p2align 3
.L19:
# sherlock.c:43:         if(map[i].count != 0 && temp == 0) {
	movl	(%rdi), %eax	# MEM[base: _17, offset: 0B], <retval>
# sherlock.c:43:         if(map[i].count != 0 && temp == 0) {
	testl	%eax, %eax	# <retval>
	je	.L17	#,
# sherlock.c:43:         if(map[i].count != 0 && temp == 0) {
	testl	%edx, %edx	# temp
	je	.L25	#,
# sherlock.c:48:             return 0;
	xorl	%eax, %eax	# <retval>
.L17:
# sherlock.c:52: }
	ret	
	.p2align 4,,10
	.p2align 3
.L25:
	addq	$4, %rdi	#, ivtmp.31
	movl	%eax, %edx	# <retval>, temp
# sherlock.c:42:     for(i = 0; i < 26; i++) {
	cmpq	%rcx, %rdi	# _14, ivtmp.31
	jne	.L19	#,
# sherlock.c:51:     return 1;
	movl	$1, %eax	#, <retval>
	ret	
	.cfi_endproc
.LFE26:
	.size	compareFrequencies, .-compareFrequencies
	.p2align 4,,15
	.globl	checkValid
	.type	checkValid, @function
checkValid:
.LFB27:
	.cfi_startproc
	leaq	104(%rdi), %rdx	#, _13
# sherlock.c:57:     int offByOne = 0;
	xorl	%eax, %eax	# <retval>
	jmp	.L29	#
	.p2align 4,,10
	.p2align 3
.L27:
	addq	$4, %rdi	#, ivtmp.38
# sherlock.c:58:     for(i = 0; i < 26; i++) {
	cmpq	%rdi, %rdx	# ivtmp.38, _13
	je	.L31	#,
.L29:
# sherlock.c:63:                 if(freq - 1 == map[i].count) {
	cmpl	$-1, (%rdi)	#, MEM[base: _16, offset: 0B]
	jne	.L27	#,
# sherlock.c:64:                     if(offByOne++) {
	testl	%eax, %eax	# <retval>
	jne	.L30	#,
	addq	$4, %rdi	#, ivtmp.38
# sherlock.c:58:     for(i = 0; i < 26; i++) {
	cmpq	%rdx, %rdi	# _13, ivtmp.38
	je	.L31	#,
# sherlock.c:63:                 if(freq - 1 == map[i].count) {
	cmpl	$-1, (%rdi)	#, MEM[base: _12, offset: 0B]
	je	.L26	#,
	addq	$4, %rdi	#, ivtmp.38
	movl	$1, %eax	#, <retval>
# sherlock.c:58:     for(i = 0; i < 26; i++) {
	cmpq	%rdi, %rdx	# ivtmp.38, _13
	jne	.L29	#,
	.p2align 4,,10
	.p2align 3
.L31:
# sherlock.c:71:     return 1;
	movl	$1, %eax	#, <retval>
.L26:
# sherlock.c:72: }
	ret	
.L30:
# sherlock.c:65:                         return 0;
	xorl	%eax, %eax	# <retval>
	ret	
	.cfi_endproc
.LFE27:
	.size	checkValid, .-checkValid
	.ident	"GCC: (GNU) 8.1.1 20180502 (Red Hat 8.1.1-1)"
	.section	.note.GNU-stack,"",@progbits
