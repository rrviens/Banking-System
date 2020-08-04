import Account
import merge_account
import hashlib

def mdhash_encode(account_number, account_type):            # store it 
    to_string = "".join(int(account_number)) + account_type
    hs = hashlib.md5(to_string.encode())
    return hs

# need to somehow have it so from the hashed value we can know the account_type. 
# md5 is one way, need some other way of approaching this
# maybe AES?
#
# def mdhash_decode(hs):
