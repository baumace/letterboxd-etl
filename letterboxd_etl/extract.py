import zipfile
import pandas
from letterboxd_etl.constants import DIARY_STR, LB_DIARY_COLUMNS
from typing import Dict 

def extract(zip_file_name) -> Dict[str, pandas.DataFrame] :
    print('extracting from ' + zip_file_name + '...')
    letterboxd_records = {}
    with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
        with zip_file.open(DIARY_STR + '.csv') as diary_file:
            diary_records = pandas.read_csv(diary_file)
            diary_columns_records = diary_records[[LB_DIARY_COLUMNS.NAME, LB_DIARY_COLUMNS.LETTERBOXD_URI, LB_DIARY_COLUMNS.RATING, LB_DIARY_COLUMNS.TAGS, LB_DIARY_COLUMNS.WATCHED_DATE]]
            letterboxd_records[DIARY_STR] = diary_columns_records
            print_file_read_log(DIARY_STR + '.csv', len(diary_columns_records))

    print('extraction complete...')
    return letterboxd_records

def print_file_read_log(file_name, num_records):
    print('\tread ' + str(num_records) + ' records from ' + file_name + '...')
    return
