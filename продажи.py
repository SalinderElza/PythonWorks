from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, things, value = line.split()
    clients[client][things] += int(value)
for client in sorted(clients):
    print(client + ':')
    for things in sorted(clients[client]):
        print(things, clients[client][things])
