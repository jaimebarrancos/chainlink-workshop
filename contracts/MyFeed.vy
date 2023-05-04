# @version ^0.3.6

interface AggregatorV3Interface:
    def decimals() -> uint8: view
    def description() -> String[1000]: view
    def version() -> uint256: view
    def getRoundData(_roundId: uint80) -> (uint80, int256, uint256, uint256, uint80): view
    def latestRoundData() -> (uint80, int256, uint256, uint256, uint80): view


price_feed: public(AggregatorV3Interface)

@external
def __init__():
    self.price_feed = AggregatorV3Interface(0x007A22900a3B98143368Bd5906f8E17e9867581b)

@external
@view
def get_latest_price() -> int256:
    a: uint80 = 0
    price: int256 = 0
    b: uint256 = 0
    c: uint256 = 0
    d: uint80 = 0
    (a, price, b, c, d) = self.price_feed.latestRoundData()
    return price

@external
@view
def get_description() -> String[1000]:
    description: String[1000] = "--- wrong description -----"
    (description) = self.price_feed.description()
    return description