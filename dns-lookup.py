import socket

fqdn_file = open('fqdn-list.txt', 'r')
line = fqdn_file.readline().strip()

fwd_results_file = open('fwd-results.csv', 'w')
rvs_results_file = open('rvs-results.csv', 'w')

print('\n--- Performing fwd lookups --------------')

# write file heading
fwd_results_file.write("FQDN,IP\n")

while line:
    try:
        ip = socket.gethostbyname(line)
        # print(f"{line},{ip}")
        fwd_results_file.write(f"{line},{ip}\n")
    except:
        # print(f"{line},no ip addr")
        fwd_results_file.write(f"{line},no ip addr\n")
    line = fqdn_file.readline().strip()

fqdn_file.close()
fwd_results_file.close()

ip_file = open('ip-list.txt', 'r')
line = ip_file.readline().strip()

print('--- Done with fwd lookups ---------------')

print('\n--- Performing reverse lookups ----------')
# write file heading
rvs_results_file.write("IP,FQDN\n")
while line:
    try:
        fqdn = socket.gethostbyaddr(line)
        # print(f"{line},{fqdn[0]}")
        rvs_results_file.write(f"{line},{fqdn[0]}\n")
    except:
        # print(f"{line},no fqdn")
        rvs_results_file.write(f"{line},no fqdn\n")
    line = ip_file.readline().strip()

ip_file.close()
rvs_results_file.close()

print('--- Done with reverse lookups -----------')