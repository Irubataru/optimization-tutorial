import csv
from dataclasses import dataclass, field


@dataclass
class Item:
    """
    An item on the file system.

    Attributes:
        name (str): The name or path of the file
        size (str): The size (in MB) of the file
        value (str): The intrinsic value of backup up the file
    """

    name: str
    size: float
    value: float

    @staticmethod
    def from_dict(value: dict) -> 'Item':
        """
        Create a new item from a dict.

        Args:
            value: the dict, must contain "name", "size", and "value" keys
        """
        return Item(value["name"], float(value["size"]), float(value["value"]))

    @staticmethod
    def from_csv(filename: str) -> list['Item']:
        """
        Create a list of items from a CSV file.

        Args:
            filename: The filename of the CSV file to read. Assumed to have columns "name", "size", and "value"
        """
        return [Item.from_dict(row) for row in csv.DictReader(open(filename, 'r'))]

    @staticmethod
    def get_by_name(items: list['Item'], name: str) -> 'Item':
        """
        Search a list of items for a specific item identified by name.

        Args:
            items: The list of items to search in
            name: The name of the item to find

        Returns:
            An item if one exists, None otherwise.
        """
        for item in items:
            if item.name == name:
                return item

        return None

    @staticmethod
    def to_dict(items: list['Item']) -> dict[str, 'Item']:
        """
        Convert a list of items to a dict of items.

        Args:
            items: The items to convert to a dictionary.

        Returns:
            A dictionary where the key is the item name, and the value is the item.
        """
        result = {}

        for item in items:
            result[item.name] = item

        return result


class Selection:
    """
    A selection of items to back up.

    Attributes:
        items (list[Item]): The list of items we can back up.
    """

    items: list[Item] = field(default_factory=list[Item])

    def size(self) -> float:
        """
        Calculate the total size of the file selection.
        """
        return sum([item.size for item in self.items])

    def score(self) -> float:
        """
        Calculate the total score/value of the file selection.
        """
        return sum([item.value for item in self.items])

    def get_item(self, name: str) -> Item | None:
        """
        Search a list of items for a specific item identified by name.

        Args:
            name: The name of the item to find

        Returns:
            An item if one exists, None otherwise.
        """
        for item in self.items:
            if item.name == name:
                return item

        return None

    def __init__(self, items: list[Item]):
        self.items = items

    def copy(self):
        """
        Create a copy of the selection.
        """
        return Selection(self.items.copy())

    @staticmethod
    def from_mask(items: list[Item], selection: list[bool]) -> 'Selection':
        """
        Create a selection based on a large list of items and a boolean mask where the value of the mask's i'th position determines
        whether to include the item at the lists i'th position.

        Args:
            items: The items to select from.
            selection: The mask determining which items to include.
        """

        solution = Selection([])

        for (i, item) in enumerate(items):
            if selection[i]:
                solution.items.append(item)

        return solution

    def __str__(self) -> str:
        """
        Pretty string conversion for a selection of items.
        """

        items = ""
        for i in range(min(10, len(self.items))):
            items += f"- {self.items[i].name}\n"

        if len(self.items) > 10:
            items += '- ...\n'

        return f"Items:\n{items}\nSize:  {self.size()}\nScore: {self.score()}"
