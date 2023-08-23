import pandas as pd
import json

# Load the JSON data into a dictionary (replace 'path_to_file.json' with your file path)
file_path = 'coupons.json'
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Extract the "coupons" data
coupons_data = json_data["coupons"]

# Convert the "coupons" data to a pandas DataFrame
coupons_df = pd.DataFrame(coupons_data)


def count_coupon_types(df):
    coupon_type_count = df["promotion_type"].value_counts().to_dict()

    formatted_coupon_count = {}
    for coupon_type, count in coupon_type_count.items():
        formatted_coupon_count[coupon_type] = count

    return formatted_coupon_count


def get_stats():
    response = dict()
    promo_stats = dict()

    # Calculate coupon type counts
    promo_stats['coupon_type_counts'] = {
        "buy_one_get_one": len(coupons_df[coupons_df["promotion_type"] == "buy-one-get-one"]),
        "dollar_off": len(coupons_df[coupons_df["promotion_type"] == "dollar-off"]),
        "free_gift": len(coupons_df[coupons_df["promotion_type"] == "free-gift"]),
        "free_shipping": len(coupons_df[coupons_df["promotion_type"] == "free-shipping"]),
        "percent_off": len(coupons_df[coupons_df["promotion_type"] == "percent-off"])
    }

    # Calculate percent-off coupon statistics
    percent_off_coupons = coupons_df[coupons_df["promotion_type"] == "percent-off"]
    promo_stats['discount_coupon_percentage'] = {
        "avg_discount": percent_off_coupons["value"].mean(),
        "max_discount": percent_off_coupons["value"].max(),
        "min_discount": percent_off_coupons["value"].min(),
        "number_of_dollar_off_coupons": len(percent_off_coupons)
    }

    # Calculate dollar-off coupon statistics
    dollar_off_coupons = coupons_df[coupons_df["promotion_type"] == "dollar-off"]
    promo_stats['dollar_discount'] = {
        "avg_discount": dollar_off_coupons["value"].mean(),
        "max_discount": dollar_off_coupons["value"].max(),
        "min_discount": dollar_off_coupons["value"].min(),
        "number_of_dollar_off_coupons": len(dollar_off_coupons)
    }

    response['promo_stats'] = promo_stats

    # Group by retailer and calculate statistics
    grouped_results = dollar_off_coupons.groupby('webshop_id')['value'].agg(['count', 'min', 'max', 'mean'])

    # Rename columns for clarity
    grouped_results.rename(columns={'count': 'number_of_coupons', 'min': 'min_discount', 'max': 'max_discount',
                                    'mean': 'avg_discount'}, inplace=True)

    # Convert the grouped results DataFrame to a dictionary
    results_dict = grouped_results.to_dict(orient='index')
    response['retailer'] = results_dict

    return response
