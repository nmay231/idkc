import unittest.mock as mock
from dataclasses import dataclass

from hypothesis import given
from hypothesis import strategies as st


@dataclass
class State:
    row: list[int]
    index: int

    def get_world_size(self) -> int:
        return len(self.row)

    def move(self, direction: int) -> None:
        assert 0 <= self.index + direction < len(self.row)
        self.index += direction

    def measure(self, direction: int = 0) -> int:
        assert 0 <= self.index + direction < len(self.row)
        return self.row[self.index + direction]

    def swap(self, direction: int) -> None:
        assert 0 <= self.index + direction < len(self.row)
        self.row[self.index], self.row[self.index + direction] = (
            self.row[self.index + direction],
            self.row[self.index],
        )


@given(
    row=st.lists(st.integers(min_value=0, max_value=9), min_size=1),
    start_index=st.integers(min_value=0),
)
def test_bubblesort(row: list[int], start_index: int) -> None:
    state = State([], 0)

    with (
        mock.patch("farmers.Cactus.clear_grid", mock.ANY, create=True),
        mock.patch("farmers.Cactus.get_world_size", state.get_world_size, create=True),
        mock.patch("farmers.Cactus.move", state.move, create=True),
        mock.patch("farmers.Cactus.measure", state.measure, create=True),
        mock.patch("farmers.Cactus.swap", state.swap, create=True),
    ):
        from farmers.Cactus import _bubble_sort_cactus

        state.row = row[:]
        state.index = start_index % len(row)
        _bubble_sort_cactus(1, -1, lambda: state.index)  # type: ignore

    assert state.row == sorted(row)
