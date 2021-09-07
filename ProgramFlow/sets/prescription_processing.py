"""
Pop does not care what it is removing in case of set
Since set is an unordered collection
"""
from prescription_data import patients

trial_patients = {'Denise', 'Eddie', 'Frank', 'Georgia', 'Kenny'}

while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=':')
    prescription = patients[patient]
    print(prescription)
