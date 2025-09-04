import asyncio

from google.protobuf.json_format import MessageToJson
from client.ihnet import IHNetClient


async def main():
    client = await IHNetClient.create_from_config()
    account = client.get_account()

    if not account.account or not account.password:
        print("Account details are incomplete or missing. Please set up your account:")

        account.account = input("Account: ").strip()
        account.password = input("Password: ").strip()

    try:
        # print("Sending 5 echo requests...")
        # for i in range(5):
        #     echo = await client.echo()
        #     print(f"Echo response {i+1}: {MessageToJson(echo)}")

        # might not be a good idea to spam registration requests
        # print("\nRegistering guest account...")
        # reg = await client.reg()
        # print(f"Registration response: {MessageToJson(reg)}")

        print("\nRequesting salt...")
        salt = await client.salt()
        print(f"Salt response: {MessageToJson(salt)}")

        print("\nLogging in...")
        login = await client.login(salt.salt)
        print(f"Login response: {MessageToJson(login)}")

        print("\nAuthenticating...")
        auth = await client.auth(login.uid, login.session)
        print(f"Auth response: {MessageToJson(auth)}")

        if auth.status == 0:
            print("\nAuthentication successful!")
        else:
            print("\nAuthentication failed!")

    finally:
        await client.disconnect()


def cli_entry():
    asyncio.run(main())


if __name__ == '__main__':
    cli_entry()