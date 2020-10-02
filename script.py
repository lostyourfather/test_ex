with open(input('type a file name'), 'r') as f:
    ips = f.read().split()

len_of_web = len(ips) #type: int
count_adr = 1 #type: int
while True:
    if len_of_web<=count_adr:
        break
    count_adr=count_adr*2

keys_to_masks = {} #type: dict
with open ('masks.txt', 'r') as f:
    for row in f:
        keys_to_masks[row.split()[1]] = (row.split()[0], row.split()[2])

ans = '' #type: str
for i in range(len(ips[0].split('.'))):
    ans += str(int(ips[0].split('.')[i]) % int(keys_to_masks[str(count_adr)][0].split('.')[i]))
    if i!=len(ips[0].split('.'))-1:
        ans+='.'

print('Result net: ' + ans+'/'+keys_to_masks[str(count_adr)][1])