SYSTEM_PROMPTS = {

}

ANALYZE_FOOD_PROMPT = """
Analyze this food label ingredient text. Categorize each ingredient into ONE of these 7 categories and group all related ingredients into each category.
Only sor tthem into one of the 7 categories and do not provide any explanations

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
"""
