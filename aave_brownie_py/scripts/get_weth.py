from scripts.helpful_scripts import get_account
from brownie import interface, config, network, accounts
import sys


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    """
    Why not "get_contract"?
    Because we're going to be testing on mainnet-fork,
    we know we're always going to refer back to the config.
    So we're confident we're not going to be deploying any mocks.
    """
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 WETH")