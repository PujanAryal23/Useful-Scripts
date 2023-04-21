import paramiko
import argparse

# Define command-line arguments
parser = argparse.ArgumentParser(description='Remove a directory on a remote machine')
parser.add_argument('hostname', type=str, help='The hostname of the remote machine')
parser.add_argument('username', type=str, help='The username for SSH authentication')
parser.add_argument('password', type=str, help='The password for SSH authentication')
parser.add_argument('directory', type=str, help='The directory to remove on the remote machine')

args = parser.parse_args()

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote machine
ssh.connect(args.hostname, username=args.username, password=args.password)

# Execute the command to remove the directory with sudo
command = f'sudo rm -r /home/ubuntu/workspace/{args.directory}'
stdin, stdout, stderr = ssh.exec_command(command)

# Enter the sudo password if prompted
if 'sudo' in stderr.read().decode():
    stdin.write(args.password + '\n')
    stdin.flush()

# Print the output and errors (if any)
print(stdout.read().decode())
print(stderr.read().decode())

# Close the SSH connection
ssh.close()
