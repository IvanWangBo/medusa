#!/usr/bin/env python
# coding:utf-8


import hash_ring

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
nodes = range(10)
print nodes

ring = hash_ring.HashRing(nodes)
# print ring

ns = []
for key in range(20):
    ns.append(ring.get_node(str(key)))
print ns
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
nodes = range(11)
print nodes

ring = hash_ring.HashRing(nodes)
# print ring

ns = []
for key in range(20):
    ns.append(ring.get_node(str(key)))
print ns
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [8, 0, 0, 3, 7, 0, 0, 6, 2, 9, 6, 6, 5, 2, 7, 3, 0, 2, 5, 3]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [8, 0, 0, 3, 7, 0, 0, 6, 2, 9, 6, 10, 5, 10, 7, 3, 10, 2, 10, 3]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>