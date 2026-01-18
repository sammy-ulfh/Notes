
# Index

- [[#AWK Built-in Variables]]
- [[#Next Notes]]
# AWK Built-in Variables

Awk's built-in variables include the field variables - __$1__, __\$2__, __\$3__, and so on (__\$0__ is the entire line) -- that break a line of text into individual words or pieces called fields.

- __NR__: NR command keeps a current count of the number of input records. Remember that records are usually lines. Awk command performs the pattern/action statements once for each record in a file.
- __NF__: NF command keeps a count of the number of fields within the current input record.
- __FS__: FS command contains the field separator character which is used to divide fields on the input line. The default is "white space", meaning space and tab characters. FS can be reassigned to another character (typically BEGIN) to change the field separator.
- __RS__: RS command stores the current record separator character. Since, by default, an input line is the input record, the default record separator character is a newline.
- __OFS__: OFS command stores the output field separator, which separates the fields when Awk prints them. The default is a blank space. Whenever print has several parameters separated with commas, it will print the value of OFS in between each parameter.
- __ORS__: ORS command stores the output record separator, which separates the output lines when Awk prints them. The default is a newline character. print automatically outputs the content of ORS at the end of whatever it is given to print.

# Next Notes

[[AWK Examples]]