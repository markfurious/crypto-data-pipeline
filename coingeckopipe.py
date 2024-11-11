from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago
import json

API_CONN_ID = 'coingecko_api'
POSTGRES_CONN_ID = 'postgres_coingecko'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

with DAG(dag_id='coingecko_crypto_etl',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    @task()
    def extract_crypto_data():
        """Extract cryptocurrency data from CoinGecko API."""
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')
        
        # CoinGecko API endpoint for market data
        endpoint = '/api/v3/coins/markets'
        params = {
            'vs_currency': 'usd',     # Base currency
            'order': 'market_cap_desc', # Order by market cap
            'per_page': 10,           # Number of coins to fetch
            'page': 1,                # Page number
            'sparkline': 'false'      # Do not include sparkline data
        }
        
        response = http_hook.run(endpoint, data=params)
        
        if response.status_code == 200:
            return response.json()  # Return JSON data if request is successful
        else:    
            raise Exception(f'Failed to fetch data: {response.status_code}')

    @task()
    def transform_crypto_data(data):
        """Transform the extracted cryptocurrency data."""
        transformed_data = []
        for item in data:
            transformed_data.append({
                'id': item['id'],
                'symbol': item['symbol'],
                'name': item['name'],
                'current_price': item['current_price'],
                'market_cap': item['market_cap'],
                'total_volume': item['total_volume'],
                'high_24h': item['high_24h'],
                'low_24h': item['low_24h'],
                'price_change_24h': item['price_change_24h']
            })
        return transformed_data

    @task()
    def load_crypto_data_to_postgres(transformed_data):
        """Load the transformed data into PostgreSQL."""
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_data (
            id VARCHAR(50),
            symbol VARCHAR(10),
            name VARCHAR(100),
            current_price FLOAT,
            market_cap BIGINT,
            total_volume BIGINT,
            high_24h FLOAT,
            low_24h FLOAT,
            price_change_24h FLOAT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Insert data into the table
        for data in transformed_data:
            cursor.execute("""
            INSERT INTO crypto_data (id, symbol, name, current_price, market_cap, total_volume, high_24h, low_24h, price_change_24h)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                data['id'],
                data['symbol'],
                data['name'],
                data['current_price'],
                data['market_cap'],
                data['total_volume'],
                data['high_24h'],
                data['low_24h'],
                data['price_change_24h']
            ))

        conn.commit()
        cursor.close()

    # Task dependencies
    crypto_data = extract_crypto_data()
    transformed_data = transform_crypto_data(crypto_data)
    load_crypto_data_to_postgres(transformed_data)
