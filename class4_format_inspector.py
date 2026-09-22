import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    df = pd.read_csv(filepath)
    logger.info("Loaded CSV file: %s", filepath)
    print(df.head(3))


def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    logger.info("Loaded JSON file: %s", filepath)
    print(data)


def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    with open(filepath, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    logger.info("Loaded YAML file: %s", filepath)
    print(data)


def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]

    logger.info(".env file loaded")
    print(keys)


def main():
    data_dir = Path("data")

    csv_path = data_dir/"sample.csv"
    json_path = data_dir/"sample.json"
    yaml_path = data_dir/"sample.yaml"

    inspect_csv(csv_path)
    inspect_json(json_path)
    inspect_yaml(yaml_path)
    inspect_env()


if __name__ == "__main__":
    main()
