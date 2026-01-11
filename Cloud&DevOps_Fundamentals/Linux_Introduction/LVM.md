
# Index

- [[#Logical Volume Manager - LVM]]
	- [[#Advantages]]
	- [[#Disadvantages]]
	- [[#overview]]
		- [[#Physical volumes]]
		- [[#Volume groups]]
		- [[#Filesystem creation]]
- [[#Next Notes]]

# Logical Volume Manager - LVM

## Advantages

LVM gives you more flexibility than just using normal hard drive partitions:

- Use any number of disks as one big disk.
- Have logical volumes stretched over several disks.
- Create small logical volumes and resize them __dynamically__ as they get more filled.
- Resize logical volumes regardless of they order on disk. It does not depend on the position of the LV within VG, there is no need to ensure surrounding available space.
- Resize/create/delete logical and physical volumes online. File system on them still need to be resized, but some support online resizing.
- Online/live migration of LV begin used by services to different disks without having to restart services.
- Snapshots allow you to backup a frozen copy of the file system, while keeping service downtime to a minimum.

## Disadvantages

- Linux exclusive (almost). There is no official support in most other OS (FreeBDS, Windows).
- Adittional steps in setting up the system, more complicated.
- If you use Btrfs file system, its Subvolume feature will also give you the benefit of having a flexible layout. In that case, using the adittional Abstraction layer of LVM may be unnecesary. 

![[lvm.png]]

## overview 

The following is summary of the steps to perform to create LVM logical volume:

- Initialize the partition you will use for the LVM volume as physical volumes (this labels them).
- Create a volume group.
- Create a logical volume

After creating the logical volume you can create and mount the file system.

### Physical volumes

__pvcreate__, __pvdisplay__ and __pvscan__ - utilities to initialize and display physical volumes.

```shell
sudo pvcreate /dev/sdb1
```
> Physical volume "/dev/sdb1" successfully created

```shell
sudo pvscan
```
> PV /dev/sda2 VG centos lvm2 \[29.51 GiB / 0 free]
> PV /dev/sdb1 lvm2 \[20 GiB]
> Total: 2 \[49.51 GiB] / in use: 1 \[29.51 GiB] / in no VG: 1 \[20.00 GiB]

```shell
sudo pvdisplay
```
> --- Physical volume ---
> PV Name /dev/sda2
> VG Name centos

### Volume groups

__vgcreate__ - create a volume group.

```shell
sudo vgcreate vg_newlvm /dev/sdb1
# create logical group from sdb1 volume.

sudo vgcreate vg_newlvm /dev/sdb1 /dev/sdc1 /dev/sdc2
# create logical group from multiple volumes.
```

__lvcreate__ - create a logical volume inside logical group.

```shell
sudo lvcreate --name centos7_newvol -l 100%FREE vg_newlvm
# creates a logical volume called cenos7_newvol that uses all of the unllocated space in the volume group vg_newlvm
```

__lvdisplay__ - display a list of logical volumes.

```shell
lvdisplay
--- Logical volume ---
LV Path /dev/vg_newlvm/centos7_newvol
LV Name centos7_newvol
VG Name vg_newlvm
LV UUID szlkNP-0lwe-f59Z-PJVU-X7pG-unBL-qN10D4
LV Write Access read/write
LV Creation host, time centos7.ehowstuff.local, 2015-01-25 15:15:48 +0800
LV Status available # Open 0 LV Size 20.00 GiB Current LE 5119
Segments 1
Allocation inherit
Read ahead sectors auto
```

### Filesystem creation

__mkfs__ - create a filesystem.

```shell
sudo mkfs.ext4 /dev/vg_newlvm/centos7_newvol
# formats a logical volume called centos7_newvol into ext4 filesystem

sudo mkfs.btrfs /dev/vg_newlvm/centos7_newvol
# formats a logical volume called centos7_newvol into btrfs filesystem

sudo mkfs.ntfs /dev/vg_newlvm/centos7_newvol
# formats a logical volume called centos7_newvol into ntfs filesystem
```

# Next Notes

[[Swap]]