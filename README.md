
# Cryptocurrency Data Pipeline

This project retrieves data for 10 cryptocurrencies daily using the CoinGecko API, transforms it using Python, and stores the results in a PostgreSQL database. The pipeline is designed for easy scheduling and automation, making it suitable for external use.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Overview
The pipeline retrieves data from CoinGecko, performs transformations on the data, and saves it to a PostgreSQL database. This data can then be used for analysis and insights on cryptocurrency trends.

## Features
- Fetches data for 10 cryptocurrencies daily
- Performs data transformations using Python
- Stores data in a PostgreSQL database for easy access and analysis
- Configurable for different intervals and cryptocurrencies

## Requirements
- Python 3.12 or higher
- PostgreSQL database
- Python packages listed in `requirements.txt`

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/cryptocurrency-pipeline.git
    cd cryptocurrency-pipeline
    ```

2. **Set Up Python Environment**

    It's recommended to use a virtual environment.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up PostgreSQL Database**

    - Ensure PostgreSQL is installed and running.
    - Create a new database and configure the connection in the `coingeckopipe.py` file or a `.env` file.

5. **Configure Environment Variables**

    You may want to store database connection details and any API keys (if needed) in an `.env` file. 

    Create a `.env` file with the following variables:

    ```plaintext
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

6. **Run the Script**

    Run the script to start the data pipeline:

    ```bash
    python coingeckopipe.py
    ```

## Usage

To automate the pipeline, you can use tools like **Apache Airflow** or **cron jobs** to run the script at desired intervals.

## License

This project is licensed under the MIT License.
