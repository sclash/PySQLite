# sudo apt update -y
# sudo apt install -y sqlite3

# echo "SQLite installed successfully."

sqlite3 name.db
DB_FILE="./name.db"
SQL_COMMANDS="
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO users (name) VALUES ('John Doe');
INSERT INTO users (name) VALUES ('Jane Smith');
"

# Execute the SQL commands using the sqlite3 command-line tool
echo "$SQL_COMMANDS" | sqlite3 "$DB_FILE"  