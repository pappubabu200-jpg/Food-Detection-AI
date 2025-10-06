import requests
USDA_API_KEY='your_usda_api_key_here'
def get_nutrition(food_name):
    url=f'https://api.nal.usda.gov/fdc/v1/foods/search?query={food_name}&api_key={USDA_API_KEY}'
    response = requests.get(url)
    return response.json() if response.status_code==200 else None