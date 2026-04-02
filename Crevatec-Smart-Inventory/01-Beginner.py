"""
*************************************************************************
* PROJECT: Crevatec Smart Inventory
* LEVEL: 01-Beginner
* POWERED BY CREVATEC | DEVELOPED BY OLAKUNLE SUNDAY OLALEKAN
* COLOR THEME: Wet Asphalt (#34495E)
* STATUS: 100% Visible Source - No Hidden Logic.
*************************************************************************
"""

def inventory_engine():
    # Standardized Data Structure for Inventory
    items = []
    
    print("=== CREVATEC INVENTORY CORE v1.0 ===")
    while True:
        entry = input("\nCommands: [add] [view] [exit]: ").lower()
        
        if entry == 'add':
            name = input("Item: ")
            qty = int(input("Qty: "))
            price = float(input("Price: "))
            items.append({"name": name, "qty": qty, "price": price})
            print(f"Record Saved: {name}")
            
        elif entry == 'view':
            print("-" * 30)
            for i in items:
                # Core Logic: Value Calculation
                val = i['qty'] * i['price']
                print(f"{i['name']} | Stock: {i['qty']} | Value: ${val:.2f}")
            print("-" * 30)
            
        elif entry == 'exit':
            break

if __name__ == "__main__":
    inventory_engine()