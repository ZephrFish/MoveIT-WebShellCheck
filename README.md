# MoveIT-WebShellCheck

This Python script checks specific URLs (`http|https://<host>/human2.aspx`) on a list of hosts and prints out a result depending on the HTTP response code it receives. It prints "compromised" if it receives a 404 status code, "exploit not present" if it receives a 302 status code, and reports an unexpected status code for all other codes.

The list of hosts can be provided as a file (with one host per line) or a single host can be provided directly. The script can optionally write the output to a specified file as well as print it to the console.

## Requirements
- Python 3
- requests library installed in Python
  
## Usage
There are two ways to provide input to the script:

- -f or --file: Specify a file containing a list of hosts (one per line)
- -s or --single: Specify a single host
  
Additionally, you can use -o or --output to specify an output file. If you don't specify an output file, the script will print to the console but not write to any file.

For example, to check a list of hosts provided in a file named hosts.txt and write the output to a file named output.txt, you would use the following command:

```
python MoveITCheck.py -f hosts.txt -o output.txt
```
  
To check a single host (example.com) and write the output to a file named output.txt, you would use the following command:
  
```
python MoveITCheck.py -s example.com -o output.txt
```
If you want to print the result to the console and not write to any file, you can omit the -o option:
  
```
python MoveITCheck.py -s example.com
````
