# Index

- [[#Alternatives]]
- [[#Next Notes]]

# Alternatives

__alternatives__ creates, removes, maintains and displays information about the symbolic links comprising the __alternatives of software__, that is installed on the system, __like several versions of java, python, ruby, nodejs__, etc.

__SYPNOSIS__:

- alternatives \[Options] --install link name path priority \[--slave link name path]... \[--initscript service
- alternatives \[Options] --remove name path
- alternatives \[Options] --set name path
- alternatives \[Options] --auto name
- alternatives \[Options] --display name
- alternatives \[Options] --config name

```
# alternatives --install /usr/bin/java java /usr/java/latest/bin/java 5
# alternatives --config java
There are 5 programs which provide 'java'.
 Selection Command
-----------------------------------------------
   1           /usr/lib/jvm/jre-1.4.2-gcj/bin/java
   2           /usr/java/jre1.6.0_13/bin/java
   3           /usr/java/jre1.6.0_18/bin/java
*+ 4           /usr/lib/jvm/jre-1.6.0-openjdk.x86_64/bin/java
   5           /usr/java/latest/bin/java
Enter to keep the current selection[+], or type selection number: 5
# java -version
java version "1.6.0_26"
Java(TM) SE Runtime Environment (build 1.6.0_30)
Java HotSpot(TM) 64-Bit Server VM (build 20.1-b02, mixed mode)
```

# Next Notes

[[Service Management in Linux]]