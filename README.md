# Blockchain Demo - Python Django Project

This is a blockchain demo project developed using Python and Django, showcasing various aspects of blockchain technology, including hash generation, mining, blockchain chaining, peer-to-peer distribution, and key-based cryptography.

## Features

### 1) Hash Page
- **Path**: `/hash`
- Converts any input string into a **SHA-256** hash.
- This page allows users to input a string and generate its corresponding hash value.

### 2) Block Page
- **Path**: `/block`
- Converts **ID**, **nonce**, and **data** into a **SHA-256** hash.
- Includes a button to mine and generate a hash with a prefix of **4 zeros** using the nonce.

### 3) Blockchain Page
- **Path**: `/blockchain`
- Displays a chain of blocks, where each block is linked to its previous hash, forming a continuous blockchain.

### 4) Distributed Blockchain
- **Path**: `/distributed-blockchain`
- Simulates a **distributed blockchain system** with **3 peer blockchains**, demonstrating how blockchains interact with one another in a decentralized network.

### 5) Coinbase (Under Construction)
- **Path**: `/coinbase`
- This feature is under construction but will implement the creation of a **coinbase transaction** in the future.
  - [ ] Implement coinbase transaction creation.

### 6) Public and Private Key Operations

#### a) Public-Private Keys
- **Path**: `/public-private-keys/keys/`
- Allows the generation and management of public and private keys for cryptographic operations.

#### b) Digital Signature
- **Path**: `/public-private-keys/signature/`
- Allows users to sign data with their private key and verify signatures with the corresponding public key.

#### c) Transactions
- **Path**: `/public-private-keys/transactions/`
- Facilitates creating, signing, and sending transactions within the blockchain network using public and private keys.
  - [ ] Implement transaction creation and validation.

#### d) Blockchain with Public Keys
- **Path**: `/public-private-keys/blockchain/`
- Displays the blockchain and integrates public-private key functionalities for enhanced security and transaction validation.
  - [ ] Integrate public-private key security into blockchain display.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
  ```bash
   git clone https://github.com/yourusername/blockchain-demo.git
  ```
Navigate to the project directory:

```bash
cd blockchain-demo
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
Run the Django server:

bash
```
python manage.py runserver
```
Open the application in your web browser:
```bash
http://127.0.0.1:8000
```
License
This project is licensed under the MIT License - see the LICENSE file for details.



The checkboxes represent tasks that are still pending. You can mark them as completed once they're done. Let me know if you need further adjustments!
