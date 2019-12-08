import pandas as pd

class_data = pd.read_csv('coursework.csv')
class_data.set_index('Course', inplace=True)
print('EECS 485' in class_data.index)
