import psycopg2
from psycopg2 import sql

class PGMetadata:
    def __init__(
            self,
            schema_name,
            table_name,
            host="localhost",
            port="5432",
            database="test",
            user="username",
            password="password"
        ) -> None:
        
        # Establish a connection to the PostgreSQL database
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        self.fetch_table_metadata(schema_name, table_name)

    def fetch_table_metadata(self, schema_name, table_name):
        # Create a cursor object using the connection
        cur = self.conn.cursor()

        # Use the psycopg2.sql.SQL class to safely format the SQL query
        query = sql.SQL("SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = {} AND table_name = {}").format(
            sql.Identifier(schema_name),
            sql.Identifier(table_name)
        )
        
        # Execute the query
        cur.execute(query)

        # Fetch all rows from the result set
        rows = cur.fetchall()

        self.metadata = {}
        # Print the column names and data types
        for row in rows:
            # row[0] = column_name
            # row[1] = data_type
            self.metadata[row[0]] = row[1]

        # Close the cursor and connection
        cur.close()
        
    def getMetadata(self):
        return self.metadata
    
    def __del__(self):
        self.conn.close()