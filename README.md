## Host Status Checker

This tool allows you to perform network scans on a list of specified IP addresses and generate a report containing detailed information about the scanned hosts. The tool utilizes the Nmap scanner to gather information about open ports, services, and potential vulnerabilities on the target hosts.

### Configuration

Before running the tool, make sure to configure the list of IP addresses to scan. Open the `ips.yaml` file located in `/opt/host-status/scripts/config/` and add the desired IP addresses under the 'ips' key.

```yaml
ips:
  - 192.168.1.1
  - 192.168.1.2
  - 192.168.1.3
```

**INSTALLATION**

# 1. Clone the repository

```
git clone https://github.com/your-username/host-status.git
cd host-status
```

# 2. Set permissions

```
chmod +x req
```

# 3. Run dependency installer 

```
sudo ./req
```

# 4. Run the program

```
python3 main.py
```

## Running as a Service

To install the Host Status Checker as a service, download the provided installer and execute it with administrator privileges. This will set up the necessary configurations to run the tool in the background.
Files and Configuration

    main.py: The main script responsible for initiating network scans and generating reports. Configure IP addresses in ips.yaml.
    scripts/mail.py: Generates an MJML template for email reports based on scanned IP addresses.
    scripts/sender.js: Sends email reports using Nodemailer and the configured email credentials.
    scripts/config/ips.yaml: Configuration file for specifying IP addresses to scan.
    scripts/config/credentials.json: Configuration file for email sender credentials.

## Note

Please use this tool responsibly and ensure that you have the necessary permissions to scan and gather information from the specified IP addresses. Unauthorized scanning may violate legal and ethical standards.
