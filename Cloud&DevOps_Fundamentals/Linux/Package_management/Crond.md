# Index

- [[#Crond]]
  - [[#Crontab syntax]]
  - [[#EDIT]]
  - [[#EXAMPLES]]
  - [[#Online generator]]
- [[#Next Notes]]

# Crond

__cron__ - daemon to execute scheduled commands

cron \[ -n | -p | -s | -m ]

cron -x \[ext,sch,proc,pars,load,misc,test,bit]

Cron should be started from __/etc/rc.d/init.d__ or __/etc/init.d__

Cron searches __/var/spool/cron__ for crontab files which are named after accounts in /etc/passwd; The founded crontabs are loaded into memory. Cron also searches for __/etc/anacrontab__ and the files in the __/etc/cron.d__ directory. which are in a different format. Cron examines all stored crontabs, checking each command to see if it should be run in the current minute.

When executing commands, any output is mailed to the owner of the crontab (or to the user named in the MAILTO environment variable in the crontab, if such exists). Job output can also be sent to syslog by using the -s option.

## Crontab syntax

![[cron-script.png]]

## EDIT

To add or update job in crontab, use bellow command. It will open crontab file in the editor where a job can be added/updated

`crontab -e`

By default, it will edit crontab entries of current logged in user. To edit other user crontab use command as bellow

`crontab -u username -e`

Crontab (cron table) is a text file that specifies the schedule of cron jobs. There are two types of crontab files. The system-wide crontab files and individual user crontab files.

Users crontab files are stored by the user's name, and their location varies by operating systems. In Red Hat based system such as CentO, crontab files are stored in the __/var/spool/cron__ directory while on Debian and Ubuntu files are stored in the __/var/spool/cron/crontabs__ directory. Although you can edit the user crontab files manually, it is recommended to use the crontab command.

__/etc/crontab__ and the files inside the __/etc/cron.d__ directory are system-wide crontab files that can be edited only by the system administrators.

In most Linux distributions you can also put scripts inside the __/etc/cron.{hourly,daily,weekly,monthly}__ directores and the scripts will be executed every hour/day/week/month.

### EXAMPLES

1. Schedule a cron to execute at 2am daily
   `0 2 * * * /bin/sh backup.sh`
2. Schedule a cron to execute twice a day
   `0 5,17 * * * /scripts/script.sh`
3. Schedule a cron to execute on every minutes
   `* * * * * /scripts/script.sh`
4. Schedule a cron to execute on every Sunday at 5 PM
   `0 17 * * sun /scripts/script.sh`
5. Schedule a cron to execute on every 10 minutes
   `*/10 * * * * /scripts/script.sh`
6. Schedule a cron to execute on selected months
   `* * * jan,may,aug * /scripts/script.sh`
7. Schedule a cron to execute on selected days
   `0 17 * * sun,fri /scripts/script.sh`
8. Schedule a cron to execute on first sunday of every month
   `0 2 * * sun [$(date+%d) -le 07] && /scripts/script.sh`
9. Schedule a cron to execute every four hours
   `0 */4 * * * /scripts/script.sh`
10. Schedule a cron to execute twice on every Sunday and Monday
    `0 4,17 * * sun,mon /scripts/script.sh`
11. Schedule a cron to execute on every 30 seconds
    `* * * * * sleep 30; /scripts/script.sh`
12. Schedule a multiple tasks in single cron
    `* * * * * /scripts/script.sh; /scripts/script2.sh`
## Online generator

You can practice by using an [online generator](https://crontab.guru/).

# Next Notes

[[JAVA (OpenJDK)]]