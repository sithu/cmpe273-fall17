# Final Exam Coding Questions

You will be completing the missing parts of a multi-crypocurrency blockchain platform which will support all universities throughout the U.S. Each university has their own currency (symbol) and total supply token amount. Under each currency, user uses wallet to store a 
digital value and can make transfers between wallets.

### 1. Install dependency

```sh
virtualenv exam-venv
source exam-venv/bin/activate
pip install -r requirements.txt
```

### 2. Generate Python gRPC binding code from a service definition .proto file.

```sh
python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. token.proto 
```

### 3. Implement get_rendezvous_node(nodes, key) function in client.py (10 points)

You will be using Rendezvous (HRW) hashing to shard coins based on their currency symbol. For example, SJSU Coin could live on the same node as SFSU Coin.

> You should not be touching other Python files except client.py.

### 4.  Test your Rendezvous hashing code

# Command with expected output

```sh
python3 coin_server_mapping.py 
SJSU coin is mapped to 0.0.0.0:3001
UCLA coin is mapped to 0.0.0.0:3001
SFSU coin is mapped to 0.0.0.0:3000
```

> Based on this above output, both SJSU and UCLA coins will run on 3001 host whereas SFSH coin will run on 3000 host.

You will be using the same setting in the Step 6 to launch multiple GRPC servers for one or more coins.

### 5. Implement all TODOs in the Wallet transfer and Merkle Root Generation functions in coin.py. (20 points)

#### How to Generate Merkle Root Hash Value

