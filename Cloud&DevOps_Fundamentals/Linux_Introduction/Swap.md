# Index

- [[#Swap]]
	- [[#Swap files and partitions]]
# Swap

## Swap files and partitions 

__Swap space__ in Linux is used when the amount of physical memory (RAM) is full. If the system needs more memory resources and the RAM is full, inactive pages in memory are moved to the swap space. While swap space can help machines with a small amount of RAM, it should not be considered a replacement for more RAM. Swap space is located on hard drives, which have a slower access time than physical memory. Swap space can be a dedicated swap partitions and swap files. Note that __Btrfs__ does not support swap space.

From the end-user perspective, swap files in versions 2.6.x and later of the Linux Kernel are virtually as fast as swap partitions; the limitation is that swap files should be contiguously allocated on their underlying file system.

To increase performance of swap files, the kernel keeps a map of where they are placed on underlying devices and accesses them directly, thus bypassing the cache and avoiding file system overhead. Regardless, Red Hat recommends swap partition to be used. When residing on HDD's, which are rotational magnetic media devices, one benefit of using swap partition is the ability to place them on contiguous HDD areas that provide higher data throughput or faster seek time. 

However, the administrative flexibility of swap files can outweigh certain advantages of swap partitions. For example, a swap file can be placed on any mounted file system, can be set to any desired size, and can be added or changed as needed. Swap partitions are not as flexible; they cannot be enlarged without using partitioning or volume management tools, which introduce various complexities and potential downtimes.