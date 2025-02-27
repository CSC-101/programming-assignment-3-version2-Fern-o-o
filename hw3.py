from http.cookiejar import eff_request_host

import build_data
import county_demographics
import data
import hw3_tests

# Task 1

#The purpose of this function is to count the total population of all the counties in the data base
# input is  a list of the CountyDemographics class
#output/return is a float which is the total number of people
def population_total(demographic_list: list[data.CountyDemographics])->int:
    i=0
    for item in demographic_list:
        num = item.population.get('2014 Population',{})
        i += num
    return i




#Task 2

# The purpose of this function is  to grab all the items in the dictionary that have the str that the user is looking for
# The input is the Country demographic class which is a list
# the return type is a list of country demographics that fit the word
def filer_by_stat (demographic_list: list[data.CountyDemographics], word:str)-> list[data.CountyDemographics]:
    given_state_list = []
    for item in demographic_list:
        if item.state == word is not None:
            given_state_list.append(item)
    return given_state_list




#Task 3

# The purpose of this function if to find population that have a specific degree
# the inputs are the demographic list and the word that we word that we are looking for in terms of education
# the return is a float which is the population
def population_by_education (demographic_list: list[data.CountyDemographics], education:str)->float:
    population_with_edu = 0.0
    deg = education
    for item in demographic_list:
        if education in item.education:
            high_degree_perc = item.education.get(deg,{}) / 100
            county_pop = item.population.get('2014 Population',{})
            population_with_edu += high_degree_perc * county_pop
    return population_with_edu


#The purpose of this function is to find population of a specific ethnicity
# the inputs are the demographic list and the ethnicity that we want to find the number for
# the return is the total population of that ethnicity
def population_by_ethnicity (demographic_list: list[data.CountyDemographics], ethnicity: str)->float:
    total_ethnic_pop = 0.0
    ethnic = ethnicity
    for item in demographic_list:
        if ethnicity in item.ethnicities:
            eth = item.ethnicities.get(ethnic,{}) / 100
            county_pop = item.population.get('2014 Population',{})
            total_ethnic_pop += eth *county_pop
    return total_ethnic_pop


#The purpose of this function is to find the population that is below the poverty level of thr full data
# the input is the data County Demographic
# the return is a number indicating the amount of people throughtout the county data that are below the poverty level
def population_below_poverty_level (demographic_list: list[data.CountyDemographics])->float:
    county_list_of_below_poverty = []
    for item in demographic_list:
        county_pop = item.population.get('2014 Population',{})
        perc_below_poverty = item.income.get('Persons Below Poverty Level',{}) / 100
        county_list_of_below_poverty.append(county_pop * perc_below_poverty)
    return sum(county_list_of_below_poverty)




#Task 4



# The purpose of this function to find the percentage of people out of the whole data set that fit a certian criteria
# the inputs are the data set and the other one is string which is the title you are looking for
# the output / return should be percentage
def percent_by_education (demographic: list[data.CountyDemographics], word: str)-> float:
        population_for_edu = population_by_education(demographic,word)
        total_population = population_total(demographic)
        percentage = population_for_edu / total_population
        return percentage * 100



# The purpose of this function is to find the percentage of an enthnicity in a data set
# the input is the data set and the ethnicity that you want to llok at
# the out put is a percentage
def percent_by_ethnicity (demographic: list[data.CountyDemographics], word: str)->float:
    population_for_ethnicity = population_by_ethnicity(demographic, word)
    total_population = population_total(demographic)
    percentage = population_for_ethnicity / total_population
    return percentage * 100



# The purpose of this function is to find the poverty percentage across the whole data set
# the input is the data set
# the return is the percentage
def percent_by_poverty (demographic: list[data.CountyDemographics])->float:
    population_for_poverty = population_below_poverty_level(demographic)
    total_population = population_total(demographic)
    percentage = population_for_poverty / total_population
    return percentage *100


#Task 5

#Purpose is to find if a counties certain education is higher than the given number
# the input is the data set , the type of education you are looking at, and number that you want to compare to
# The return is a list of counties that have a greater education
def education_greater_than (demographic: list[data.CountyDemographics], education:str , num:float)->list[data.CountyDemographics]:
    edu_list = []
    for item in demographic:
        if education in item.education:
            if item.education.get(education) > num:
                edu_list.append(item)
    return edu_list




#Purpose is to find if a counties certain education is less than the given number
# the input is the data set , the type of education you are looking at, and number that you want to compare to
# The return is a list of counties that have a less education
def education_less_than (demographic: list[data.CountyDemographics], education:str , num:float)->list[data.CountyDemographics]:
    edu_list = []
    for item in demographic:
        if education in item.education:
            if item.education.get(education) < num:
                edu_list.append(item)
    return edu_list



# The purpose of this function is to find the certain counties with a higher percentage of a specific ethnic group
# the input is the data set, the ethnic group that you are looking at and the percentage that you want to find is greater than
# output the list of counties that have a greater percentage of the number that you entered.
def ethnicity_greater_than (demographic:list[data.CountyDemographics], ethnicity:str , num:float)->list[data.CountyDemographics]:
    ethnicity_list = []
    for item in demographic:
        if ethnicity in item.ethnicities:
            if item.ethnicities.get(ethnicity) > num:
                ethnicity_list.append(item)
    return ethnicity_list



# The purpose of this function is to find the certain counties with a lower percentage of a specific ethnic group
# the input is the data set, the ethnic group that you are looking at and the percentage that you want to find is less than
# output the list of counties that have a less percentage of the number that you entered.
def ethnicity_less_than (demographic:list[data.CountyDemographics], ethnicity:str , num:float)->list[data.CountyDemographics]:
    ethnicity_list = []
    for item in demographic:
        if ethnicity in item.ethnicities:
            if item.ethnicities.get(ethnicity) < num:
                ethnicity_list.append(item)
    return ethnicity_list

#The purpose of this function is to find the counties that have a greater percentage than he number your input
# the inputs are the data set and the number that you want to compare all th counties to
# the output is a list of counties that the percentage of poverty is greater than the number your input

def def_poverty_level_greater_than (demographic:list[data.CountyDemographics], num:float)->list[data.CountyDemographics]:
    poverty_greater = []
    for item in demographic:
        if item.income.get('Persons Below Poverty Level',{}) > num:
            poverty_greater.append(item)
    return poverty_greater




#The purpose of this function is to find the counties that have a lower percentage than he number your input
# the inputs are the data set and the number that you want to compare all th counties to
# the output is a list of counties that the percentage of poverty is lower than the number your input.
def def_poverty_level_less_than (demographic:list[data.CountyDemographics], num:float)->list[data.CountyDemographics]:
    poverty_less = []
    for item in demographic:
        if item.income.get('Persons Below Poverty Level',{}) < num:
            poverty_less.append(item)
    return poverty_less










