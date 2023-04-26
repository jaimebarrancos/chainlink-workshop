from ape import accounts, networks

def test_accounts():
    account = accounts.load('workshop')


    with networks.polygon.mumbai.use_provider("alchemy"):
        assert account.balance > 0



# def test_a():
#     assert 1==1