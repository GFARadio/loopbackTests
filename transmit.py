"""
  Transmit a raw bitcoin transaction using Fldigi
"""

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import pyfldigi

CALLSIGN = 'KBBL' # update this

fldigi = pyfldigi.Client()
fldigi.modem.id = 40 # try 40-45 for BPSK31-500

btc = AuthServiceProxy("http://%s:%s@45.76.1.186:18443"%('foo','bar')) 
btc.getbestblockhash() # check to make sure it's working
addr = btc.getnewaddress() # generate address 
txhash = btc.sendtoaddress(addr, 1) # send 1 bitcoin to new address
tx = btc.getrawtransaction(txhash) # get raw transaction
print(tx)
txQueue = """QST DE %s\n \
<SIZE %s>%s<EOT>\n\
DE %s K
""" % (CALLSIGN, len(tx), tx, CALLSIGN)
timeout = round(len(tx)/3)
fldigi.main.send(txQueue, block=True, timeout=timeout)
fldigi.main.rx()
