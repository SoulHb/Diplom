import re
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from config import *


def get_eq_type(file_path):
    # Extracting just the desired part from the file path using regular expressions
    match = re.search(r'/([^/]+)\.pdf$', file_path)

    if match:
        filename = match.group(1)
        parts = filename.split('_')

        # Joining all parts that are not 'pdf' extension
        desired_part = ' '.join([part for part in parts if part != 'pdf'])

        return desired_part.lower()
    else:
        print("No match found.")


def init_formatter_model():
    llm = ChatOpenAI(model_name=GPT_FORMATER_MODEL, temperature=GPT_FORMATER_TEMPERATURE)
    return llm


def text_formatter(text):
    llm = init_formatter_model()
    prompt = PromptTemplate(
        template=GPT_FORMATER,
        input_variables=["text"], )
    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run(text=text)
    return output


def read_pdf(data_path):
    print(data_path)
    loader = PyPDFLoader(data_path)
    text = ''
    pages = loader.load()
    # Extract text
    for i in range(len(pages)):
        text += f"{pages[i].page_content}\n"
    output = text_formatter(text)
    return output
