from ape import accounts, project
def main():
    user = accounts.load("workshop")

    registry = project.Registration.at("0xa6cb85062cf15c65398c33b8fb8268669e575310")


    registry.checkin("caller", sender=accounts[0])

#ape run call_registration --network polygon:mumbai:alchemy