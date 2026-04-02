"""
*************************************************************************
* PROJECT: Crevatec Smart Inventory (Enterprise SQLite Edition)
* LEVEL: 04-Expert (Business Intelligence & Sales Audit)
* POWERED BY CREVATEC | DEVELOPED BY OLAKUNLE SUNDAY OLALEKAN
* STATUS: Standardized for Investment-Grade Portfolio.
*************************************************************************
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings
import os

# --- 1. SYSTEM CALIBRATION ---
warnings.filterwarnings("ignore", category=UserWarning)

# --- 2. DATABASE ENGINE (Standardized for Production) ---
def initialize_local_db():
    db_file = "crevatec_inventory.db"
    exists = os.path.exists(db_file)
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # REAL-WORLD SCHEMA: Tracking the "Flow of Goods"
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            opening_qty INTEGER,
            qty_sold INTEGER,
            remaining_qty INTEGER,
            unit_price REAL,
            total_asset_val REAL,
            revenue REAL
        )
    """)

    # Seed data only if the DB is brand new
    if not exists:
        print("[!] New Enterprise DB Detected. Seeding Market-Ready Data...")
        # (Name, Opening, Sold, Remaining, Price, Total Asset Val, Revenue)
        sample_data = [
            ('Industrial Drill', 50, 10, 40, 500.0, 20000.0, 5000.0),
            ('Safety Helmet', 100, 85, 15, 25.0, 375.0, 2125.0),
            ('Heavy Boots', 60, 45, 15, 120.0, 1800.0, 5400.0),
            ('Work Gloves', 200, 195, 5, 10.0, 50.0, 1950.0),
            ('Power Saw', 30, 2, 28, 450.0, 12600.0, 900.0)
        ]
        cursor.executemany("""
            INSERT INTO stock (item_name, opening_qty, qty_sold, remaining_qty, unit_price, total_asset_val, revenue) 
            VALUES (?,?,?,?,?,?,?)""", sample_data)
        conn.commit()
    
    return conn

# --- 3. THE STRATEGIC AUDIT ENGINE ---
def run_enterprise_audit(conn):
    # Fetching the full ledger
    df = pd.read_sql("SELECT * FROM stock", conn)

    if df.empty:
        print("CRITICAL: Database empty. No assets to analyze.")
        return

    # --- FINANCIAL LOGIC: Performance Metrics ---
    total_revenue = df['revenue'].sum()
    total_assets = df['total_asset_val'].sum()
    
    print("\n" + "█"*65)
    print("   CREVATEC SALES & PERFORMANCE AUDIT (SQLITE ENTERPRISE)")
    print("   CHIEF CONSULTANT: OLAKUNLE SUNDAY OLALEKAN")
    print("█" * 65)
    
    print(f"[*] TOTAL REVENUE GENERATED : ${total_revenue:,.2f}")
    print(f"[*] TOTAL ASSET VALUE (STOCK): ${total_assets:,.2f}")
    
    # Financial Status Trigger (Capital Lock Logic)
    if total_assets > (total_revenue * 1.5):
        print("[!] STATUS: HIGH CAPITAL LOCK (Warning: Cash flow is restricted)")
    else:
        print("[!] STATUS: EFFICIENT FLOW (Stock is moving profitably)")
    print("-" * 65)

    # --- AI ANALYTICS: Predicting Potential Revenue ---
    # We train the model to understand the relationship between Stock and Profit
    model = LinearRegression().fit(df[['qty_sold']], df['revenue'])
    
    # --- 4. VISUALIZATION: The CEO Dashboard ---
    plt.style.use('dark_background') # Using professional high-contrast theme
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Side-by-side comparison of Sold vs Remaining
    items = df['item_name']
    sold = df['qty_sold']
    remaining = df['remaining_qty']

    ax.bar(items, sold, label='Units Sold (Liquid Cash)', color='#27AE60')
    ax.bar(items, remaining, bottom=sold, label='Remaining Stock (Locked Assets)', color='#E74C3C')

    plt.title("Crevatec Inventory Intelligence: Sales vs. Asset Ratio", fontsize=14, fontweight='bold')
    plt.ylabel("Quantity of Units")
    plt.xlabel("Product Name")
    plt.legend()
    
    print("\n[+] Audit Complete. Visualization generated for stakeholder review.")
    plt.tight_layout()
    plt.show()

# --- EXECUTION ---
if __name__ == "__main__":
    db_conn = initialize_local_db()
    run_enterprise_audit(db_conn)
    db_conn.close()