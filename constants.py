nutrient_patterns={
    "Total Fat": r"(Total\s)?Fat\s*(\d+(\.\d+)?)(g|mg|mcg|mog|µg|%)?",
    "Saturated Fat": r"Saturated Fat\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Trans Fat": r"Trans Fat\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Cholesterol": r"Cholesterol\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Cholestrol": r"Cholestrol\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Sodium": r"Sodium\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Dietary Fiber": r"Dietary Fiber\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Total Carbohydrate": r"(Total\s)?Carbohydrates?\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Total Carb": r"(Total\s)?Carb?\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Total Carb.": r"(Total\s)Carb.?\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Total Sugars": r"(Total\s)?Sugars\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Protein": r"Protein\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Potassium": r"Potassium\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Vitamin A": r"Vitamin A\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Vitamin B6": r"Vitamin B6\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Vitamin B12": r"Vitamin B12\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Vitamin C": r"Vitamin C\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Vitamin D": r"Vitamin D\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Vitamin E": r"Vitamin E\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Vitamin K": r"Vitamin K\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Calcium": r"Calcium\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?",
    "Iron": r"Iron\s*([a-zA-Z]|\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?"
}
nutrient_correction={
    "Cholestrol":"Cholesterol",
    "Total Carb":"Total Carbohydrate",
    "Total Carb.":"Total Carbohydrate",
}
nutrients = [
"Total Fat",
"Saturated Fat",
"Trans Fat",
"Cholesterol",
"Sodium",
"Dietary Fiber",
"Total Carbohydrate",
"Total Sugars",
"Protein",
"Potassium",
"Vitamin A",
"Vitamin B6",
"Vitamin B12",
"Vitamin C",
"Vitamin D",
"Vitamin E",
"Vitamin K",
"Calcium",
"Iron"
]