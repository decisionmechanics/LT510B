"""This module tests the data_store module."""

import pytest
from pytest_mock import MockerFixture
import data_store


def test_load_data_returns_empty_list_when_out_of_memory(mocker: MockerFixture) -> None:
    """Tests that an empty list is return when there's a memory error.

    Args:
      mocker: Automatically injected mocker fixture.
    """

    # Arrange
    mocker.patch("json.load", side_effect=MemoryError("out of memory"))

    # Act
    data = data_store.load_data()

    # Assert
    assert data == []


def test_load_data_returns_exception_when_file_is_missing(
    mocker: MockerFixture,
) -> None:
    """Tests that an exception is raised when a file is missing..

    Args:
      mocker: Automatically injected mocker fixture.
    """

    # Arrange
    mocker.patch("json.load", side_effect=FileNotFoundError("file not found"))

    # Act
    with pytest.raises(FileNotFoundError) as exc_info:
        data_store.load_data()

    # Assert
    assert str(exc_info.value) == "file not found"
