# Steps to solve with grub

1. Use an arch installer USB to get arch installer terminal.
2. Connect your arch installer terminal to a wifi.
3. Use `lsblk -f` to show the current partitions on your system.
4. Identify /boot (Ex: /dev/nvme0n1p1) and /root (Ex: /dev/nvme0n1p3) partition.
5. Mount each paritition to get system terminal (chroot).
   - `mount /dev/nvme0n1p1 /boot`
   - `mount /dev/nvme0n1p3 /mnt`
6. Execute `arch-chroot /mnt` to get the terminal of the system.
7.  Delete the /var/lib/pacman/db.lck sometimes it's possible that it's blocket the database, if you delete this file, you unlock it.
8. Install the kernel that you are currently using (linux, linux-lts, etc), linux-firmware and linux-headers
	`pacman -Syu linux-lts linux-firmware linux-headers`
9.  Regenerate the initramfs image: `mkinitcpio -P`
10. Update grub configuration: `grub-mkconfig -o /boot/grub/grub.cfg`
11. Finally type exit to get out of chroot and turn off the computer.
12. Turn op without USB Installer and that's it.