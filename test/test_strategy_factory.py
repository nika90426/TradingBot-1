import pytest
from Components.Configuration import Configuration
from Strategies.SimpleMACD import SimpleMACD
from Strategies.StrategyFactory import StrategyFactory
from Strategies.WeightedAvgPeak import WeightedAvgPeak


@pytest.fixture
def config():
    return Configuration.from_filepath("test/test_data/config.json")


@pytest.fixture
def broker():
    return "mock"


def test_make_strategy_fail(config, broker):
    sf = StrategyFactory(config, broker)
    strategy = sf.make_strategy("")
    assert strategy is None

    strategy = sf.make_strategy("wrong")
    assert strategy is None


def test_make_strategy(config, broker):
    sf = StrategyFactory(config, broker)
    strategy = sf.make_strategy("simple_macd")
    assert isinstance(strategy, SimpleMACD)

    strategy = sf.make_strategy("weighted_avg_peak")
    assert isinstance(strategy, WeightedAvgPeak)
