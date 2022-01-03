import day15_project_data as data


ingredients = data.MENU["espresso"]['ingredients']
resources = data.resources

for i in resources:
    if i in ingredients:
        print(i)
        
        print(resources[i] - ingredients[i])