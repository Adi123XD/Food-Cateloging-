nutrient_patterns={
    "weight":r'\(\s*(\d+(\.\d+)?)\s*(g|mg|ml)\s*\)|\(\s*(\d+(\.\d+)?)\s*\)|(serving\s*size)\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg)',
    "servingUnit":r'(\d+)\s*(?:[a-z]*)?\s*(cup|scoop|katori|tablespoon)',
    "calories":r'(energy|calorie|calories)\s*\(\s*(kcal)\s*\)\s*(\d+(\.\d+)?)|(energy|calorie|calories)\s*(\d+(\.\d+)?)\s*(kcal)?',
    "fat": r"(((total\s*)?fat|lipides?)\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|((total\s*)?fat|lipides?)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "saturatedFat": r"(saturated\s*(fat|fatty\s*acids)\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|saturated\s*(fat|fatty\s*acids)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?|saturés?\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?|saturés?\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?)",
    "polyUnsaturatedFat":r"(poly\s*unsaturated\s*(fat|fatty\s*acids)\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|poly\s*unsaturated\s*(fat|fatty\s*acids)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "monoUnsaturatedFat":r"(mono\s*unsaturated\s*(fat|fatty\s*acids)\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|mono\s*unsaturated\s*(fat|fatty\s*acids)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "transFat": r"(trans\s*((fat|fatty\s*acids))?\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|trans\s*((fat|fatty\s*acids))?\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "Cholesterol": r"((cholesterol|cholestrol|cholestérol)\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|(cholesterol|cholestrol|cholestérol)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "sodium": r"(sodium\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|sodium\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "fibre": r"((dietary\s*)?(fiber|fibre)s?\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|(dietary\s*)?(fiber|fibre)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "carbs": r"((total\s*)?(carbohydrates?|carb|carb\.)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?|(total\s*)?(carbohydrates?|carb|carb\.)\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?)",
    "glucides":r"(glucides?\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?|(total\s*)?glucides?\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?)",
    "sugar": r"((total\s*)?(sugars?|sucres)\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|(total\s*)?(sugars?|sucres)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "addedSugar":r'((added\s*)(sugars?|sucres)\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|(added\s*)(sugars?|sucres)\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)',
    "protein": r"(proteins?\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|proteins?\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?|protéines?\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?|protéines?\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?)",
    "potassium": r"(potassium\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|potassium\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "vitaminA": r"(vitamin\s*a\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|vitamin\s*a\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "vitaminB6": r"(vitamin\s*b6\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|vitamin\s*b6\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "vitaminB12": r"(vitamin\s*b12\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|vitamin\s*b12\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "vitaminC": r"(vitamin\s*c\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|vitamin\s*c\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "vitaminD": r"(vitamin\s*d\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|vitamin\s*d\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "vitaminE": r"(vitamin\s*e\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|vitamin\s*e\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "vitaminK": r"(vitamin\s*k\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|vitamin\s*k\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "calcium": r"(calcium\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|calcium\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)",
    "iron": r"((i|f)ron\s*<?\s*(\d+(\.\d+)?)\s*(g|mg|mcg|mog|µg|%)?|(i|f)ron\s*\((\s*g\s*|\s*mg\s*|\s*mcg\s*|\s*mog\s*|\s*µg\s*|%)\)\s*(\d+(\.\d+)?)?)"
}
nutrient_correction={
    "glucides":"carbs",
}
nutrients = [
"weight",
"servingUnit",
"calories",
"fat",
"saturatedFat",
"polyUnsaturatedFat",
"monoUnsaturatedFat",
"transFat",
"Cholesterol",
"sodium",
"fibre",
"carbs",
"sugar",
"addedSugar",
"protein",
"potassium",
"vitaminA",
"vitaminB6",
"vitaminB12",
"vitaminC",
"vitaminD",
"vitaminE",
"vitaminK",
"calcium",
"iron"
]
ignore_content=[
    "original_image_link",
    "addedSugar",
    "calories",
    "servingUnit"
]
# order of the features used to build the model
correct_order = [
    "Cholesterol", "carbs", "fat", "fibre", "monoUnsaturatedFat",
    "polyUnsaturatedFat", "protein", "transFat", "weight", "sugar",
    "vitaminC", "vitaminE", "vitaminD", "vitaminK", "vitaminB6",
    "vitaminA", "vitaminB12", "potassium", "calcium", "saturatedFat",
    "sodium", "iron"
]
class_label = ["Unhealthy","Healthy"]