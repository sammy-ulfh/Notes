# Index

- [[#Boot Loaders]]
  - [[#LILO]]
  - [[#GRUB]]
- [[#Next Notes]]

# Boot Loaders

When a computer is turned off, its software (including operating systems, application code, and data) remains stored on non-volatile memory. When the computer is powered on, it typically does not have an operating system or its loader in random-access memory (RAM). The computer first executes a relatively small program stored in read-only memory (ROM), along with a small amount of needed data, to access the nonvolatile device or devices from which the operating system programs and data can be loaded into RAM.

The small program that starts this sequence is known as a bootstrap loader, bootstrap or boot loader. This small program's only job is to load other data and programs which are then executed from RAM. Often, multiple-stage boot loaders are used, during which several programs of increasing complexity load one after the other in a process of chain loading.

# LILO

LILO comes as standard on all distributions of Linux. LILO is older and less powerfull. Originally LILO did not include GUI menu choice.

# GRUB 

GRUB is a bit easier to administer. Command line interface, network boot, MD5 passwords.

- /boot/grub/grub.conf
- /etc/grub.conf

# Next Notes

[[Runlevels]]