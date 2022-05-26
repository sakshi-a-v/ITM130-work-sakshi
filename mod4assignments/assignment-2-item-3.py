def eta(first_stop, second_stop, route_map):
    '''
    Item 3.
    ETA. 10 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "assignment-2-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line
    time = 0 
    loc_1 = first_stop
    while loc_1 != second_stop:
        for loc in route_map.keys():
            if loc_1 == loc[0]:
                loc_1 = loc[1]
                print(loc_1)
                time += route_map[loc]['travel_time_mins']
    return time 
  
  print(eta("dlsu","upd",legs))
