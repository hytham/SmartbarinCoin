"""
Collection of tools to handle the merkal tree
"""
import hashlib
from bitstring import xrange

def calculate_merkal_root(transactions):
    blocks = []
    if not transactions:
        raise ValueError('Missing required file hashes for computing merkel tree hash')

    for m in sorted(transactions):
        blocks.append(m)

    list_len = len(blocks)

    while list_len % 2 != 0:
        blocks.extend(blocks[-1:])
        list_len = len(blocks)

    secondary = []

    for k in [blocks[x:x + 2] for x in xrange(0, len(blocks), 2)]:
        hasher = hashlib.sha256()
        hasher.update(k[0].encode() + k[1].encode())
        secondary.append(hasher.hexdigest())
    if len(secondary) == 1:
        return secondary[0][0:64]
    else:
        return calculate_merkal_root(secondary)