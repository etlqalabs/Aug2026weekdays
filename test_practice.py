import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

# Create a connection string
mysql_tgt_conn = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/aug_2026")
oracle_src_conn = create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe")
# Compare between source ( oracle) and target (mysql) and report test status
def test_compare_data():
    query_source = "select * from product"
    df_source_oracle = pd.read_sql(query_source, oracle_src_conn)

    query_target = "select * from product"
    df_target_mysql = pd.read_sql(query_target, mysql_tgt_conn)

    assert df_source_oracle.equals(df_target_mysql),"data between source and target does not match"