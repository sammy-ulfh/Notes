# Index

- [[#Swap]]
	- [[#Swap files and partitions]]
	- [[#Swappiness]]
	- [[#Swap size]]
	- [[#Adding swap as an LVM logical volume]]
	- [[#Creating a swap file]]
	- [[#Removing a swap file]]
- [[#Next Notes]]
# Swap

## Swap files and partitions 

__Swap space__ in Linux is used when the amount of physical memory (RAM) is full. If the system needs more memory resources and the RAM is full, inactive pages in memory are moved to the swap space. While swap space can help machines with a small amount of RAM, it should not be considered a replacement for more RAM. Swap space is located on hard drives, which have a slower access time than physical memory. Swap space can be a dedicated swap partitions and swap files. Note that __Btrfs__ does not support swap space.

From the end-user perspective, swap files in versions 2.6.x and later of the Linux Kernel are virtually as fast as swap partitions; the limitation is that swap files should be contiguously allocated on their underlying file system.

To increase performance of swap files, the kernel keeps a map of where they are placed on underlying devices and accesses them directly, thus bypassing the cache and avoiding file system overhead. Regardless, Red Hat recommends swap partition to be used. When residing on HDD's, which are rotational magnetic media devices, one benefit of using swap partition is the ability to place them on contiguous HDD areas that provide higher data throughput or faster seek time. 

However, the administrative flexibility of swap files can outweigh certain advantages of swap partitions. For example, a swap file can be placed on any mounted file system, can be set to any desired size, and can be added or changed as needed. Swap partitions are not as flexible; they cannot be enlarged without using partitioning or volume management tools, which introduce various complexities and potential downtimes.

## Swappiness

Swappiness is a Linux kernel parameter that controls the relative weight given to swapping out of runtime memory, as opposed to dropping pages from the system page cache, whenever a memory allocation request cannot be met from "free" memory. Swappiness can be set to values between 0 and 100 inclusive. A low value causes the kernel to prefer to evict pagesfrom the page cache; a higher value causes the kernel to prefer to swap out "cold" memory pages. 

The default value is 60; setting it higher will increase overall throughput (particularly disk IO) at the risk of occasional high latency if cold pages need to be swapped back in, while setting it lower (even 0) may provide more consistently low latency. Certainly the default values work well in most workloads, but desktops and interactive systems with more than adequate RAM for any expected task may want to lower the setting while batch processing and less interactive systems may want to increase it.

[swap size configuration](https://docs.redhat.com/en/documentation/Red_Hat_Enterprise_Linux/7/html/Storage_Administration_Guide/ch-swapspace.html)

## Swap size

| Amount of RAM in the system | Recommended swap space     | Recommended swap space if allowing for hibernation |
| --------------------------- | -------------------------- | -------------------------------------------------- |
| <= 2 GB                     | 2 times the amount of RAM  | 3 times the amount of RAM                          |
| > 2 GB - 8 GB               | Equal to the amount of RAM | 2 times the amount of RAM                          |
| > 8 GB - 64 GB              | At least 4 GB              | 1.5 times the amount of RAM                        |
| > 64 GB                     | At least 4 GB              | Hibernation not recommended                        |
Official recomendaction:
https://docs.redhat.com/en/documentation/Red_Hat_Enterprise_Linux/7/html/Storage_Administration_Guide/ch-swapspace.html

Swap space is located on hard drives, which have a slower access time than physical memory.

Swap space can be:

- A dedicated swap partition
- A swap file
- A combination of swap partitions and swap files

To check if swap is activated, you can run:

```shell
cat /proc/swaps
free -h
```

## Adding swap as an LVM logical volume

To add a swap volume group 2 GB in size, assuming /dev/VolGroup00/LogVol02 the swap volume you want to add:

1. Create the LVM2 logical volume of size 2 GB:
   ```shell
	   lvcreate VolGroup00 -n LogVol02 -L 2G
	 ```

2. Format the new swap space
   ```shell
	   mkswap /dev/VolGroup00/LogVol02
	 ```

3. Add the following entry to the /etc/fstab file:
   ```shell
	   /dev/VolGroup00/LogVol02 swap swap defaults 0 0
	 ```

4. Regenerate mount units so that your system registers the new configuration:
   
   ```shell
	   systemctl daemon-reload
	 ```

5. Activate swap on the logical volume:
   ```shell
		swapon -v /dev/VolGroup00/LogVol02
	 ```  

## Creating a swap file

1. Determine the size of the new swap file in megabytes and multiply by 1024 to determinate the number of blocks. For example, the block size of a 64 MB swap file is 65536.
2. Create an empty file, replacing count with the value equal to the desired block size 

	```shell
		dd if=/dev/zero of=/swapfile bs=1024 count=65536
	```

3. Set up the swap file with the command:
   
   ```shell
	   mkswap /swapfile
	 ```

4. Change the security of the swap file so it is not world readable:
   
   ```shell
		chmod 0600 /swapfile
     ```

5. To enable the swap file at boot time, edit /etc/fstab as root to include the following entry:
   
   ```shell
		/swapfile swap swap defaults 0 0
     ```

6. Regenerate mount units so that your system registers the new /etc/fstab configuration:
   ```shell
	   systemctl daemon-reload
     ```
     
7. To activate the swap file immediately:
   ```shell
	   swapon /swapfile
     ```
8. To test if the new swap file was successfully created and activated, inspect active swap space. 


## Removing a swap file

To remove a swap file:

1. At a shell prompt, execute the following command to disable the swap file (where /swapfile is the swap file)
   ```shell
	   swapoff -v /swapfile
     ```
2. Remove its entry from the /etc/fstab file.
   ```shell
	   vi /etc/fstab
     ```
3. Regenerate mount units so that your system registers the new configuration
   ```shell
	   systemctl daemon-reload
     ```
4. Remove the actual file 
```shell
	rm /swapfile
```

# Next Notes

[[Disk Quotas]]