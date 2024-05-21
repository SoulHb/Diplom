import yaml
import sys
sys.path.append('src')
with open(r'/home/solution/PycharmProjects/DIPLOM_old/src/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
GPT_MATH_SOLVE = config["gpt_math_solve"]
GPT_CLASSIFICATION = config["gpt_classification"]
CLASSIFIER_GPT_MODEL = config["classifier_gpt_model"]
SOLVER_GPT_MODEL = config["solver_gpt_model"]
DATA_PATH = config["data_path"]
MAX_TOKEN_LIMIT = config["max_token_limit"]
CLASSIFIER_TEMPERATURE = config["classifier_temperature"]
SOLVER_TEMPERATURE = config["solver_temperature"]
GPT_FORMATER = config["gpt_formatter"]
GPT_FORMATER_TEMPERATURE = config["gpt_formatter_temperature"]
GPT_FORMATER_MODEL = config["gpt_formatter_model"]
GPT_SOLVE_CHECKER = config["gpt_solve_checker"]
GPT_SOLVE_CHECKER_TEMPERATURE = config["gpt_solve_checker_temperature"]
GPT_SOLVE_CHECKER_MODEL = config["gpt_solve_checker_model"]
HOST = config["host"]
DB_NAME = config["db_name"]
USER = config["user"]
PASSWORD = config["password"]
TABLE_NAME = config["table_name"]
