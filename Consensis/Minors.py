import hashlib


def block_mining(miner_details,chain,last_block,transactions):
    """ min the blockchain and reword  """
    chain.add_transaction(sender=0, recepient=miner_details, amount=1, memo="")


    last_proof_no = last_block.proof_no
    proof_no = do_proof_of_work(last_proof_no)
    last_hash = last_block.hash

    block = chain.generate_block(proof_of_work=proof_no, last_block_hash=last_hash, transaction=transactions)

    return vars(block)

def do_proof_of_work(last_proof):
    """ Construct a proof of work"""
    proof_no = 0
    while Verifying_proof(proof_no, last_proof) is False:
        proof_no += 1

    return proof_no


def Verifying_proof(last_proof, proof_no):
    """ Verify the last proof of work """
    guss = f'{last_proof}{proof_no}'.encode()
    guss_hash = hashlib.sha256(guss).hexdigest()
    return guss_hash[:4] == "0000"




def check_validity(block, previous_block):
    """ Check validity of two blocks """
    if previous_block.id + 1 != block.id:
        return False
    elif previous_block.hash != block.hash:
        return False
    elif not Verifying_proof(block.proof_no, previous_block.proof_no):
        return False
    elif block.timestamp <= previous_block.timestamp:
        return False
    return True
