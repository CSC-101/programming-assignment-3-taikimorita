import data
import build_data
import unittest
from hw3 import *
from typing import List

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total(self):
        expected_population = sum(county.population['2014 Population'] for county in reduced_data)
        result = population_total(reduced_data)
        self.assertEqual(result, expected_population)

    def test_population_total_empty(self):
        result = population_total([])
        self.assertEqual(result, 0)

    # Part 2
    # test filter_by_state
    def test_filter_by_state(self):
        state = 'CA'
        filtered_counties = filter_by_state(reduced_data, state)
        self.assertTrue(all(county.state == state for county in filtered_counties))
        self.assertEqual(len(filtered_counties), 2)

    def test_filter_by_state_no_results(self):
        state = 'XY'
        filtered_counties = filter_by_state(reduced_data, state)
        self.assertEqual(filtered_counties, [])

    # Part 3
    # test population_by_education
    # test population_by_ethnicity
    # test population_below_poverty_level
    def test_population_by_education(self):
        education_key = "Bachelor's Degree or Higher"
        expected_population = sum(
            county.population['2014 Population'] * (county.education.get(education_key, 0) / 100)
            for county in reduced_data
        )
        result = population_by_education(reduced_data, education_key)
        self.assertEqual(result, expected_population)

    def test_population_by_education_no_data(self):
        education_key = "PhD"
        result = population_by_education(reduced_data, education_key)
        self.assertEqual(result, 0)

    def test_population_by_ethnicity(self):
        ethnicity_key = "White Alone"
        expected_population = sum(
            county.population['2014 Population'] * (county.ethnicities.get(ethnicity_key, 0) / 100)
            for county in reduced_data
        )
        result = population_by_ethnicity(reduced_data, ethnicity_key)
        self.assertEqual(result, expected_population)

    def test_population_by_ethnicity_no_data(self):
        ethnicity_key = "Non-Existent Ethnicity"
        result = population_by_ethnicity(reduced_data, ethnicity_key)
        self.assertEqual(result, 0)

    def test_population_below_poverty_level(self):
        expected_population = sum(
            county.population['2014 Population'] * (county.income['Persons Below Poverty Level'] / 100)
            for county in reduced_data
        )
        result = population_below_poverty_level(reduced_data)
        self.assertEqual(result, expected_population)

    def test_population_below_poverty_level_no_data(self):
        result = population_below_poverty_level([])
        self.assertEqual(result, 0)

    # Part 4
    # test percent_by_education
    # test percent_by_ethnicity
    # test percent_below_poverty_level
    def test_percent_by_education(self):
        education_key = "Bachelor's Degree or Higher"
        total_population = population_total(reduced_data)
        education_population = population_by_education(reduced_data, education_key)
        expected_percent = (education_population / total_population) * 100 if total_population > 0 else 0
        result = percent_by_education(reduced_data, education_key)
        self.assertEqual(result, expected_percent)

    def test_percent_by_education_no_population(self):
        education_key = "Bachelor's Degree or Higher"
        result = percent_by_education([], education_key)
        self.assertEqual(result, 0)

    def test_percent_by_ethnicity(self):
        ethnicity_key = "White Alone"
        total_population = population_total(reduced_data)
        ethnicity_population = population_by_ethnicity(reduced_data, ethnicity_key)
        expected_percent = (ethnicity_population / total_population) * 100 if total_population > 0 else 0
        result = percent_by_ethnicity(reduced_data, ethnicity_key)
        self.assertEqual(result, expected_percent)

    def test_percent_by_ethnicity_no_population(self):
        ethnicity_key = "Black Alone"
        result = percent_by_ethnicity([], ethnicity_key)
        self.assertEqual(result, 0)

    def test_percent_below_poverty_level(self):
        total_population = population_total(reduced_data)
        poverty_population = population_below_poverty_level(reduced_data)
        expected_percent = (poverty_population / total_population) * 100 if total_population > 0 else 0
        result = percent_below_poverty_level(reduced_data)
        self.assertEqual(result, expected_percent)

    def test_percent_below_poverty_level_no_data(self):
        result = percent_below_poverty_level([])
        self.assertEqual(result, 0)

    # Part 5
    # test education_greater_than
    # test education_less_than
    # test ethnicity_greater_than
    # test ethnicity_less_than
    # test below_poverty_level_greater_than
    # test below_poverty_level_less_than
    def test_education_greater_than(self):
        education_key = "Bachelor's Degree or Higher"
        threshold = 20.0
        filtered_counties = education_greater_than(reduced_data, education_key, threshold)
        self.assertTrue(all(county.education.get(education_key, 0) > threshold for county in filtered_counties))

    def test_education_greater_than_no_results(self):
        education_key = "Bachelor's Degree or Higher"
        threshold = 100.0
        filtered_counties = education_greater_than(reduced_data, education_key, threshold)
        self.assertEqual(filtered_counties, [])

    def test_education_less_than(self):
        education_key = "Bachelor's Degree or Higher"
        threshold = 20.0
        filtered_counties = education_less_than(reduced_data, education_key, threshold)
        self.assertTrue(all(county.education.get(education_key, 0) < threshold for county in filtered_counties))

    def test_ethnicity_less_than_no_results(self):
        ethnicity_key = "White Alone"
        threshold = 0.0
        filtered_counties = ethnicity_less_than(reduced_data, ethnicity_key, threshold)
        self.assertEqual(filtered_counties, [])

    def test_ethnicity_greater_than(self):
        ethnicity_key = "White Alone"
        threshold = 75.0
        filtered_counties = ethnicity_greater_than(reduced_data, ethnicity_key, threshold)
        self.assertTrue(all(county.ethnicities.get(ethnicity_key, 0) > threshold for county in filtered_counties))

    def test_below_poverty_level_greater_than_no_results(self):
        threshold = 100.0
        filtered_counties = below_poverty_level_greater_than(reduced_data, threshold)
        self.assertEqual(filtered_counties, [])

    def test_ethnicity_less_than(self):
        ethnicity_key = "White Alone"
        threshold = 75.0
        filtered_counties = ethnicity_less_than(reduced_data, ethnicity_key, threshold)
        self.assertTrue(all(county.ethnicities.get(ethnicity_key, 0) < threshold for county in filtered_counties))

    def test_ethnicity_less_than_no_results(self):
        ethnicity_key = "White Alone"
        threshold = 0.0
        filtered_counties = ethnicity_less_than(reduced_data, ethnicity_key, threshold)
        self.assertEqual(filtered_counties, [])

    def test_below_poverty_level_greater_than(self):
        threshold = 20.0
        filtered_counties = below_poverty_level_greater_than(reduced_data, threshold)
        self.assertTrue(all(county.income.get('Persons Below Poverty Level', 0) > threshold for county in filtered_counties))

    def test_below_poverty_level_greater_than_no_results(self):
        threshold = 100.0
        filtered_counties = below_poverty_level_greater_than(reduced_data, threshold)
        self.assertEqual(filtered_counties, [])

    def test_below_poverty_level_less_than(self):
        threshold = 20.0
        filtered_counties = below_poverty_level_less_than(reduced_data, threshold)
        self.assertTrue(all(county.income.get('Persons Below Poverty Level', 0) < threshold for county in filtered_counties))

    def test_below_poverty_level_less_than_no_results(self):
        threshold = 0.0

if __name__ == '__main__':
    unittest.main()
