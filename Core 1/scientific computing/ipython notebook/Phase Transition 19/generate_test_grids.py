Nsweeps = 100
size = 32

for beta in [0.1, 0.8, 1.6]:
    g = Grid(size, beta)
    m = g.do_sweeps(0, Nsweeps)
    grid = g.cells
    mag = g.magnetisation(grid)
    e_plus = np.zeros((size, size))
    e_minus = np.zeros((size, size))
    for i in np.arange(size):
        for j in np.arange(size):
            e_plus[i,j], e_minus[i,j] = g.energy(i, j, beta, grid)
                 
    if not os.path.exists(filename):
        filename = 'test_data_beta_%0.1f_2.pickle'%beta       
        f = open(filename, 'wb')
        pickle.dump((grid, mag, e_plus, e_minus, beta), f)
        f.close()

    if not os.path.exists(filename):
        filename = 'test_data_beta_%0.1f_grid_only_2.pickle'%beta
        f = open(filename, 'wb')
        pickle.dump((grid, beta), f)
        f.close()