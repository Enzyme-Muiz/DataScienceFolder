from abc import ABC, abstractmethod
from typing import Optional, Dict, Any


class SQLCRUD(ABC):
    """
    Abstract base class for SQL CRUD operations.
    """

    def _init_(self, connection_params: dict):
        self.connection_params = connection_params
        self.connection = None
        self.query = None

    @abstractmethod
    def connect(self):
        """
        Establish a database connection.
        """
        pass

    @abstractmethod
    def build_query(self, sql_file_path: str, params: Optional[Dict[str, Any]] = None):
        """
        Build SQL query from a .sql file and optional parameters.
        """
        pass

    @abstractmethod
    def read_data(self):
        """
        Execute the built query and return the results.
        """
        pass

    def close_connection(self):
        """
        Close the database connection if open.
        """
        if self.connection:
            self.connection.close()
            self.connection = None


from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from typing import Optional, Dict, Any


class SQLServerCRUD(SQLCRUD):
    """
    Concrete implementation of SQLCRUD for SQL Server using SQLAlchemy.
    Designed for NMTR training and imputation queries.
    """

    def _init_(self, connection_string: str):
        super()._init_({"connection_string": connection_string})
        self.engine = None
        self.params: Dict[str, Any] = {}


def connect(self):
    connection_url = URL.create(
        "mssql+pyodbc",
        query={"odbc_connect": self.connection_params["connection_string"]},
    )
    self.engine = create_engine(connection_url)


def build_query(
    self,
    sql: Optional[str] = None,
    sql_file_path: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
):
    """
    Build query from either:
    - raw SQL string
    - .sql file path
    """

    if sql_file_path:
        with open(sql_file_path, "r") as file:
            sql = file.read()

    if not sql:
        raise ValueError("Either sql or sql_file_path must be provided")

    self.query = sql
    self.params = params or {}


def read_data(self):
    import pandas as pd

    """
 Executes the query. For SELECT returns results,
 for DDL (like SELECT INTO) just executes.
 """
    if not self.engine:
        raise ValueError("Connection not established")

    if not self.query:
        raise ValueError("Query not built")

    with self.engine.begin() as conn:
        result = conn.execute(text(self.query), self.params)

    # Try fetching (will fail for DDL, so handle gracefully)
    try:
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df
    except:
        return None
