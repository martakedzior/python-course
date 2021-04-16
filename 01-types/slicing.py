# string slicing
ip_addr = '203.0.113.68/24'

print(ip_addr[:12])  #grab 0 (inclusive) to 12
print(ip_addr[:-3])
print(ip_addr[12:])  #grab 12 (inclusive) to end
print(ip_addr[-3:])
print(ip_addr[6:9])
print(ip_addr[-9:-6])

# list slicing

cars = ['bmw', 'ford', 'gmc']
print(cars[1:])