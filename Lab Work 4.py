class FlowerShopAnalyzer:
    def __init__(self, product_names, units_sold, customer_reviews):
        self.product_names = product_names
        self.units_sold = units_sold
        self.customer_reviews = customer_reviews

    def calculate_total_units_sold(self):
        return sum(self.units_sold)

    def identify_highest_sales(self):
        max_sales_index = self.units_sold.index(max(self.units_sold))
        return self.product_names[max_sales_index]

    def identify_above_average_reviews(self, threshold=3):
        above_average_flowers = [
            self.product_names[i]
            for i, review in enumerate(self.customer_reviews)
            if review > threshold
        ]
        return above_average_flowers

    def calculate_average_review_score(self):
        return sum(self.customer_reviews) / len(self.customer_reviews)

    def identify_below_average_sales(self):
        average_sales = sum(self.units_sold) / len(self.units_sold)
        below_average_flowers = [
            {
                "product_name": self.product_names[i],
                "units_sold": self.units_sold[i],
                "customer_review": self.customer_reviews[i],
            }
            for i, sales in enumerate(self.units_sold)
            if sales < average_sales
        ]
        return below_average_flowers

# Dataset
product_names = ["Rose", "Lily", "Tulip", "Sunflower", "Daisy", "Orchid", "Daffodil", "Peony", "Marigold", "Hydrangea",
                 "Carnation", "Iris", "Gerbera", "Snapdragon", "Chrysanthemum", "Lavender", "Pansy", "Zinnia",
                 "Poppy", "Ranunculus"]
units_sold = [220, 250, 100, 180, 250, 302, 410, 100, 360, 230, 400, 150, 140, 160, 510, 475, 98, 321, 212, 32]
customer_reviews = [4.5, 3.8, 2.2, 4.0, 3.5, 3.0, 4.0, 3.2, 4.6, 2.3, 2.6, 3.0, 3.9, 3.5, 4.7, 4.8, 2.1, 3.3, 3.8, 3.6]

# Create instance of the FlowerShopAnalyzer
flower_shop_analyzer = FlowerShopAnalyzer(product_names, units_sold, customer_reviews)

# Task 1: Calculate total units sold
total_units_sold = flower_shop_analyzer.calculate_total_units_sold()
print(f"Total units sold: {total_units_sold}")

# Task 2: Identify flower with the highest sales
highest_sales_flower = flower_shop_analyzer.identify_highest_sales()
print(f"The flower with the highest sales is: {highest_sales_flower}")

# Task 3: Identify flowers with above-average customer reviews
above_average_reviews_flowers = flower_shop_analyzer.identify_above_average_reviews()
print(f"Flowers with above-average reviews: {above_average_reviews_flowers}")

# Task 4: Calculate average customer review score
average_review_score = flower_shop_analyzer.calculate_average_review_score()
print(f"Average customer review score: {average_review_score:.2f}")

# Task 5: Identify flowers with below-average sales
below_average_sales_flowers = flower_shop_analyzer.identify_below_average_sales()
print("Flowers with below-average sales:")
for flower in below_average_sales_flowers:
    print(
        f"Product: {flower['product_name']}, Units Sold: {flower['units_sold']}, Customer Review: {flower['customer_review']}"
    )
