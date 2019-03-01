import numpy
import pyfldigi
import base64
from bitstring import BitArray
import binascii

fldigi = pyfldigi.Client()
fldigi.modem.id = 40 # try 40-45 for BPSK31-500
fldigi.main.rx()

rx = fldigi.text.get_rx_data()
print(rx)

# need to fetch original data from logs
txBits = BitArray(tx).bin

# Get bit array
rxBits = BitArray(rx).bin
N = len(rxBits)
errors = (numpy.array(list(txBits)) == numpy.array(list(rxBits))).sum()
ber = 1.0 * errors / N

# raw transaction
# rxHex = binascii.hexlify(base64.b64decode(rx))
