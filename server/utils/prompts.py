ANALYZE_SUPPLEMENTS_PROMPT = """

"""

ANALYZE_FOOD_PROMPT = """
Analyze this food label ingredient text. Categorize each ingredient into ONE of these 7 categories and group all related ingredients into each category.
Only sort them into one of the 7 categories and do not provide any explanations. If a category is empty, don't include it.

1. **Sugars & Sweeteners** 
2. **Fats & Oils** 
3. **Preservatives & Additives**
4. **Proteins**
5. **Grains & Starches**
6. **Salt & Sodium**
7. **Vitamins & Minerals**

In addition, create a summary of concern separating each ingredient into one of these 3 categories which negatively impact health. Include a brief explanation of what they are and why it belongs there if the ingredient name is not obvious to an average person
- High Concern
- Medium Concern
- Low Concern

Do below only if it is available

If tabular data is found such as nutritional information, create a summary table listing the key nutritional facts such as calories, fats, sugar, sodium, cholestrol, protein and fiber.

For serving size, provide a real life example that uses that amount or a practical application of it.
"""
