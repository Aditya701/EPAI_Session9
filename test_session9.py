import pytest
import random
import session9
import os
import inspect
import re
import math

from session9 import *
#readme content check

README_CONTENT_CHECK_FOR = ['namedtuple', 'profile', 'dictionary', 
'Faker', 'age', 'location', 'blood']





def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    #readme_words = [word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session10)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__

def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        if function[1].__name__ not in ['namedtuple', 'wraps']:
            assert function[1].__annotations__


def test_gen_profiles_tuples():
    profiles = generate_profiles_using_namedtuple(50)
    assert len(profiles) == 50, "Something wrong with the  generate_profiles_using_namedtuple function."
    

def test_gen_profiles_dict():
    profiles = generate_profiles_using_dictionary(50)
    assert len(profiles) == 50, "Something wrong with the generate_profiles_using_dictionary function."
  
