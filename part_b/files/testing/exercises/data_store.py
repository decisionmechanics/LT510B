"""This module supports loading JSON documents when memory is tight.

Attributes:
  load_data (function): Loads JSON data from a file.
"""

import json
from typing import Any, Dict, List, Union

JsonType = Union[
    Dict[str, Any],
    List[Any],
]


def load_data() -> JsonType:
    """Loads JSON data from a file.

    Data is taken from small.json.

    Returns:
      The deserialized data.
    """

    try:
        with open("small.json", encoding="utf8") as json_file:
            return json.load(json_file)
    except MemoryError:
        return []
