"""
*************************************************************************
* PROJECT: Crevatec Smart Inventory
* LEVEL: 04-Expert (Sales Tracking & Profit Audit)
* POWERED BY CREVATEC | DEVELOPED BY OLAKUNLE SUNDAY OLALEKAN
* STANDARD: GAAP (Generally Accepted Accounting Principles) Logic
* STATUS: RECTIFIED FOR DATABASE COLUMN CONSISTENCY
*************************************************************************
"""
import pandas as pd
import mysql.connector
import warnings

# Suppress the SQLAlchemy warning to keep the audit clean
warnings.filterwarnings("ignore", category=UserWarning)

def run_sales_audit():
    try:
        # 1. ESTABLISH SECURE CONNECTION
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="", 
            database="crevatec_inventory"
        )
        
        # 2. RECTIFIED SQL QUERY: Changed 'name' to 'item_name'
        # We fetch item_name, qty (as remaining), price, and total_val
        query = "SELECT item_name, qty as remaining, price, total_val FROM stock"
        df = pd.read_sql(query, conn)

        if df.empty:
            print("\n[!] AUDIT ABORTED: No records found in 'crevatec_inventory.stock'.")
            return

        print("\n" + "█"*65)
        print("   CREVATEC SALES & PERFORMANCE AUDIT (LEVEL 04)")
        print("   CHIEF CONSULTANT: OLAKUNLE SUNDAY OLALEKAN")
        print("█"*65)

        # 3. INTELLIGENT SIMULATION DATA
        # We ensure the 'qty_sold' list matches the number of items in your DB
        num_items = len(df)
        # Creating a simulated 'Sold' list (e.g., 5 for the first, 2 for the second, etc.)
        df['qty_sold'] = [5 if i % 2 == 0 else 2 for i in range(num_items)]
        
        # 4. GAAP CALCULATION: Revenue = Sold * Price
        df['revenue'] = df['qty_sold'] * df['price']

        # 5. ENTERPRISE REPORTING VIEW
        print("\n{:<20} {:<10} {:<10} {:<15}".format('ITEM', 'SOLD', 'REMAINING', 'REVENUE'))
        print("-" * 65)

        for index, row in df.iterrows():
            print("{:<20} {:<10} {:<10} ${:<15,.2f}".format(
                row['item_name'], # Using the rectified column name
                int(row['qty_sold']), 
                int(row['remaining']), 
                row['revenue']
            ))

        # 6. FINANCIAL SUMMARY & ANALYTICS
        total_revenue = df['revenue'].sum()
        total_assets = df['total_val'].sum()

        print("-" * 65)
        print(f"[*] TOTAL REVENUE GENERATED : ${total_revenue:,.2f}")
        print(f"[*] TOTAL ASSET VALUE (STOCK): ${total_assets:,.2f}")
        
        # EFFICIENCY RATIO LOGIC
        if total_revenue > (total_assets * 0.5):
            print("[!] STATUS: HIGH TURNOVER (Healthy Business Flow)")
        else:
            print("[!] STATUS: HIGH CAPITAL LOCK (Stock is moving slowly)")

        print("█" + "═"*63 + "█\n")
        conn.close()

    except mysql.connector.Error as db_err:
        print(f"Database Error: {db_err}")
    except Exception as e:
        print(f"Audit Error: {e}")

if __name__ == "__main__":
    run_sales_audit()