from ape import accounts, project

def main():
    user = accounts.test_accounts[0]

    #contract = project.Simple.deploy(sender=user)
    contract = user.deploy(project.Simple)

    print(contract.value())