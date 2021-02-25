#!/usr/bin/python

import sqlite3
import pandas as pd

from constants import DB_NAME, TOKEN_METRICS_SUFFIX, EXCHANGE_METRICS_SUFFIX, UNISWAP_EXCHANGE_CODE, SOLANA_TOKEN_CODE, \
    ETHERIUM_TOKEN_CODE, SERUM_EXCHANGE_CODE
from exchange_metrics_service import ExchangeMetricsService
from token_metrics_service import TokenMetricsService




class SQLLiteDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)

        print(f"Opened {DB_NAME} successfully")

        # # Create a table for each token
        # for token_code in TOKEN_CODES:
        #     self.conn.execute(f'''CREATE TABLE IF NOT EXISTS {token_code}_metrics
        #              (id INT PRIMARY KEY     NOT NULL,
        #              timestamp TIMESTAMP CURRENT_TIMESTAMP,
        #              tx_fee            DOUBLE     NOT NULL,
        #              tx_delay            DOUBLE     NOT NULL
        #              );''')
        #
        # self.conn.close()

    def get_token_df(self, token_code) -> pd.DataFrame:
        """"""
        self.conn = sqlite3.connect(DB_NAME)

        print(f"Opened {DB_NAME} successfully")

        df = pd.read_sql_query(f"SELECT * from {token_code}_metrics", self.conn)

        self.conn.close()
        return df

    def get_exchange_df(self, exchange_code) -> pd.DataFrame:
        """"""
        self.conn = sqlite3.connect(DB_NAME)

        print(f"Opened {DB_NAME} successfully")

        df = pd.read_sql_query(f"SELECT * from {exchange_code}_metrics", self.conn)

        self.conn.close()
        return df

    def store_dummy_data(self):
        """Just for development, storing test data"""
        self.conn = sqlite3.connect(DB_NAME)

        # Add tokens - manually for now
        token_metrics_service = TokenMetricsService(self)

        eth_df = token_metrics_service.get_dummy_data_eth()
        eth_df.to_sql(f"{ETHERIUM_TOKEN_CODE}{TOKEN_METRICS_SUFFIX}", self.conn, if_exists="replace")
        sol_df = token_metrics_service.get_dummy_data_sol()
        sol_df.to_sql(f"{SOLANA_TOKEN_CODE}{TOKEN_METRICS_SUFFIX}", self.conn, if_exists="replace")

        exchange_metrics_service = ExchangeMetricsService(self)
        uniswap_df = exchange_metrics_service.get_dummy_data_uniswap()
        uniswap_df.to_sql(f"{UNISWAP_EXCHANGE_CODE}{EXCHANGE_METRICS_SUFFIX}", self.conn, if_exists="replace")
        serum_df = exchange_metrics_service.get_dummy_data_serum()
        serum_df.to_sql(f"{SERUM_EXCHANGE_CODE}{EXCHANGE_METRICS_SUFFIX}", self.conn, if_exists="replace")


        self.conn.close()

