from letterboxd_etl.constants import DIARY_STR, LB_DIARY_COLUMNS, SB_DIARY_COLUMNS
import pandas
from typing import Dict, List, Any

def transform(letterboxd_records: Dict[str, pandas.DataFrame]) -> List[Dict[str, Any]]:
    print("transforming letterboxd records...")

    # convert data types
    diary_records = letterboxd_records[DIARY_STR]
    diary_records[LB_DIARY_COLUMNS.NAME] = diary_records[LB_DIARY_COLUMNS.NAME].astype(str)
    diary_records[LB_DIARY_COLUMNS.LETTERBOXD_URI] = diary_records[LB_DIARY_COLUMNS.LETTERBOXD_URI].astype(str)
    diary_records[LB_DIARY_COLUMNS.TAGS] = diary_records[LB_DIARY_COLUMNS.TAGS].astype(str)
    diary_records[LB_DIARY_COLUMNS.RATING] = pandas.to_numeric(diary_records[LB_DIARY_COLUMNS.RATING], errors='coerce')
    diary_records[LB_DIARY_COLUMNS.WATCHED_DATE] = diary_records[LB_DIARY_COLUMNS.WATCHED_DATE]

    # convert data to dict
    records: List[Dict[str, Any]] = []
    for _, row in diary_records.iterrows():
        rec = {}
        rec[SB_DIARY_COLUMNS.NAME] = row[LB_DIARY_COLUMNS.NAME]
        rec[SB_DIARY_COLUMNS.LETTERBOXD_URI] = row[LB_DIARY_COLUMNS.LETTERBOXD_URI]
        rec[SB_DIARY_COLUMNS.TAGS] = row[LB_DIARY_COLUMNS.TAGS]
        rec[SB_DIARY_COLUMNS.RATING] = row[LB_DIARY_COLUMNS.RATING]
        rec[SB_DIARY_COLUMNS.WATCHED_DATE] = row[LB_DIARY_COLUMNS.WATCHED_DATE]
        records.append(rec)

    print("transformed letterboxd records...")
    return records
