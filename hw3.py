import build_data
import county_demographics
import data
import hw3_tests

# Task 1
def population_total(demographic_list: list[data.CountyDemographics])->int:
    i=0
    for item in demographic_list:
        num = item.population.get('2014 Population',{})
        i += num
    return i



