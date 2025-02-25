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

#Task 3
def population_by_education (demographic_list: list[data.CountyDemographics], education:str)->float:
    population_with_edu = 0.0
    deg = education
    for item in demographic_list:
        if education in item.education:
            high_degree_perc = item.education.get(deg,{}) / 100
            county_pop = item.population.get('2014 Population',{})
            population_with_edu += high_degree_perc * county_pop
    return population_with_edu

def population_by_ethnicity (demographic_list: list[data.CountyDemographics], ethnicity: str)->float:
    total_ethnic_pop = 0.0
    ethnic = ethnicity
    for item in demographic_list:
        if ethnicity in item.ethnicities:
            eth = item.ethnicities.get(ethnic,{}) / 100
            county_pop = item.population.get('2014 Population',{})
            total_ethnic_pop += eth *county_pop
    return total_ethnic_pop

def population_below_poverty_level (demographic_list: list[data.CountyDemographics])->float:
    county_list_of_below_poverty = []
    for item in demographic_list:
        county_pop = item.population.get('2014 Population',{})
        perc_below_poverty = item.income.get('Persons Below Poverty Level',{})
        county_list_of_below_poverty.append(county_pop * perc_below_poverty)
    return sum(county_list_of_below_poverty)

#Task 4
def percent_by_education (demographic: list[data.CountyDemographics], word: str)-> float:
        population_for_edu = population_by_education(demographic,word)
        total_population = population_total(demographic)
        percentage = population_for_edu / total_population
        return percentage * 100


def percent_by_ethnicity (demographic: list[data.CountyDemographics], word: str)->float:
    population_for_ethnicity = population_by_ethnicity(demographic, word)
    total_population = population_total(demographic)
    percentage = population_for_ethnicity / total_population
    return percentage * 100


def percent_by_poverty (demographic: list[data.CountyDemographics])->float:
    population_for_poverty = population_below_poverty_level(demographic)
    total_population = population_total(demographic)
    percentage = population_for_poverty / total_population
    return percentage


#Task 5
def education_greater_than (demographic: list[data.CountyDemographics], education:str , num:float)->list[data.CountyDemographics]:
    edu_list = []
    for item in demographic:
        if education in item.education:
            if item.education.get(education) >= num:
                edu_list.append(item)
    return edu_list



def education_less_than (demographic: list[data.CountyDemographics], education:str , num:float)->list[data.CountyDemographics]:
    edu_list = []
    for item in demographic:
        if education in item.education:
            if item.education.get(education) <= num:
                edu_list.append(item)
    return edu_list








