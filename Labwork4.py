'''
    Program purpose: To develop a Python program to perform the following tasks:
    Programmer: NOOR MARSYALINA
    Date: 8 March 2024
'''

def calculate_total_units_sold(units_sold):
    """Calculate the total number of units sold for all flowers based on the given flower sales data."""
    return sum(units_sold)

def find_highest_sales_product(product_names, units_sold):
    """Determine the flower with the highest sales among the provided flower sales data."""
    highest_sales_index = units_sold.index(max(units_sold))
    return product_names[highest_sales_index]

def find_above_average_products(product_names, customer_reviews):
    """Identify flowers with average customer reviews above 3 from the given flower sales data."""
    above_average_products = [product_names[i] for i in range(len(customer_reviews)) if customer_reviews[i] > 3]
    return above_average_products

def find_average_customer_reviews(customer_reviews):
    """Calculate the average customer review score for all flowers based on the provided flower sales data."""
    return sum(customer_reviews)/len(customer_reviews)

def find_below_average_sales(product_names, units_sold):
    """Identify flowers with below-average sales from the given flower sales, including product names, units sold, and customer reviews."""
    below_average_sales = [product_names[i] for i in range(len(units_sold)) if units_sold[i] < 100]
    return below_average_sales

# Sample lists of flower names, units sold, and customer reviews
product_names = ["Lily", "Mawar" , "Melati" , "Sepatu", "Kemboja" , "Kembuning" , "Geranium", "Matahari" , "Tulip","Kenanga" ,"Alamanda","Asoka","Amarilis","Lavender","Seruni","Puring","Rose","Ammi","Anemone", "Camelia"]
units_sold = [150,200,100,75,250,400,250,450,60,30,58,234,231,134,178,190,199,300,301,198 ]
customer_reviews = [4.5, 2.8,3.2, 4.0,3.5,8.5,10.0,7.0,2.0,2.6,3.5,1.6,4.8,5.6,7.8,1.7,9.9,5.5,3.3,3.9]

# Calculate total units sold
total_units_sold = calculate_total_units_sold(units_sold)

# Find flower with the highest sales
highest_sales_product = find_highest_sales_product(product_names, units_sold)

# Find flower with above-average customer reviews
above_average_products = find_above_average_products(product_names, customer_reviews)

# Find average customer review score
average_customer_reviews = find_average_customer_reviews(customer_reviews)

# Find below-average sales from the given flower sales, including product names, units sold, and customer reviews
below_average_sales=find_below_average_sales(product_names, units_sold)

# Display the output
print("The Total number of units sold for all flowers:", total_units_sold)
print("The highest sales of flowers:", highest_sales_product)
print("Flowers with customer reviews above 3:", above_average_products)
print("Average customer review score for all flowers :", average_customer_reviews)
print("Below-Average Sales identification on product name :", below_average_sales)


