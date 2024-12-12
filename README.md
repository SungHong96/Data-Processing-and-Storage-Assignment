# Data-Processing-and-Storage
## Overview
This program is a small database that runs in memory (no files or storage needed) and supports basic transactions. You can:
- Start a transaction
- Add or update data during a transaction
- Commit changes to save them
- Roll back changes to undo them

Keys are strings, and values are integers. It’s all about making sure changes happen completely or not at all (atomicity).

## How to Run
1. Download the code
2. Make sure Python is installed
3. Open terminal and run **python InMemoryDB.py**
4. The program includes test cases, so you’ll see how it works when you run it.

## How It Works
The code uses a class called **InMemoryDB** to handle everything:
- Main storage (main): Keeps permanent data.
- Temporary storage (storage): Stores data during a transaction.
- Transaction status (active): Tracks whether a transaction is happening.

Key Functions:
- begin_transaction(): Starts a new transaction.
- put(key, value): Adds or updates a key-value pair in the transaction.
- get(key): Fetches data, prioritizing transaction data.
- commit(): Saves transaction changes to the main storage.
- rollback(): Cancels all changes in the transaction.

## Suggestions For Assignment
- Add more detailed error messages instead of just "Null".
- Allow nested transactions for more complex cases.
- Write automated tests to make sure it works in all scenarios
- Add a way to save data to a file or database for longer-term use.