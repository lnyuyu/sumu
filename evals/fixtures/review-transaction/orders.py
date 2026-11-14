def with_transaction(conn, action):
    conn.begin()
    try:
        result = action(conn)
        conn.commit()
        return result
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.release()


def save_order(conn, order):
    return with_transaction(conn, lambda c: c.insert("orders", order))
