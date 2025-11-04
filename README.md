# letterboxd-etl
Python console application to extract, transform, and load Letterboxd account export data.

## Setup
1. Clone the repository
2. Ensure `poetry` is installed
3. Copy `.env.example` to `.env` and fill with appropriate values
4. Disable RLS temporarily
5. Run the scripts with the exported data
```bash
poetry run python scripts/run_etl.py ~/path/to/exported/zip
```
6. Re-enable RLS

## Local Development
1. Activate `poetry` virtual environment from the project root 
```bash
eval $(poetry env activate)
```
2. Install dependencies (from activated environment)
```bash
poetry install
```
3. Run the script (from activated environment)
```bash
python scripts/run_etl.py ~/path/to/exported/zip
```
