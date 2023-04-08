import os

FLASK_HOST=os.environ.get("FLASK_HOST", "0.0.0.0")
FLASK_PORT=os.environ.get("FLASK_PORT", 5002)

MYSQL_HOST=os.environ.get("MYSQL_HOST", "localhost")
MYSQL_PORT=os.environ.get("MYSQL_PORT", 3306)
MYSQL_DB=os.environ.get("MYSQL_DB", "ipapp")
MYSQL_USER=os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD=os.environ.get("MYSQL_PASSWORD", "root")
