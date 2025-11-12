# src/store.py
import json
import os
from datetime import datetime
from uuid import uuid4
from typing import List, Dict, Optional

# Default data file (override in tests or with env var)
DATA_FILE = "data.json"

def _read_file(path: str) -> List[Dict]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        if not text:
            return []
        try:
            data = json.loads(text)
            if isinstance(data, list):
                return data
            return []
        except json.JSONDecodeError:
            # corrupted or invalid JSON -> treat as empty (safer)
            return []

def _write_file(path: str, data: List[Dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_data(path: Optional[str] = None) -> List[Dict]:
    path = path or DATA_FILE
    return _read_file(path)

def save_data(items: List[Dict], path: Optional[str] = None) -> None:
    path = path or DATA_FILE
    _write_file(path, items)

def add_item(text: str, path: Optional[str] = None) -> Dict:
    path = path or DATA_FILE
    items = load_data(path)
    item = {
        "id": str(uuid4()),
        "text": text,
        "done": False,
        "created_at": datetime.utcnow().isoformat() + "Z"
    }
    items.append(item)
    save_data(items, path)
    return item

def list_items(path: Optional[str] = None) -> List[Dict]:
    return load_data(path)

def mark_done(index: int, path: Optional[str] = None) -> Dict:
    """
    Mark the item at 0-based index as done.
    Raises IndexError if index invalid.
    """
    path = path or DATA_FILE
    items = load_data(path)
    if index < 0 or index >= len(items):
        raise IndexError("Item index out of range")
    items[index]["done"] = True
    items[index]["done_at"] = datetime.utcnow().isoformat() + "Z"
    save_data(items, path)
    return items[index]