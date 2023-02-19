import nmap
import yaml
import os
import re
import subprocess
import sys

from colorama import Fore
from scripts.mail import mjml

def bot():
    with open('scripts/config/ips.yaml') as f:
        ips_config = yaml.safe_load(f)

    for ip in ips_config['ips']:
        scanner = nmap.PortScanner()
        scanner.scan(ip, arguments='-A -T4')

        with open(f"log/{ip}.yaml", 'w') as f:
            yaml.dump(scanner[ip], f)

        filename = f"log/{ip}.txt"
        with open(filename, 'w') as f:
            for host in scanner.all_hosts():
                f.write(f"Host : {host} ({scanner[host].hostname()})\n")
                f.write(f"Estado : {scanner[host].state()}\n")
                for proto in scanner[host].all_protocols():
                    f.write('----------\n')
                    f.write(f"Protocolo : {proto}\n")

                    lport = list(scanner[host][proto].keys())
                    lport.sort()
                    for port in lport:
                        f.write(f"Puerto : {port}\tEstado : {scanner[host][proto][port]['state']}\tServicio: {scanner[host][proto][port]['name']}\tVersion : {scanner[host][proto][port]['version']}\n")

                        service_name = scanner[host][proto][port]['name']
                        search_term = f"{service_name} {scanner[host][proto][port]['version']}"
                        search_results = subprocess.run(['searchsploit', '-w', search_term], capture_output=True, text=True)
                        if search_results.stdout:
                            vulnerabilities = re.findall(r'CVE-\d{4}-\d{4}', search_results.stdout)
                            if vulnerabilities:
                                f.write(f"La versión {scanner[host][proto][port]['version']} en el puerto {port} es vulnerable:\n")
                                for vuln in vulnerabilities:
                                    f.write(f" - {vuln}\n")

        print(f"Se han registrado los resultados del escaneo para la IP {ip} en el archivo {filename}.")


def main():
    try:
        print(Fore.RED + "IPS A ESCANEAR" + Fore.RESET)

        with open('scripts/config/ips.yaml') as f:
            ips = yaml.load_all(f, Loader=yaml.FullLoader)

            for ip in ips:
                for k, v in ip.items():
                    print(k, "->", v)

        scan = input("Continuar? [s/n]: ")

        if "s" in scan:
            bot()
            mjml()
        else:
            sys.exit(1)

    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()