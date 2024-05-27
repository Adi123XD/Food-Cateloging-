import streamlit as st
import pandas as pd 
data={ 
    "_id" : "ObjectId(5dea3e3528fdfeabbd8b1d46)", 
    "Cholesterol" : 0, 
    "addedSugar" : "0", "alternateName" : "bcaa, bcaa 6000, mb bcaa", 
    "calories" : 2.56, 
    "carbs" : 0.64, 
    "createDt" : "2020-08-06 11:26:04", 
    "createdAt" : "2020-08-06T05:56:04.571Z", 
    "fat" : 0, "foodChoice" : "Veg", 
    "foodId" : 600655, "foodName" : "MuscleBlaze BCAA 6000 Tangy Orange", 
    "mealType" : "Supplement", "minerals" : {  }, 
    "monoUnsaturatedFat" : 0, 
    "polyUnsaturatedFat" : 0, 
    "protein" : 0, 
    "servingSize" : 1, 
    "servingUnit" : "Scoop", 
    "servingUnitType" : "Supplements", 
    "status" : "inactive", 
    "sugar" : 0, 
    "transFat" : 0, 
    "updateDt" : "2020-08-06 14:30:04", 
    "updatedAt" : "2020-08-06T09:00:04.392Z", 
    "vitamins" : { "vitaminD2" : 0, "vitaminD3" : 0, "vitaminD" : 0 }, 
    "weight" : 8, 
    "applicable_for_diet" : "true", 
    "include_in_diet_chat" : "false"
    }
df = pd.DataFrame(data)

# Display the DataFrame as a Streamlit table
st.write(df)