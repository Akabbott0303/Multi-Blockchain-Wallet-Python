# Import dependencies
import subprocess
import json
import os
from dotenv import load_dotenv
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from bit import wif_to_key
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive):
    command = 'php ./derive -g --mnemonic="'+str(mnemonic)+'" --numderive="'+str(numderive)+'" --coin="'+str(coin)+'" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {'eth':derive_wallets(mnemonic, ETH, 3), 'btc-test':derive_wallets(mnemonic, BTCTEST, 3)}

# Create private key objects for each coin
eth_priv_key = coins['eth'][0]['privkey']
btctest_priv_key = coins['btc-test'][0]['privkey']

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# Create account object for each coin
eth_acc = btc_acc = priv_key_to_account(ETH, eth_priv_key)
btc_acc = priv_key_to_account(BTCTEST, btctest_priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
        }   
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    if coin == ETH:
        tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    if coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)

# Check ETH balance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545/0xd36eb3f541c90f19705b3b4cfe878cfe3b7456b5ce1e76ace8dfacbccb6333c7"))
w3.eth.getBalance("0x45D09DD827d7E831EF60f4E8EF7EAA9b0b1edC66")