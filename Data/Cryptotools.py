"""
Have all the cryptographic tools and modules
"""

import hashlib as henc
def generate_hash(value):
    """ generate a hash code  """
    return henc.sha256(value.encode()).hexdigest()