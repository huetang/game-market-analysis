from database import get_connection


def load_dataframe(df, table_name):

    print(f"\nLoading {table_name}...")
    print(df.head())

    conn = get_connection()

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    conn.commit()
    conn.close()

    print(f"{table_name} loaded successfully.")