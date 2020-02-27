import psycopg2


class Database:
    def __init__(self, host="localhost",
                 database="gmql_meta_new16_tommaso",
                 user="geco",
                 password="geco78",
                 port=5432):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

        self.conn = self.get_connection()
        self.curr = self.conn.cursor()

    def get_connection(self):
        conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port
        )
        # conn.autocommit = True
        return conn

    # def get_item_id(self, dataset_name, file_name):
    #     with self.get_connection() as conn, conn.cursor() as curr:
    #         query = f"""SELECT item_id
    #                     FROM item
    #                     NATURAL JOIN dataset
    #                     WHERE dataset_name = '{dataset_name}'
    #                     AND file_name = '{file_name}'  """
    #         curr.execute(query)
    #         row = curr.fetchone()
    #         # print("row",row)
    #         item_id = row[0]
    #         return item_id
    #
    #
    # def get_item_id2(self, dataset_name, file_name):
    #     with self.conn.cursor() as curr:
    #         query = f"""SELECT item_id
    #                     FROM item
    #                     NATURAL JOIN dataset
    #                     WHERE dataset_name = '{dataset_name}'
    #                     AND file_name = '{file_name}'  """
    #         curr.execute(query)
    #         row = curr.fetchone()
    #         # print("row",row)
    #         item_id = row[0]
    #         return item_id

    def get_item_id(self, dataset_name, file_name):
        query = f"""SELECT item_id
                    FROM item
                    NATURAL JOIN dataset
                    WHERE dataset_name = '{dataset_name}'
                    AND file_name = '{file_name}'  """
        self.curr.execute(query)
        row = self.curr.fetchone()
        # print("row",row)
        item_id = row[0]
        return item_id


    def get_item_ids(self, dataset_name):
        with self.get_connection() as conn, conn.cursor() as curr:
            query = f"""SELECT file_name, item_id
                        FROM item
                        NATURAL JOIN dataset
                        WHERE dataset_name = '{dataset_name}'  """
            curr.execute(query)
            result = {x[0]:x[1] for x in curr}
            # row = curr.fetchall()
            # print("row",row)
            # item_id = row[0]
            return result

    def copy_from(self, file, table):
        # print(file,table)
        with self.get_connection() as conn, conn.cursor() as curr:
            curr.copy_from(file, table, sep='\t', null="NULL", size=8192*16)
            conn.commit()


db = Database()




# print(db.get_item_id("GRCh38_TCGA_miRNA_expression_2018_12", "7c1b652b-91bb-446d-aef8-3d4f1b68a348-meq.bed"))
