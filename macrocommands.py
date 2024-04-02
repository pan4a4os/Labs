from abc import ABC, abstractmethod
from typing import Any, Union


class Recipient:
    def perform_action(self, msg: str):
        print(f"{self.__class__.__name__}: {msg}")


class Command(ABC):
    __slots__ = ("recipient",)

    def __init__(self, recipient: Recipient) -> None:
        self.recipient: Recipient = recipient

    @abstractmethod
    def process(self) -> Any:
        raise NotImplementedError()


class StartCommand(Command):
    def __init__(self, recipient: Recipient) -> None:
        super().__init__(recipient=recipient)

    def process(self):
        self.recipient.perform_action(msg=f"The {self.__class__.__name__} performed.")


class EndCommand(Command):
    def __init__(self, recipient: Recipient) -> None:
        super().__init__(recipient=recipient)

    def process(self):
        self.recipient.perform_action(msg=f"The {self.__class__.__name__} performed.")


class Summoner:
    __slots__ = ("_cmd",)

    def __init__(self) -> None:
        self._cmd = None

    @property
    def command(self) -> Union[Command, None]:
        return self._cmd

    @command.setter
    def command(self, cmd: Command) -> None:
        self._cmd = cmd

    def execute(self) -> None:
        self._cmd.process()


if __name__ == "__main__":
    recipient_ = Recipient()
    start_command = StartCommand(recipient=recipient_)
    end_command = EndCommand(recipient=recipient_)

    summoner = Summoner()
    summoner.command = start_command
    summoner.execute()

    summoner.command = end_command
    summoner.execute()
