# import logging
# from os import environ

# import psycopg2
# from dotenv import load_dotenv

# from connections import connect_to_postges
# from setting_loaders import load_etl_settings

# load_dotenv('/_MYF/1_pr/postgres_to_es/.env')
# logger = logging.getLogger(__file__)
# logging.basicConfig(filename='/_MYF/1_pr/postgres_to_es/main_py.log',level=logging.INFO)

# postgres_settings = load_etl_settings()
# print(postgres_settings)
# pg_conn: psycopg2.extensions.connection = connect_to_postges(postgres_settings.dict())
# print('everyting in order')
