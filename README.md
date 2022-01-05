# Multi-Blockchain Wallet in Python

This project includes code and instructions for building and using a cryptocurrency hot wallet in Python.  The code imports the required libraries and environment variable and creates functions to create the wallet, convert privates keys to wallet addresses, and create and send transactions.  The coins used are Ethereum (ETH) and Bitcoin testnet (BTCTEST).  Additional coins can be added to this wallet.

### Installations

Use the [Requirements](/Requirements.txt)) to install the dependencies needed to run the code to create the HD wallet.  

Install [PHP and Apache Web Server](https://www.apachefriends.org/index.html) for Windows operating systems.  Windows users might also need to install [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/downloads/).

To install the [hd-wallet-derive tool](https://github.com/dan-da/hd-wallet-derive), open up a terminal window as Administrator.  Run the following code:

![hd-wallet-derive-install-code](/Screenshots/hd_wallet_derive_install.png)

This will create a new folder called hd-wallet-derive.  You will run the Pyhon code in the folder containing the hd-wallet-derive folder.  To create a shorcut (symlink) to make it easier to run the code, open a terminal as Administrator and change directory to your project folder, which should contain the hd-wallet-derive folder.  Run the following commands:

1. export MSYS=winsymlinks:nativestrict
2. ln -s hd-wallet-derive/hd-wallet-derive.php derive

To test that you can run the ./derive script properly, run the following command:

./derive --key=xprv9zbB6Xchu2zRkf6jSEnH9vuy7tpBuq2njDRr9efSGBXSYr1QtN8QHRur28QLQvKRqFThCxopdS1UD61a5q6jGyuJPGLDV9XfYHQto72DAE8 --cols=path,address --coin=ZEC --numderive=3 -g

The output should look similar to this:

![symlink_creation_output](/Screenshots/symlink_creation_output.png)

Now you can start creating your own multi-blockchain wallet!

### Setting up the Wallet and Sending Transactions
l
Thy Python code first imports all libraries and loads an environment variable to set the mnemonic phrase that will be used to generate the keys and addresses.  The code also imports a constants file to set the coin variables.  You'll need to add to these if you want to use the wallet to hold additional coin types.

The derive_wallets function uses the mnemonic phrase to generate wallet private keys and addresses for each coin type.  A dictionary called coins is established to hold the keys.  The priv_key_to_account function creates an account object from a private key.  The create_tx function creates a raw, unsigned transaction that contains the metadata required to run a transaction.  The send_tx signs the transaction and sends it to the designated network.



[Download Geth web page](https://geth.ethereum.org/downloads/)

![My Crypto Custom Network Information](/Screenshots/MyCryptoCustomNode.png)

[Node_Keys](/Node_Keys.txt))


