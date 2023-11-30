from project.waze_api.route_calculator import RouteCalculator, RouteError

from_address = 'Cluj Napoca, Romania'
to_address = 'Brno, czech republic'
route = RouteCalculator(from_address, to_address)
try:
    route.calc_route_info()
except RouteError as err:
    print(err)
