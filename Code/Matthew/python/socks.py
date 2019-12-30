
import random




# sock_counts = {
#     'ankle': 5,
#     'crew': 17
# }
# sock_counts['calf'] # crash, KeyError
# sock_counts['calf'] = sock_counts.get('calf', 0) + 1



# 1. choose 1,000 random types of sock, build a list of strings
# 2. start with an empty dictionary
# 3. loop over socks
# 4. if sock_type in dictionary, += 1, else value = 1
# 5. mod each value by 2, figure out if we have any loners


sock_types = ['ankle', 'crew', 'calf', 'thigh']

random_socks = []
for i in range(1000):
    random_socks.append(random.choice(sock_types))

# print(random_socks)

sock_counts = {}
for sock in random_socks:
    sock_counts[sock] = sock_counts.get(sock, 0) + 1

    # if sock in sock_counts:
    #     sock_counts[sock] += 1
    # else:
    #     sock_counts[sock] = 1


for key in sock_counts:
    # print(key, sock_counts[key])
    pairs = sock_counts[key]//2
    loners = sock_counts[key]%2
    add_s = ''
    if loners != 1:
        add_s = 's'
    print(f'{key} - {sock_counts[key]} total, {pairs} pair(s), {loners} loner{add_s}')
