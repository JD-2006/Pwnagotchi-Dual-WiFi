import subprocess
import re

def generate_psk_from_command(ssid, passphrase):
    try:
        # Run the wpa_passphrase command and get the PSK
        command = f"sudo wpa_passphrase \"{ssid}\" \"{passphrase}\""
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

        # Extract the PSK from the command output using regular expression
        psk_match = re.search(r'psk=(\S+)', result.stdout)
        
        if psk_match:
            psk = psk_match.group(1)

            # Check if the entry already exists in the configuration file
            with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'r') as config_file:
                existing_entries = config_file.read()

            if psk not in existing_entries:
                # Append the new entry to the configuration file
                with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a') as config_file:
                    config_file.write(result.stdout)
                return True
            else:
                print(f"Duplicate entry found for SSID: {ssid}")
                return False
        else:
            print(f"Error: 'psk=' line not found in the output:\n{result.stdout}")
            return False

    except subprocess.CalledProcessError as e:
        # PSK generation failed, print error and return False
        print(f"Error generating PSK: {e}")
        return False
    except subprocess.CalledProcessError as e:
        # PSK generation failed, print error and return False
        print(f"Error generating PSK: {e}")
        return False
    except subprocess.CalledProcessError as e:
        # PSK generation failed, print error and return False
        print(f"Error generating PSK: {e}")
        return False

def process_line(line):
    parts = line.strip().split(':')
    if len(parts) >= 4:
        ssid = parts[2]
        passphrase = parts[3]
        
        # Use wpa_passphrase command to generate PSK and update configuration file
        success = generate_psk_from_command(ssid, passphrase)
        
        if success:
            print(f"PSK generated and configuration updated for SSID: {ssid}")
        else:
            print(f"Failed to generate PSK for SSID: {ssid}")

if __name__ == "__main__":
    with open('/home/pi/wpa-sec.cracked.potfile', 'r') as file:
        lines = file.readlines()

    for line in lines:
        process_line(line)
