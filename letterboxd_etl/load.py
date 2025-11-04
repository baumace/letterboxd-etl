import os
from supabase import create_client
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def load(letterbox_records):
    print("loading letterboxd records...")
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")

    if url is None:
        raise RuntimeError("URL is NONE")

    if key is None:
        raise RuntimeError("KEY is NONE")

    supabase = create_client(url, key)

    print("\tdeleting letterboxd records...")
    supabase.table("diary").delete().neq("id", 0).execute()
    print("\tdeleted letterboxd records...")

    print("\tinserting letterboxd records...")
    supabase.table("diary").insert(letterbox_records).execute()
    print("\tinserted letterboxd records...")

    print("loaded letterboxd records...")
    return
