a = {'apple': {'fruit': "a", "test": "b"}, 'beetroot': 'vegetable', 'cake': 'dessert'}

new = {fruit for (fruit, category) in a.items()}

print(new)