![](http://orm-chimera-prod.s3.amazonaws.com/1234000001802/images/msbt_0702.png)

> You should not be touching other Python files except coin.py.

#### Test your coin.py code without running as GRPC server.

```sh
python3 coin.py
coin_symbol: CMPE_Coin
total_supply: 100
num_txns: 2
merkle_root: 8a981b24324bb9eada8920a5bcaddf75397ba29322eda4b51989096364fe6ae8
---- WALLET START ----
wallet_id:Alice, wallet_balance:5
wallet_id:Bob, wallet_balance:5
wallet_id:owner, wallet_balance:90
---- WALLET END ----
---- TXN START ----
{'from_wallet': 'owner', 'to_wallet': 'Alice', 'amount': 10, 'time_stamp': '2017-12-13 14:46:33.942971', 'hash': '5e0e3bd986d1ab40725cb9cae4c7a071eef71195074a4bcd240b37b862ace3f4', 'merkle_root': '138fe999385070e06ddee82ccea1a8f5448f81219c27d95e4cde1efd2bc06fd9'}
{'from_wallet': 'Alice', 'to_wallet': 'Bob', 'amount': 5, 'time_stamp': '2017-12-13 14:46:33.943026', 'hash': '1f6a6582bd02a3ddd1cdaf974df74d9f88e64c09c2dbd2b1b177cc5ece7b8787', 'merkle_root': '8a981b24324bb9eada8920a5bcaddf75397ba29322eda4b51989096364fe6ae8'}
---- TXN END ----
```

### 6. Now, Run multiple gRPC servers based on the coin_server_mapping.py output.

Based on your Rendezvous hashing output in the step 4, you will be running multiple gRPC servers. So, we will need two servers for SJSU, UCLA, and SFSU universities.

```sh
python3 server.py 0.0.0.0:3000 SFSU
Blockchain server 0.0.0.0:3000 started for symbols:['SFSU']
```

```sh
python3 server.py 0.0.0.0:3001 SJSU,UCLA
Blockchain server 0.0.0.0:3001 started for symbols:['SJSU', 'UCLA']
```

### 7. Finally test all your code end-to-end.

```sh
python3 client.py
```

#### How to check your Merkle tree implementation?

If global Merkle root is the same as the last (recent) transaction's Merkle root, then you are done!

Example:

__Global Merkle Root__

```sh
{\'coin_symbol\': \'SFSU\', \'total_supply\': \'100\', \'num_txns\': \'4\', \'merkle_root\': \'2d6788bd05fff1f0a7cff427504ececbb1e68ec2a498b807d5adf03da8b18862\'
```

__Last Transaction__

```sh
\'txn_id_3\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:55:38.720856\', \'hash\': \'3967cf535bb9e6601d108553eca2d76d0382908271d77a5e328fd0aca6d7e3f5\', \'merkle_root\': \'2d6788bd05fff1f0a7cff427504ececbb1e68ec2a498b807d5adf03da8b18862\'}\"}"
```


__Expected Output__

```sh
Testing SFSU coin transactions
Client connected to 0.0.0.0:3000
SFSU Coin: TXN 1 - result = SUCCESS
Client connected to 0.0.0.0:3000
SFSU Coin: TXN 2 - result = SUCCESS
Client connected to 0.0.0.0:3000
data {
  entry {
    key: "SFSU"
    value: "{\'coin_symbol\': \'SFSU\', \'total_supply\': \'100\', \'num_txns\': \'4\', \'merkle_root\': \'2d6788bd05fff1f0a7cff427504ececbb1e68ec2a498b807d5adf03da8b18862\', \'wallet_id_Alice\': \'10\', \'wallet_id_Bob\': \'10\', \'wallet_id_owner\': \'80\', \'txn_id_0\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:27:49.787544\', \'hash\': \'ef2ed93215187645487d839194337979e1aa1868cfb32d5666f835d83774694c\', \'merkle_root\': \'3ee7e31a3a3aaacc901b4d74e3eda7f8f552695e2a15cd0d0872eee15b8151ba\'}\", \'txn_id_1\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:27:49.789654\', \'hash\': \'5162aa78e82e68e209cdb8c48a63abf64d9ab06942bd0fddd3069a05c7888e2e\', \'merkle_root\': \'6aa437d7c83d705b0f89368236637869c921c3f324e6d6ab18bd7fd9c3d420de\'}\", \'txn_id_2\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:55:38.718931\', \'hash\': \'2b2f2f8c60babdaed3d1479d29c7993432e565f4f15d6b6bf802e547a5ce420e\', \'merkle_root\': \'141f0282206d3e47d15d60d67c54a91af1a4dde6fbe6044e2f3629da7cea9e5e\'}\", \'txn_id_3\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:55:38.720856\', \'hash\': \'3967cf535bb9e6601d108553eca2d76d0382908271d77a5e328fd0aca6d7e3f5\', \'merkle_root\': \'2d6788bd05fff1f0a7cff427504ececbb1e68ec2a498b807d5adf03da8b18862\'}\"}"
  }
}

Testing SJSU coin transactions
Client connected to 0.0.0.0:3001
SJSU Coin: TXN 1 - result = SUCCESS
Client connected to 0.0.0.0:3001
SJSU Coin: TXN 2 - result = SUCCESS
Client connected to 0.0.0.0:3001
data {
  entry {
    key: "SJSU"
    value: "{\'coin_symbol\': \'SJSU\', \'total_supply\': \'100\', \'num_txns\': \'4\', \'merkle_root\': \'627f49beba9ad424babeffea2d2c26ec0b94dd6b4201e0c9f7ed898388a238f1\', \'wallet_id_Alice\': \'15\', \'wallet_id_Bob\': \'15\', \'wallet_id_owner\': \'70\', \'txn_id_0\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:27:49.793824\', \'hash\': \'182f6e26c732ac40b0dc0563a8bfc21b74fec707d36422882e3d42ee435d996c\', \'merkle_root\': \'1a2a724998ba7499625762c0bf6f0b79bf63c6ecefbd674dbeede74654d4f991\'}\", \'txn_id_1\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:27:49.795727\', \'hash\': \'54c214d0b1959102bc5dd47fceb9ad0a814b50e6a16a26a974873cc7cb7e0403\', \'merkle_root\': \'e911e46f340cd87b96fbbfcae13660f5e4c51854fc8944dfb7d531b0e225634b\'}\", \'txn_id_2\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:55:38.724920\', \'hash\': \'92b877626c4c873808a9cae189b1af13ba2068185d1ae1f1793c253e02121918\', \'merkle_root\': \'26bb79b1dddb3c50dec3b6db8f4438bdee17a5180007e236210c6a76f088a141\'}\", \'txn_id_3\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:55:38.726386\', \'hash\': \'405673fd959c4e9a6f3f9f5caca09ab1c13d4d717139941a7f26df609f12e3ec\', \'merkle_root\': \'627f49beba9ad424babeffea2d2c26ec0b94dd6b4201e0c9f7ed898388a238f1\'}\"}"
  }
  entry {
    key: "UCLA"
    value: "{\'coin_symbol\': \'UCLA\', \'total_supply\': \'100\', \'num_txns\': \'2\', \'merkle_root\': \'0d21d370fce02e33dcad942795f6ed9e6edfb333f100db1cc3586fafec821f1a\', \'wallet_id_Alice\': \'15\', \'wallet_id_Bob\': \'15\', \'wallet_id_owner\': \'70\', \'txn_id_0\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:27:49.800311\', \'hash\': \'3055758a9438d5971708369df715d0e35f12d8a14bd1ad52b9fba620800fa097\', \'merkle_root\': \'1529ca37d380fe43776124f50648ebf13c161446aa9c03692328c4827a0e32d3\'}\", \'txn_id_1\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:27:49.801676\', \'hash\': \'a01c67b80864f3ff89e59c451b784f4025966bc7b6eefbe905b27090a31345a8\', \'merkle_root\': \'0d21d370fce02e33dcad942795f6ed9e6edfb333f100db1cc3586fafec821f1a\'}\"}"
  }
}

Testing UCLA coin transactions
Client connected to 0.0.0.0:3001
UCLA Coin: TXN 1 - result = SUCCESS
Client connected to 0.0.0.0:3001
UCLA Coin: TXN 2 - result = SUCCESS
Client connected to 0.0.0.0:3001
data {
  entry {
    key: "SJSU"
    value: "{\'coin_symbol\': \'SJSU\', \'total_supply\': \'100\', \'num_txns\': \'4\', \'merkle_root\': \'627f49beba9ad424babeffea2d2c26ec0b94dd6b4201e0c9f7ed898388a238f1\', \'wallet_id_Alice\': \'20\', \'wallet_id_Bob\': \'20\', \'wallet_id_owner\': \'60\', \'txn_id_0\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:27:49.793824\', \'hash\': \'182f6e26c732ac40b0dc0563a8bfc21b74fec707d36422882e3d42ee435d996c\', \'merkle_root\': \'1a2a724998ba7499625762c0bf6f0b79bf63c6ecefbd674dbeede74654d4f991\'}\", \'txn_id_1\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:27:49.795727\', \'hash\': \'54c214d0b1959102bc5dd47fceb9ad0a814b50e6a16a26a974873cc7cb7e0403\', \'merkle_root\': \'e911e46f340cd87b96fbbfcae13660f5e4c51854fc8944dfb7d531b0e225634b\'}\", \'txn_id_2\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:55:38.724920\', \'hash\': \'92b877626c4c873808a9cae189b1af13ba2068185d1ae1f1793c253e02121918\', \'merkle_root\': \'26bb79b1dddb3c50dec3b6db8f4438bdee17a5180007e236210c6a76f088a141\'}\", \'txn_id_3\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:55:38.726386\', \'hash\': \'405673fd959c4e9a6f3f9f5caca09ab1c13d4d717139941a7f26df609f12e3ec\', \'merkle_root\': \'627f49beba9ad424babeffea2d2c26ec0b94dd6b4201e0c9f7ed898388a238f1\'}\"}"
  }
  entry {
    key: "UCLA"
    value: "{\'coin_symbol\': \'UCLA\', \'total_supply\': \'100\', \'num_txns\': \'4\', \'merkle_root\': \'f052129049a04d6de0c67a2f0c279bec21023a9ea0f2ca8b9a3769ffe934a40f\', \'wallet_id_Alice\': \'20\', \'wallet_id_Bob\': \'20\', \'wallet_id_owner\': \'60\', \'txn_id_0\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:27:49.800311\', \'hash\': \'3055758a9438d5971708369df715d0e35f12d8a14bd1ad52b9fba620800fa097\', \'merkle_root\': \'1529ca37d380fe43776124f50648ebf13c161446aa9c03692328c4827a0e32d3\'}\", \'txn_id_1\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:27:49.801676\', \'hash\': \'a01c67b80864f3ff89e59c451b784f4025966bc7b6eefbe905b27090a31345a8\', \'merkle_root\': \'0d21d370fce02e33dcad942795f6ed9e6edfb333f100db1cc3586fafec821f1a\'}\", \'txn_id_2\': \"{\'from_wallet\': \'owner\', \'to_wallet\': \'Alice\', \'amount\': 10, \'time_stamp\': \'2017-12-13 14:55:38.729832\', \'hash\': \'60a2273550b98edc7b64154f1c5cd48694d13b13d95cbc0f43088a4bbe7d4b5a\', \'merkle_root\': \'6d1e29fab5f9a2b0c23b421bc3399927701fd54b880e44a090e3b990004640ab\'}\", \'txn_id_3\': \"{\'from_wallet\': \'Alice\', \'to_wallet\': \'Bob\', \'amount\': 5, \'time_stamp\': \'2017-12-13 14:55:38.731055\', \'hash\': \'bcef3ca624264ad51a5b2230da494691b13a007e25268f5f7708a7cec199560d\', \'merkle_root\': \'f052129049a04d6de0c67a2f0c279bec21023a9ea0f2ca8b9a3769ffe934a40f\'}\"}"
  }
}

```
