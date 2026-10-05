import argparse
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

from settings import Settings

ROOT = Path(__file__).parent


def export_envs(environment: str = "dev") -> None:

    env_path = ROOT / "config" / f".env.{environment}"

    load_dotenv(env_path)


def export_secrets_yaml(path: Path) -> None:
    with open(path, "r") as f:
        secrets_yaml = yaml.safe_load(f)
        os.environ["API_KEY"] = secrets_yaml["API_KEY"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets_yaml(ROOT / "secrets.yaml")

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY", settings.API_KEY)
