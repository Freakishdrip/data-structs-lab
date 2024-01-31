spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [resturant["name"] for resturant in spicy_foods]
    # print(names)
    return names

def get_spiciest_foods(spicy_foods):
    arr = []
    for rest in spicy_foods:
      if(rest["heat_level"] > 5):
        arr.append(rest)
      
    # print(arr)
    return arr
#get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
  
  for i in spicy_foods:
    rest_name = (i["name"])
    rest_cuisine = (i["cuisine"])
    rest_heat = (i["heat_level"])
    # print(rest_heat, rest_cuisine, rest_name)
    
    # rest_cuisine = [rest("cuisine")]
    # rest_spicy = [rest("heat_level")]
    heat_in_peppers = "🌶" * rest_heat 
    print(f"{rest_name} ({rest_cuisine}) | Heat Level: {heat_in_peppers}")
#print_spicy_foods(spicy_foods)
  

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
  
  for rest in spicy_foods:
    
    rest_cuisine = (rest["cuisine"])
    
    if rest_cuisine == cuisine:
      print(rest)
      return rest
   
     
    # find_rest = [rest["cuisine"] == cuisine ]
    # if find_rest:
    #   return rest
  
  
  # for i in spicy_foods:
  #   print(i)
  #   if i["cuisine"] == cuisine:
  #     return i
  #   else:
  #     return
get_spicy_food_by_cuisine(spicy_foods, "Thai")


def print_spiciest_foods(spicy_foods): #greater than 5 and syntax = Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
  
  for rest in spicy_foods:
    if(rest["heat_level"] > 5):
      rest_name = (rest["name"])
      rest_cuisine = (rest["cuisine"])
      rest_heat = (rest["heat_level"])
      heat_in_peppers = "🌶" * rest_heat 
      print(f"{rest_name} ({rest_cuisine}) | Heat Level: {heat_in_peppers}")

def get_average_heat_level(spicy_foods):
  heat_arr =[]
  for rest in spicy_foods:
    rest_heat = (rest["heat_level"])
    heat_arr.append(rest_heat)
  print(heat_arr)
  average_heat = sum(heat_arr) / len(heat_arr)
  print(average_heat)
  return average_heat
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
  spicy_foods.append(spicy_food)
  return spicy_foods