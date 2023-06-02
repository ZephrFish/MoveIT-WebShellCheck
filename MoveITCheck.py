import requests
import argparse

def check_host(host, output_file=None):
    for protocol in ['http', 'https']:
        try:
            response = requests.get(f"{protocol}://{host.strip()}/human2.aspx")
            if response.status_code == 404:
                result = f"{protocol.upper()} {host}: has webshell code present, therefore may be compromised"
            else:
                result = f"{protocol.upper()} {host}: exploit not presentde {response.status_code}"
        except Exception as e:
            result = f"An error occurred while checking {protocol.upper()} {host}: {str(e)}"
        
        print(result)
        
        if output_file:
            with open(output_file, 'a') as f:
                f.write(result + '\n')

def check_file(file_name, output_file=None):
    try:
        with open(file_name, 'r') as file:
            hosts = file.readlines()
            for host in hosts:
                check_host(host, output_file)
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Check hosts for specific response codes.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help='File containing list of hosts')
    group.add_argument('-s', '--single', help='Single host to check')
    parser.add_argument('-o', '--output', help='Output file')
    
    args = parser.parse_args()
    
    if args.file:
        check_file(args.file, args.output)
    elif args.single:
        check_host(args.single, args.output)

if __name__ == "__main__":
    main()
