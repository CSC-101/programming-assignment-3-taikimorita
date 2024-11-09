import data
from data import CountyDemographics
import unittest
from hw3 import *
from typing import List

# Part 1
def population_total(counties: list[CountyDemographics]) -> int:
    """
    Computes the total 2014 population across the provided list of counties.
    :param counties: A list of CountyDemographics objects.
    :return: Total 2014 population as an integer.
    """
    total_population = 0
    for county in counties:
        total_population += county.population['2014 Population']
    return total_population

# Part 2
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    """
    Filters counties by state abbreviation.
    :param counties: A list of CountyDemographics objects.
    :param state: The two-letter state abbreviation.
    :return: A list of counties from the specified state.
    """
    return [county for county in counties if county.state == state]

# Part 3
def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    """
    Computes the total population for a given education level across the counties.
    :param counties: A list of CountyDemographics objects.
    :param education_key: The education key (e.g., "Bachelor's Degree or Higher").
    :return: The total population for the given education level.
    """
    total_population = 0
    for county in counties:
        if education_key in county.education:
            percentage = county.education[education_key]
            total_population += (county.population['2014 Population'] * (percentage / 100))
    return total_population

def population_by_ethnicity(counties: List[data.CountyDemographics], ethnicity_key: str) -> float:
    """
    Computes the total population for a given ethnicity across the counties.
    :param counties: A list of CountyDemographics objects.
    :param ethnicity_key: The ethnicity key (e.g., 'Two or More Races').
    :return: The total population for the given ethnicity.
    """
    total_population = 0
    ethnicity_found = False
    print(f"Ethnicity key: {ethnicity_key}")
    for county in counties:
        print(f"County: {county.county}, Ethnicities: {county.ethnicities}")
        if ethnicity_key in county.ethnicities:
            ethnicity_percentage = county.ethnicities[ethnicity_key]
            population = county.population['2014 Population']
            calculated_population = population * (ethnicity_percentage / 100)
            total_population += calculated_population
            print(
                f"Found {ethnicity_key}: {ethnicity_percentage}% of population {population} => {calculated_population}")
            ethnicity_found = True
    print(f"Total Population for {ethnicity_key}: {total_population}")
    if ethnicity_found:
        return total_population
    else:
        return 0

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    """
    Computes the total population below the poverty level across the counties.
    :param counties: A list of CountyDemographics objects.
    :return: The total population below the poverty level.
    """
    total_population = 0
    for county in counties:
        poverty_level = county.income['Persons Below Poverty Level']
        total_population += (county.population['2014 Population'] * (poverty_level / 100))
    return total_population

# Part 4
def percent_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    """
    Computes the percentage of the population with a specific education level.
    :param counties: A list of CountyDemographics objects.
    :param education_key: The education key (e.g., "Bachelor's Degree or Higher").
    :return: The percentage of population for the given education level.
    """
    total_population = population_total(counties)
    education_population = population_by_education(counties, education_key)
    return (education_population / total_population) * 100 if total_population > 0 else 0

def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    """
    Computes the percentage of the population of a specific ethnicity.
    :param counties: A list of CountyDemographics objects.
    :param ethnicity_key: The ethnicity key (e.g., 'Two or More Races').
    :return: The percentage of population for the given ethnicity.
    """
    total_population = population_total(counties)
    ethnicity_population = population_by_ethnicity(counties, ethnicity_key)
    return (ethnicity_population / total_population) * 100 if total_population > 0 else 0

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    """
    Computes the percentage of the population below the poverty level.
    :param counties: A list of CountyDemographics objects.
    :return: The percentage of population below the poverty level.
    """
    total_population = population_total(counties)
    poverty_population = population_below_poverty_level(counties)
    return (poverty_population / total_population) * 100 if total_population > 0 else 0

# Part 5
def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    """
    Filters counties where the percentage of people with the specified education level is greater than the threshold.
    :param counties: A list of CountyDemographics objects.
    :param education_key: The education key (e.g., "Bachelor's Degree or Higher").
    :param threshold: The percentage threshold.
    :return: A list of counties where the specified education level is greater than the threshold.
    """
    return [county for county in counties if county.education.get(education_key, 0) > threshold]


def education_less_than(county_list: List[CountyDemographics], education_key: str, threshold: float) -> List[
    CountyDemographics]:
    """
    Returns a list of counties where the specified education percentage is less than the given threshold.

    :param county_list: List of CountyDemographics objects
    :param education_key: The education key to look up (e.g., "Bachelor's Degree or Higher")
    :param threshold: The threshold percentage to compare against
    :return: List of CountyDemographics objects with education percentage less than threshold
    """
    result = []
    for county in county_list:
        if education_key in county.education:
            if county.education[education_key] < threshold:
                result.append(county)
    return result

def ethnicity_greater_than(county_list: List[CountyDemographics], ethnicity_key: str, threshold: float) -> List[
    CountyDemographics]:
    """
    Returns a list of counties where the specified ethnicity percentage is greater than the given threshold.

    :param county_list: List of CountyDemographics objects
    :param ethnicity_key: The ethnicity key to look up (e.g., "Hispanic or Latino")
    :param threshold: The threshold percentage to compare against
    :return: List of CountyDemographics objects with ethnicity percentage greater than threshold
    """
    result = []
    for county in county_list:
        if ethnicity_key in county.ethnicities:
            if county.ethnicities[ethnicity_key] > threshold:
                result.append(county)
    return result

def ethnicity_less_than(county_list: List[CountyDemographics], ethnicity_key: str, threshold: float) -> List[
    CountyDemographics]:
    """
    Returns a list of counties where the specified ethnicity percentage is less than the given threshold.

    :param county_list: List of CountyDemographics objects
    :param ethnicity_key: The ethnicity key to look up (e.g., "Hispanic or Latino")
    :param threshold: The threshold percentage to compare against
    :return: List of CountyDemographics objects with ethnicity percentage less than threshold
    """
    result = []
    for county in county_list:
        if ethnicity_key in county.ethnicities:
            if county.ethnicities[ethnicity_key] < threshold:
                result.append(county)
    return result

def below_poverty_level_greater_than(county_list: List[CountyDemographics], threshold: float) -> List[
    CountyDemographics]:
    """
    Returns a list of counties where the percentage of the population below the poverty level is greater than the threshold.

    :param county_list: List of CountyDemographics objects
    :param threshold: The threshold percentage to compare against
    :return: List of CountyDemographics objects with poverty level percentage greater than threshold
    """
    result = []
    for county in county_list:
        if 'Persons Below Poverty Level' in county.income:
            if county.income['Persons Below Poverty Level'] > threshold:
                result.append(county)
    return result

def below_poverty_level_less_than(county_list: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    """
    Returns a list of counties where the percentage of the population below the poverty level is less than the threshold.

    :param county_list: List of CountyDemographics objects
    :param threshold: The threshold percentage to compare against
    :return: List of CountyDemographics objects with poverty level percentage less than threshold
    """
    result = []
    for county in county_list:
        if 'Persons Below Poverty Level' in county.income:
            if county.income['Persons Below Poverty Level'] < threshold:
                result.append(county)
    return result
