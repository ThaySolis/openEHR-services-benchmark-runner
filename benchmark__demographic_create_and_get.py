import os
import random

import rm_mock_generation
import demographic_api
import benchmark_utils
from time_measurement import Timed

timed = Timed(1100)
WARMUP = 5
REPEAT = 1000

@timed.measure("create_patient")
def create_patient(patient_data):
    return demographic_api.create_patient(patient_data)

@timed.measure("get_patient")
def get_patient(patient_id):
    return demographic_api.get_patient(patient_id)

def main():
    timed.clear_all()
    demographic_api.clear_statistics()
    
    random.seed(1)
    for i in range(0, WARMUP + REPEAT):
        mock_patient_data = rm_mock_generation.generate_mock_patient()
        mock_patient_id = create_patient(mock_patient_data)
        get_patient(mock_patient_id)

    api_statistics = demographic_api.get_statistics()

    create_patient_samples_local = timed.get_group("create_patient").get_samples()[-REPEAT:]
    create_patient_samples_remote = api_statistics["usage_statistics"]["create_patient"]["samples"][-REPEAT:]
    get_patient_samples_local = timed.get_group("get_patient").get_samples()[-REPEAT:]
    get_patient_samples_remote = api_statistics["usage_statistics"]["get_patient"]["samples"][-REPEAT:]

    dir_name = benchmark_utils.time_formatted() + "--DEMOGRAPHIC--CREATE_AND_GET"
    os.mkdir(dir_name)

    with open(dir_name + "/create_patient_local.txt", mode="w", encoding="utf-8") as f:
        benchmark_utils.save_stats(create_patient_samples_local, f)
    with open(dir_name + "/create_patient_remote.txt", mode="w", encoding="utf-8") as f:
        benchmark_utils.save_stats(create_patient_samples_remote, f)
    with open(dir_name + "/get_patient_local.txt", mode="w", encoding="utf-8") as f:
        benchmark_utils.save_stats(get_patient_samples_local, f)
    with open(dir_name + "/get_patient_remote.txt", mode="w", encoding="utf-8") as f:
        benchmark_utils.save_stats(get_patient_samples_remote, f)

main()