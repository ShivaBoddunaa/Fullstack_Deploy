import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


DB_URL = os.getenv("postgresql://postgres.plfcbrrmqulhjavgkyhf:1234567@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres")


def get_conn():
    conn = psycopg2.connect(DB_URL)
    return conn