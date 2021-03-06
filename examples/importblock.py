from pyethapp.leveldb_service import LevelDB
from pyethapp.config import default_data_dir
from pyethapp.eth_protocol import TransientBlock
from ethereum.chain import Chain
from ethereum.slogging import configure
import rlp
import os
configure(':trace')

def get_chain(data_dir=default_data_dir):
    """
    returns an ethereum.chain.Chain instance
    """
    dbfile = os.path.join(data_dir, 'leveldb')
    db = LevelDB(dbfile)
    return Chain(db)


# block # 447361 / 0x9c496f3bdfd428d19c8ae87fc8f653cac3278e0b07528bd0a065b1878dc56ca6
rlp_data = """f90201f901fca03a3ce492dd9865a0baeafbf4df006aff84e0b4ae39c8fbecfd994f9a7c0af748a01dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d493479482b27dbe07d34fb96309d2306e2729b6c5d155ffa0b9e10a7b297a3e5fb57bb222dc1b5df6211457271a37ebe2710b63da47d7904aa056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421a056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421b9010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000850177ffb17e8306d381832fefd880845564a4f280a089a6165f905f48436103b7a6ee6c216530029e01378883672d2ccb46e3ce478f888b11ce88aed597f2c0c0""".decode('hex')

def import_block(chain, rlp_data):
    ll = rlp.decode_lazy(rlp_data)
    transient_block = TransientBlock.init_from_rlp(ll, 0)
    transient_block.to_block(chain.db)

if __name__ == '__main__':
    chain = get_chain()
    print '\nIMPORTING BLOCK'
    # h = chain.get_blockhash_by_number(447360)
    # b = chain.get(h)
    # rlp_data = rlp.encode(b)
    import_block(chain, rlp_data)
