# CLI File-Backed Movie List Manager

An upgraded Python command-line application for managing a personal movie collection. Extends in-memory operations with flat-file I/O operations (`movies.txt`) to ensure persistent data storage across application restarts.

## Technical Highlights

* **File-Backed Data Persistence:** Features flat-file read/write handlers (`read_movies_file`, `write_movies_file`) using Python's `with open()` context managers to synchronize in-memory list updates with disk storage.
* **Automatic File Initialization:** Executes bootstrap logic (`create_movies_file`) to initialize the storage file with default entries upon initial execution.
* **Array-to-File Syncing:** Automatically triggers disk-write operations whenever the collection is modified via addition (`add_title`) or removal (`delete_title`).
* **Enumerated Index Mapping & Validation:** Combines `enumerate(start=1)` list presentation with `try/except` integer casting to safely process 1-indexed user selections against zero-indexed array boundaries.

## File Architecture

* `movies.txt` — Plain text flat-file storing the movie collection line-by-line.

## Technical Requirements

* **Python Version:** Built using pure standard Python 3.x (requires zero external `pip` dependencies).

## Usage

```bash
python main.py
