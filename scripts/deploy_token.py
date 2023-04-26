from ape import accounts, project

def main():
    dev = accounts.test_accounts[0]

    #contract = project.Simple.deploy(sender=user)
    contract =  dev.deploy(project.Token, "MyToken", "TKN")

    print("the name is : " + contract.name())