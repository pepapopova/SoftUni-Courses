def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for cheese_name, value in kwargs:
        result.append(cheese_name)
        quantity_list = sorted(value, reverse=True)
        result.extend(quantity_list)

    return "\n".join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)
