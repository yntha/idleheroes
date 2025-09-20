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
$ ih-client
[IHNetClient] Logging in...
[IHNetClient] Logged in.
[IHNetClient] Checking for updates...
[IHNetClient] Client is up-to-date (version: 1.34.119)
[IHNetClient] Syncing game state...
[IHNetClient] Game state synced.
[IHNetClient] Checking mail...
[IHNetClient] Claimed 1 mails:
[IHNetClient]   Mail(ID: 357, Name: Pioneer Points Reward Email, From: System Email, Affix: [Treasure Coupon x3, Magic Dust x3000, Gem x1500, Gold x3000000])
Logged in as: ----- (UID: ----------)
Gold: 702960346 | Gems: 16658 | XP: 69747312
```

On first launch, the client will ask you for your credentials (email and password) to log in. It will then save your credentials to `config/account.json` for future use.

## Features
- Email & password login
- Server pinging (echo)
- Guest account registration
- Account authentication
- Version update checking
- Game state synchronization
- Player bag information retrieval
- Mail operations (read, claim, delete, block)

## Assets
The official Idle Heroes assets are encrypted and include the source code for the game client. This client distributes only the decrypted resource assets to provide a better experience, but not the decrypted game client code due to ethical and legal considerations. The decrypted assets are provided as a downloadable zip file in the [Releases](https://github.com/yntha/idleheroes/releases) section and are updated with each new game version. If the client detects that the local assets are outdated or missing, it will download and extract the latest/base assets automatically. <b>The base assets are 642 MB in size.</b>

## Contact
For questions or support, please open an [issue](https://github.com/yntha/idleheroes/issues). For direct contact, you can reach me on Discord `@kilozz` or Telegram `@neosophaux`.
