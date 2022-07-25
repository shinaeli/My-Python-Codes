def car_info(manufacturer, model, **car_infos):
    car_infos['manufacturer_name'] = manufacturer.title()
    car_infos['model_name'] = model.title()
    return car_infos


car1 = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car1)
# {'color': 'blue', 'tow_package': True, 'manufacturer_name': 'Subaru', 'model_name': 'Outback'}