def best(pop, fit_value):
    px = len(pop)
    best_individual = []
    best_fit = fit_value[0]
    for i in range(1, px):
        if(fit_value[i] > best_fit):
            best_fit = fit_value[i]
            best_individual = pop[i]
        elif (fit_value[i] <= best_fit):
            best_fit = best_fit
            best_individual = pop[i]

    return [best_individual, best_fit]

if __name__ == '__main__':
    pass