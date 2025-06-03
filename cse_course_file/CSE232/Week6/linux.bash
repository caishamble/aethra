#!/bin/bash

echo "Basic Linux Operations"

# 1. File and Directory Operations
echo "Listing files in the current directory:"
ls

echo "Changing to home directory:"
cd ~

echo "Current directory:"
pwd

echo "Creating a new directory called 'test_directory':"
mkdir test_directory

echo "Navigating into 'test_directory':"
cd test_directory

echo "Creating an empty file 'file.txt':"
touch file.txt

echo "Listing files in 'test_directory':"
ls

echo "Removing 'file.txt':"
rm file.txt

echo "Navigating back to the home directory:"
cd ~

# 2. File Permissions and Ownership
echo "Changing permissions of 'test_directory' to 755:"
chmod 755 test_directory

echo "Listing directory with detailed information:"
ls -l test_directory

# 3. Searching for Files and Content
echo "Searching for files named 'file.txt' in the home directory:"
find ~ -name "file.txt"

# 4. File Compression and Archiving
echo "Creating a file and compressing it:"
touch file1.txt file2.txt
tar -czvf archive.tar.gz file1.txt file2.txt

echo "Extracting the archive:"
tar -xzvf archive.tar.gz

echo "Cleaning up archive and files:"
rm file1.txt file2.txt archive.tar.gz

# 5. Process Management
echo "Listing current processes:"
ps aux | head -10

# 6. Disk Usage and System Information
echo "Displaying disk usage:"
df -h | head -5

echo "Displaying memory usage:"
free -h

echo "Displaying system uptime:"
uptime

# 7. User Management
echo "Displaying current user:"
whoami

# 8. Package Management (for Debian-based systems)
echo "Updating package lists (requires sudo):"
sudo apt update

echo "Upgrading packages (requires sudo):"
sudo apt upgrade -y

# 9. Network Operations
echo "Pinging google.com to check network connectivity:"
ping -c 3 www.google.com

echo "Displaying network interfaces:"
ifconfig

# 10. Scripting and Automation
echo "Creating a simple 'Hello World' script:"
echo -e "#!/bin/bash\n echo 'Hello, World!'" > hello.sh
chmod +x hello.sh
./hello.sh

# 11. System Shutdown and Reboot (commented out to avoid accidental shutdowns)
#echo "Shutting down the system in 1 minute:"
#sudo shutdown -h +1

#echo "Rebooting the system in 1 minute:"
#sudo reboot

echo "Basic Linux operations completed!"
