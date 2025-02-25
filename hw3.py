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
#Task 2
def filer_by_stat (demographic_list: list[data.CountyDemographics], word:str)-> list[data.CountyDemographics]:
    given_state_list = []
    for item in demographic_list:
        if item.state == word is not None:
            given_state_list.append(item)
    return given_state_list





