from ai_agent.yandex_gpt import generate_comp_profile, generate_theme_blocks
import pandas as pd
from utils.parser import read_pdf

pdf = read_pdf("../files/new_document.pdf")
path = "../files/test.csv"
data = pd.read_csv(path)


result = generate_theme_blocks(pdf)
print(result)