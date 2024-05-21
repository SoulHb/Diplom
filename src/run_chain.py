from database import create_database
from pipeline import *
import os
import openai
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    create_database(HOST, USER, PASSWORD, DB_NAME, TABLE_NAME, DATA_PATH)
    model_name = 'gpt-4'
    classifier_parameters = {'temperature': 0.01, 'max_tokens': 1, 'top_k': 2, 'top_p': 0.95, 'classifier_prompt': GPT_CLASSIFICATION}
    checker_parameter = {'temperature': 0.01, 'max_tokens': None, 'top_k': 2, 'top_p': 0.95, 'checker_prompt': GPT_SOLVE_CHECKER}
    solver_parameters = {'temperature': 0.01, 'max_tokens': None, 'top_k': 2, 'top_p': 0.95, 'solver_prompt': GPT_MATH_SOLVE}
    pipeline = Pipeline(model_name=model_name, classifier_parameters=classifier_parameters, checker_parameter=checker_parameter, solver_parameters=solver_parameters)
    equation = 'y`+y*cosx = sinx * cosx'#'dy/dx= (1+y**2)/(1+x**2)'#'-2xydx + (1+x**2)*dy = 0'#'dy/dx= (1+y**2)/(1+x**2)'#'y`+y*cosx = sinx * cosx'#'(1+x**2)*dy - 2xydx = 0'#'y`+y*cosx = sinx * cosx'#'xy`- y + x*e^(y/x) = 0'#'y` + y*cosx = sinx*cosx'#'dy/dx= (1+y**2)/(1+x**2)' #'(1+x**2)*dy - 2xydx = 0'#'dy/dx= (1+y**2)/(1+x**2)' #'(1+x**2)*dy - 2xydx = 0'#input("Enter differential equation:")
    solution = pipeline.solve_equation(equation, check=False)
    print(solution)


main()
