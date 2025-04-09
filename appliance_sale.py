import random
import matplotlib.pyplot as plt
import pandas as pd


def create_csv():
    product_sales_data = []

    dates = pd.date_range(start="2025-01-01", periods=60, freq="D")

    products = ["AC", "TV", "Refrigerator", "Washing Machine"]

    for date in dates:
        product = random.choice(products)
        unit_sold = random.randint(20,30)
        unit_price = random.randint(10000, 30000)

        product_sales_data.append([date.strftime("%Y-%m-%d"), product, unit_sold, unit_price])

    df = pd.DataFrame(product_sales_data ,columns=["Date", "Product","Unit Sold", "Unit Price"])
    df.to_csv("product_sales_data.csv", index = False)
    return df

def analyse():
    df = pd.read_csv("../product_sales_data.csv")
    print(df.head())
    print(df.describe())

    df["Total Sale"] = df["Unit Sold"]*df["Unit Price"]

    daily_total_sale = df.groupby("Date")["Total Sale"].sum()
    best_day = daily_total_sale.idxmax()
    worst_day = daily_total_sale.idxmin()

    print(f"Daily Total sale: ${daily_total_sale}")
    print(f"Best Day: {best_day}")
    print(f"Worst Day: {worst_day}")
    total_sale_product_wise = df.groupby("Product")["Total Sale"].sum()
    print(f"Total Sale Product-wise: ${total_sale_product_wise}")
    best_seller = total_sale_product_wise.idxmax()
    worst_seller = total_sale_product_wise.idxmin()

    print(f"Best Seller: {best_seller}")
    print(f"Worst Seller: {worst_seller}")

    average_sell = df.groupby("Date")["Total Sale"].mean().round(2)

    print(f"Average Daily Sale: ${average_sell}")

    return total_sale_product_wise


def visualize(data):

    plt.figure(figsize=(10,5))

    data.plot(kind="bar", color="green")

    plt.title("Product-Wise Total Sale")
    plt.xlabel("Product")
    plt.ylabel("Total Sale")

    plt.tight_layout()
    plt.savefig("Appliance_sales_analysis.png")
    plt.show()



def main():
    create_csv()
    total_sale_product_wise = analyse()
    visualize(total_sale_product_wise)


if __name__ == "__main__":
    main()