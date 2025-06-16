country_codes = {
    "US": "United States",
    "IN": "India",
    "GB": "United Kingdom",
    "CA": "Canada",
    "AU": "Australia"
}

def get_country_name(code):
    return country_codes.get(code.upper(), "Not found")


codes_to_check = ["US", "IN", "FR", "CA", "BR"]

for code in codes_to_check:
    print(f"Country code: {code}, Country name: {get_country_name(code)}")

