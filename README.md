# Tykoon - Smart Contract Automation Engine

## How To run

### Setup environment
* Install python virtual env
```shell
$ pip3 install virtualenv
```
* To create venv in, run the following command
```shell
$ python3 -m venv path/to/new/virtual/environment
```
* Activate your virtual environment
```shell
$ source path/to/new/virtual/environment/bin/activate
```

### Install required dependencies
* install all listed python modules
```shell
$ pip3 install -r requirements.txt
```

### Env variables
make sure the required env variables are defined, you can see the example in `.env.example` file

### If Use Alchemy provider
```shell
$ brownie networks set_provider alchemy
```

### Install Solidity Version
- check solidity version on contract file
```shell
$ from brownie.project.compiler import install_solc("0.8.4")
```

### Install external library via brownie
```shell
$ brownie pm install OpenZeppelin/openzeppelin-contracts@4.7.3
$ brownie pm install chiru-labs/ERC721A@4.2.3
```

### Run the server
```shell
$ python3 server.py
```