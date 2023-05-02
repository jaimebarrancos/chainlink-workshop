from ape import accounts, project

def main():
    dev = accounts.load("workshop")

    contract =  dev.deploy(project.Token, "MyToken", "TKN")

    print("the name is : " + contract.name())