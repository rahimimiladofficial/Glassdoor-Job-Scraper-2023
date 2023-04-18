import glassdor_scraper as gs
import pandas as pd
path = "D:/dev/ds_salary_project/chromedriver.exe"

df = gs.get_jobs("data scientist", 5, True, path, 5)

print(df)

