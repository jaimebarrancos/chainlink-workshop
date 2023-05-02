from ape import project, accounts

def main():
    user = accounts.load("workshop")
    faucet = project.Faucet.at("0xD8c338f520C2e9289cC645b58B7471988143aA59")

    faucet.withdraw(sender=user)