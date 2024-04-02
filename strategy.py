import abc
from typing import Any

__all__ = ("BlockchainHelper", "BlockchainStrategy", "EthereumStrategy", "TronStrategy")


class BlockchainStrategy(abc.ABC):
    @abc.abstractmethod
    def send_transaction(self, data: dict) -> Any:
        raise NotImplementedError()


class EthereumStrategy(BlockchainStrategy):
    __slots__ = ("_blockchain",)

    def __init__(self) -> None:
        self._blockchain = "Ethereum"

    @property
    def blockchain(self) -> str:
        return self._blockchain

    def send_transaction(self, data: dict) -> None:
        print(f"A transaction on the {self.blockchain} blockchain was created with this data: {data}\n")


class TronStrategy(BlockchainStrategy):
    __slots__ = ("_blockchain",)

    def __init__(self) -> None:
        self._blockchain = "Tron"

    @property
    def blockchain(self) -> str:
        return self._blockchain

    def send_transaction(self, data: dict) -> None:
        print(f"A transaction on the Tron blockchain was created with this data: {data}")


class BlockchainHelper:
    __slots__ = ("_strategy",)

    def __init__(self, blockchain: str) -> None:
        self._strategy: BlockchainStrategy = self._get_strategy(blockchain=blockchain)

    @property
    def strategy(self) -> BlockchainStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, blockchain: str) -> None:
        self._strategy: BlockchainStrategy = self._get_strategy(blockchain=blockchain)

    def _get_strategy(self, blockchain: str) -> BlockchainStrategy:
        match blockchain:
            case "Ethereum":
                return EthereumStrategy()
            case "Tron":
                return TronStrategy()
            case _:
                raise NotImplementedError()

    def send_transaction(self, data: dict) -> None:
        self.strategy.send_transaction(data=data)


if __name__ == "__main__":
    blockchain_helper = BlockchainHelper(blockchain="Ethereum")
    blockchain_helper.send_transaction(data={"address_from": "{ether_address}", "address_to": "{ether_address}"})

    blockchain_helper.strategy = "Tron"
    blockchain_helper.send_transaction(data={"address_from": "{tron_address}", "address_to": "{tron} address"})
