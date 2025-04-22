
import sqlite3

def init_db():
    conn = sqlite3.connect("threats.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS threats (pattern TEXT, severity TEXT)")
    cur.execute("INSERT INTO threats VALUES ('attack', 'high')")
    cur.execute("INSERT INTO threats VALUES ('scan', 'medium')")
    cur.execute("INSERT INTO threats VALUES ('malicious', 'critical')")
    conn.commit()
    conn.close()

def load_threats():
    conn = sqlite3.connect("threats.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM threats")
    rows = cur.fetchall()
    conn.close()
    patterns = [r[0] for r in rows]
    severity = {r[0]: r[1] for r in rows}
    return patterns, severity
