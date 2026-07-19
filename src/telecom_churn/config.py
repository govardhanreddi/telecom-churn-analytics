"""Environment-based MySQL configuration."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True, slots=True)
class DatabaseConfig:
    user: str
    password: str
    host: str = "127.0.0.1"
    port: int = 3306
    database: str = "telecom_churn"

    @classmethod
    def from_environment(cls) -> "DatabaseConfig":
        user = os.getenv("MYSQL_USER", "").strip()
        password = os.getenv("MYSQL_PASSWORD", "")
        if not user or not password:
            raise RuntimeError(
                "MYSQL_USER and MYSQL_PASSWORD must be set in the environment or .env file"
            )
        try:
            port = int(os.getenv("MYSQL_PORT", "3306"))
        except ValueError as exc:
            raise RuntimeError("MYSQL_PORT must be an integer") from exc
        return cls(
            user=user,
            password=password,
            host=os.getenv("MYSQL_HOST", "127.0.0.1"),
            port=port,
            database=os.getenv("MYSQL_DATABASE", "telecom_churn"),
        )
