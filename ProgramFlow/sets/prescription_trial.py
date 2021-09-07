from prescription_data import *

trial_patients = ['Denise', 'Eddie', 'Frank', 'Georgia', 'Kenny']

# Remove Earfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"{patient} is not taking {warfarin}, please remove him from trial list")
    print(patient, prescription)
