import sys
from letterboxd_etl.extract import extract
from letterboxd_etl.transform import transform
from letterboxd_etl.load import load

zip_file_name = sys.argv[1]

letterboxd_records = extract(zip_file_name)
transformed_records = transform(letterboxd_records)
load(transformed_records)
