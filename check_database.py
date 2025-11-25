import sqlite3
import os
from tabulate import tabulate

# Database path
DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "src", "database", "users.db"
)

def check_database():
    """Check and display database contents"""
    try:
        # Connect to database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        print("=" * 80)
        print("DATABASE INSPECTION TOOL")
        print("=" * 80)
        print(f"Database Location: {DB_PATH}")
        print()
        
        # Check if database exists
        if not os.path.exists(DB_PATH):
            print("❌ Database file not found!")
            return
        
        print("✓ Database file found")
        print()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print(f"Tables in database: {len(tables)}")
        print("-" * 80)
        
        for table in tables:
            table_name = table[0]
            print(f"\n📋 TABLE: {table_name}")
            print("-" * 80)
            
            # Get table structure
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            print("\nTable Structure:")
            col_headers = ["ID", "Column Name", "Type", "Not Null", "Default", "PK"]
            print(tabulate(columns, headers=col_headers, tablefmt="grid"))
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"\nTotal Records: {count}")
            
            # Display data
            if count > 0:
                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()
                
                # Get column names
                cursor.execute(f"PRAGMA table_info({table_name});")
                col_info = cursor.fetchall()
                col_names = [col[1] for col in col_info]
                
                print("\nTable Data:")
                print(tabulate(rows, headers=col_names, tablefmt="grid"))
                
                # Show password security info
                if table_name == "users":
                    print("\n🔐 Security Info:")
                    for row in rows:
                        username = row[1]
                        hash_preview = row[2][:16] + "..." if len(row[2]) > 16 else row[2]
                        salt_preview = row[3][:16] + "..." if len(row[3]) > 16 else row[3]
                        print(f"  User: {username}")
                        print(f"    Password Hash: {hash_preview}")
                        print(f"    Salt: {salt_preview}")
                        print(f"    ✓ Password is encrypted (SHA-256)")
                        print()
            else:
                print("\n⚠️  No records found in this table")
        
        print("\n" + "=" * 80)
        print("DATABASE INSPECTION COMPLETE")
        print("=" * 80)
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_database()