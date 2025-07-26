import csv
from database import products_col

def load_csv_to_db(csv_file_path):
    with open(csv_file_path, newline=' ') as csvfile:
        reader = csv.DictReader(csvfile)
        products = [row for row in reader]
        if products:
            products_col.insert_many(products)
            print("Products loaded successfully.")
if __name__ == "__main__":
    load_csv_to_db("data/products.csv")