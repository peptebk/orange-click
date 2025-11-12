import sqlite3

def load_state():
    conn = sqlite3.connect('save.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS state (
        id INTEGER PRIMARY KEY, counter INTEGER, multiplier INTEGER, upgrade_cost INTEGER
    )''')
    c.execute('SELECT counter, multiplier, upgrade_cost FROM state WHERE id=1')
    row = c.fetchone()
    conn.close()
    if row:
        return {'counter': row[0], 'multiplier': row[1], 'upgrade_cost': row[2]}
    else:
        return {'counter': 0, 'multiplier': 1, 'upgrade_cost': 25}

def save_state(counter, multiplier, upgrade_cost):
    conn = sqlite3.connect('save.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS state (
        id INTEGER PRIMARY KEY, counter INTEGER, multiplier INTEGER, upgrade_cost INTEGER
    )''')
    c.execute('''INSERT OR REPLACE INTO state (id, counter, multiplier, upgrade_cost) VALUES (1, ?, ?, ?)''',
              (counter, multiplier, upgrade_cost))
    conn.commit()
    conn.close()
