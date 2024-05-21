from sql_retriever import *
from setup_classes import *
from config import *


class Pipeline:
    def __init__(self, model_name, classifier_parameters, checker_parameter, solver_parameters):
        self.model_name = model_name
        self.classifier_parameters = classifier_parameters
        self.checker_parameters = checker_parameter
        self.solver_parameters = solver_parameters
        self.model = LLM(self.model_name)

    def __equation_classifier(self, methods, equation):
        self.model.set_parameters(self.classifier_parameters)
        for i, method in enumerate(methods):
            prompt = SetupClassifierPrompt.setup_prompt(
                classifier_prompt=self.classifier_parameters['classifier_prompt'], instructions=method,
                equation=equation)
            output = self.model.complete(prompt)
            if output == "T":
                return method[0]
        print(f"Sorry but we don`t know how to solve this equation...")

    def __solution_checker(self, unchecked_solution):
        self.model.set_parameters(self.checker_parameters)
        output = self.model.complete(unchecked_solution)
        return output

    def solve_equation(self, equation, check=False):
        methods = sql_retrieval(HOST, USER, PASSWORD, DB_NAME, TABLE_NAME)
        print(methods)
        instructions = self.__equation_classifier(methods, equation)
        if instructions is not None:
            prompt_solver = SetupSolverPrompt.setup_prompt(solver_prompt=self.solver_parameters['solver_prompt'], instructions=instructions, equation=equation)
            self.model.set_parameters(self.solver_parameters)
            solution = self.model.complete(prompt_solver)
            if check:
                prompt_checker = SetupSolveCheckerPrompt.setup_prompt(solve_checker_prompt=self.checker_parameters['checker_prompt'],
                                                                      instructions=instructions, equation=equation,
                                                                      unchecked_solution=solution)
                solution = self.__solution_checker(prompt_checker)
                return solution
            return solution
        return "Sorry but we don`t know how to solve this equation..."


