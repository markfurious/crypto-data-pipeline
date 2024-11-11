
# Cryptocurrency ETL Pipeline Documentation

This documentation provides an overview of the images that showcase various stages and components of the cryptocurrency ETL (Extract, Transform, Load) pipeline project.

## 1. Airflow Connections - `Connections.png`


This image shows the configuration of connections in Apache Airflow. Connections are set up to facilitate communication between Airflow and external services or databases:

- **CoinGecko API (`coingecko_api`)**: This HTTP connection is configured to pull cryptocurrency data from the CoinGecko API. The host URL points to `https://api.coingecko.com`.
- **PostgreSQL Connections (`postgres_coingecko` and `postgres_default`)**: These PostgreSQL connections are configured to store transformed data in a PostgreSQL database. The database is hosted within the Docker container environment, as indicated by the hostnames (e.g., `etl-project_20f416-postgres-1`). Port `5432` is the default for PostgreSQL.

This setup allows the ETL pipeline to extract data from CoinGecko and load it into PostgreSQL.

## 2. Airflow DAG Dashboard - `Dashboard DAGs.png`


This image displays the Airflow DAG (Directed Acyclic Graph) dashboard for the ETL pipeline (`coingecko_crypto_etl`). The DAG is scheduled to run daily, with tasks organized as follows:

- **DAG Overview**: Provides a summary of the total runs, success and failure counts, and other statistics related to the ETL pipeline's execution.
- **Task View**: The tasks are broken down into:
  - `extract_crypto_data`: Extracts cryptocurrency data from CoinGecko.
  - `transform_crypto_data`: Transforms the extracted data into the required format.
  - `load_crypto_data_to_postgres`: Loads the transformed data into the PostgreSQL database.

Each task’s color (green for success, red for failure) provides a quick insight into the status of each run. The graphical representation helps identify the overall health of the DAG.

## 3. Docker Desktop Overview - `Docker Desktop.png`



This image shows the Docker Desktop interface with containers running for the ETL project:

- **Containers**:
  - **PostgreSQL Container (`postgres`)**: Manages the PostgreSQL database for storing the cryptocurrency data.
  - **Airflow Scheduler and Webserver Containers**: Manages the DAG scheduling and provides the user interface for Airflow.

The log output for each container displays status messages and any issues encountered, allowing real-time monitoring of the pipeline’s execution.

## 4. PostgreSQL Database - `Fetched Database.png`


This image displays the PostgreSQL database (`coingecko`) and the `crypto_data` table that stores the cryptocurrency data fetched from the API.

- **Table Structure**:
  - **Columns**: Each column represents an attribute of the cryptocurrency, such as `id`, `symbol`, `name`, `current_price`, `market_cap`, `total_volume`, `timestamp`, and more.
  - **Data**: The data includes various cryptocurrencies with their respective market metrics, prices, and timestamps.

This table acts as the destination for the ETL pipeline, storing historical cryptocurrency data for further analysis.

---

This setup demonstrates how to build a data pipeline for automated data retrieval, transformation, and storage, leveraging Apache Airflow, Docker, and PostgreSQL.
