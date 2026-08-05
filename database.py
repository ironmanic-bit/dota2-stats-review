import aiosqlite
import asyncio
from datetime import datetime, timedelta

db_path = "dota.db"

async def init_db():
    async with aiosqlite.connect(db_path) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS players (
                account_id INTEGER PRIMARY KEY,
                nickname TEXT,
                last_matches_count INTEGER
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS matches (
                match_id INTEGER PRIMARY KEY,
                account_id INTEGER,
                win BOOLEAN,
                hero_id INTEGER,
                kills INTEGER,
                deaths INTEGER,
                match_date TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES players (account_id)
            )
        """)
        await db.commit()

async def save_player(account_id, nickname, matches_count):
    async with aiosqlite.connect(db_path) as db:
        await db.execute("""
            INSERT OR REPLACE INTO players (account_id, nickname, last_matches_count)
            VALUES (?, ?, ?)
        """, (account_id, nickname, matches_count))
        await db.commit()


async def save_matches(account_id, matches_data):
    async with aiosqlite.connect(db_path) as db:
        values = []
        for match in matches_data:
            values.append((
                match['match_id'],
                account_id,
                match.get('win', False),
                match.get('hero_id', 0),
                match.get('kills', 0),
                match.get('deaths', 0),
                datetime.fromtimestamp(match.get('start_time', 0))
            ))
        
        await db.executemany("""
            INSERT OR REPLACE INTO matches (
                match_id, account_id, win, hero_id, kills, deaths, match_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, values)
        await db.commit()


async def get_cached_matches(account_id, limit_matches=15):
        try:
            async with aiosqlite.connect(db_path) as db:
                db.row_factory = aiosqlite.Row
                async with db.execute(
                    "SELECT last_matches_count FROM players WHERE account_id = ?",
                    (account_id,)
                ) as cursor:
                    cached_count = (await cursor.fetchone())[0]


                async with db.execute(
                    "SELECT COUNT(*) FROM matches WHERE account_id = ?",
                    (account_id,)
                ) as cursor2:
                    actual_count = (await cursor2.fetchone())[0]

                if actual_count < limit_matches:
                    return None
                
                async with db.execute(
                    "SELECT * FROM matches WHERE account_id = ? ORDER BY match_date DESC LIMIT ?",
                    (account_id, limit_matches)
                ) as cursor3:
                    rows = await cursor3.fetchall()
                    return [dict(row) for row in rows]
        
        except Exception as e:
            print(f"Ошибка База данных: {e}")
            return None

async def test_db(account_id):
    async with aiosqlite.connect(db_path) as db:
        async with db.execute(
            "SELECT * FROM matches WHERE account_id = ?",
            (account_id,)
        ) as cursor:
            matches = await cursor.fetchall()
            print(f"Найдено матчей: {len(matches)}")
            if matches:
                print(f"Первый матч: {matches[0]}")
            return matches

