import pytest

from src.fila import Fila


def test_fila_fifo() -> None:
    fila: Fila[int] = Fila()
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    assert fila.peek() == 10
    assert fila.dequeue() == 10
    assert fila.dequeue() == 20
    assert fila.dequeue() == 30
    assert len(fila) == 0

    with pytest.raises(IndexError):
        fila.dequeue()
