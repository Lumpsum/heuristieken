grid_grid = [[0 for i in range(9)] for j  in range(9)]
grid_car_list = ['placeholder']
grid = Grid(grid_grid, grid_car_list)
grid.add_car(Car('hor', 2, 0, 4)) # red car
grid.add_car(Car('vert', 2, 0, 1))
grid.add_car(Car('vert', 3, 0, 6))
grid.add_car(Car('vert', 2, 1, 5))
grid.add_car(Car('vert', 2, 2, 3))
grid.add_car(Car('vert', 3, 3, 3))
grid.add_car(Car('vert', 2, 4, 0))
grid.add_car(Car('vert', 2, 4, 2))
grid.add_car(Car('vert', 3, 4, 6))
grid.add_car(Car('vert', 2, 5, 2))
grid.add_car(Car('vert', 2, 7, 0))
grid.add_car(Car('vert', 3, 8, 5))
grid.add_car(Car('hor', 2, 0, 0))
grid.add_car(Car('hor', 2, 2, 0))
grid.add_car(Car('hor', 3, 1, 1))
grid.add_car(Car('hor', 2, 5, 1))
grid.add_car(Car('hor', 2, 2, 2))
grid.add_car(Car('hor', 2, 7, 2))
grid.add_car(Car('hor', 3, 6, 3))
grid.add_car(Car('hor', 2, 4, 5))
grid.add_car(Car('hor', 2, 6, 5))
grid.add_car(Car('hor', 2, 2, 6))
grid.add_car(Car('hor', 3, 5, 6))
grid.add_car(Car('hor', 2, 2, 7))
grid.add_car(Car('hor', 2, 5, 7))
grid.add_car(Car('hor', 3, 1, 8))