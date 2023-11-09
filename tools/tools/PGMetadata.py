import psycopg2
from psycopg2 import sql

import logging
log = logging.getLogger()

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
        # query = sql.SQL("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'Verbindungspunkte' and table_schema = 'detailnetz'").format(
        query = sql.SQL(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name =  '{table_name}'  and table_schema = '{schema_name}'")

        # Execute the query
        cur.execute(query)

        # Fetch all rows from the result set
        rows = cur.fetchall()

        self.metadata = {}
        # Print the column names and data types
        log.debug(f'rows = {rows}')
        log.debug("\tcolumn_name\t|\tdata_type")
        for row in rows:
            # row[0] = column_name
            # row[1] = data_type
            log.debug(f"\t{row[0]}\t|\t{row[1]}")
            self.metadata[row[0]] = row[1]

        query_geo = sql.SQL(f"SELECT f_geometry_column,type,srid FROM geometry_columns WHERE f_table_schema = '{schema_name}' AND f_table_name = '{table_name}'")
        cur.execute(query_geo)
        rows_geo = cur.fetchall()
        log.debug(f'rows_geo = {rows_geo}')
        geom_col = rows_geo[0][0]
        geom_type = rows_geo[0][1]
        srid = rows_geo[0][2]
        self.metadata[geom_col]={"type": geom_type, "srid": srid}
        log.debug(f"self.metadata = {self.metadata}")
        # Close the cursor and connection
        cur.close()
        
    def getMetadata(self):
        return self.metadata
    
    def __del__(self):
        self.conn.close()