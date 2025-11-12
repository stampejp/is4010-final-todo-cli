# tests/test_store.py
import src.store as store
from pathlib import Path

def test_add_and_list(tmp_path):
    file = tmp_path / "data.json"
    store.DATA_FILE = str(file)
    item = store.add_item("task1")
    items = store.list_items()
    assert len(items) == 1
    assert items[0]["text"] == "task1"
    assert items[0]["id"] == item["id"]
    assert not items[0]["done"]

def test_mark_done(tmp_path):
    file = tmp_path / "data.json"
    store.DATA_FILE = str(file)
    store.add_item("task1")
    store.add_item("task2")
    done_item = store.mark_done(1)
    assert done_item["text"] == "task2"
    assert done_item["done"] is True
    items = store.list_items()
    assert items[1]["done"]