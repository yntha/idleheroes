# Idle Heroes Client

A Python client for interacting with the official Idle Heroes game using an account of your choice.

## Usage
This client is designed to be used as a library in your own Python scripts, but it also provides a command-line interface (CLI) for basic operations:
```
# installation
$ git clone https://github.com/yntha/idleheroes.git
$ cd idleheroes
$ python -m pip install --user -e .

# run
$ ih-client
Requesting salt... Success!
Logging in... Success!
Authenticating... Success!
Checking for updates... Success!
Updating version 1.34.0 -> 1.34.115

# debug output
$ ih-client --debug
Requesting salt...
Sending 30 bytes:
====   0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
0000  00 1c 02 02 00 00 0a 16 78 78 78 78 78 78 78 78    ........xxxxxxxx
0010  78 78 78 78 78 78 78 78 78 78 78 78 78 78          xxxxxxxxxxxxxx


Received 49 bytes:
====   0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
0000  00 2f 02 02 08 00 12 20 78 78 78 78 78 78 78 78    ./..... xxxxxxxx
0010  78 78 78 78 78 78 78 78 78 78 78 78 78 78 78 78    xxxxxxxxxxxxxxxx
0020  78 78 78 78 78 78 78 78 18 ff ff ff ff 20 00 28    xxxxxxxx...." .(
0030  00                                                 .


Salt response: {
  "status": 0,
  "salt": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "uid": xxxxxxxx,
  "flag": 0,
  "cd": 0
}
Logging in...
Sending 82 bytes:
```

## Features
- Email & password login
- Server pinging (echo)
- Guest account registration
- Account authentication
- Version update checking

## Assets
The official Idle Heroes assets are encrypted and include the source code for the game client. This client distributes only the decrypted resource assets to provide a better experience, but not the decrypted game client code due to ethical and legal considerations. The decrypted assets are provided as a downloadable zip file in the [Releases](https://github.com/yntha/idleheroes/releases) section and are updated with each new game version.

## Contact
For questions or support, please open an [issue](https://github.com/yntha/idleheroes/issues). For direct contact, you can reach me on Discord `@kilozz` or Telegram `@neosophaux`.
