from typing import List
from abc import ABC, abstractmethod
from openai import OpenAI


class SetupChatPrompt(ABC):
    @staticmethod
    @abstractmethod
    def setup_prompt(*args):
        pass


class SetupSolverPrompt(SetupChatPrompt):
    @staticmethod
    def setup_prompt(solver_prompt, instructions, equation):
        system_prompt = solver_prompt.format(instructions=instructions, equation=equation)
        user_request = f"""Differential equation: '{equation}'\nSolution:"""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_request}
        ]
        return messages


class SetupClassifierPrompt(SetupChatPrompt):
    @staticmethod
    def setup_prompt(classifier_prompt, instructions, equation):
        system_prompt = classifier_prompt.format(text=instructions, equation=equation)
        user_request = f"""User differential equation: {equation}\nOutput:"""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_request}
        ]
        return messages


class SetupSolveCheckerPrompt(SetupChatPrompt):
    @staticmethod
    def setup_prompt(solve_checker_prompt, instructions, equation, unchecked_solution):
        system_prompt = solve_checker_prompt.format(instructions=instructions)

        user_request = f"""Methods: <{instructions}>
                        User`s differential equation: {equation}
                        Unchecked solution: {unchecked_solution}
                        Correct solution:"""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_request}
        ]
        return messages


class LLM:
    def __init__(self, model_name):
        self.model_name = model_name
        if self.model_name in ['codellama-34b-instruct', 'llama3-70b', 'mistral-7b-instruct', 'mixtral-8x22b-instruct']:
            self.model = OpenAI(api_key='LL-Xs8ZH57YRePfs53xDSpWRifUpA4DgZUMmWZhBGb3AkAXpbng0PLfJSPQEzhGSRGD', base_url="https://api.llama-api.com")
        elif self.model_name in ['gpt-4', 'gpt-3.5-turbo', 'gpt-4o']:
            self.model = OpenAI()

    def set_parameters(self, parameters):
        self.temperature = parameters['temperature']
        self.max_tokens = parameters['max_tokens']
        self.top_k = parameters['top_k']
        self.top_p = parameters['top_p']

    def complete(
            self,
            messages: List[dict],
    ) -> str:
        response = self.model.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return response.choices[0].message.content