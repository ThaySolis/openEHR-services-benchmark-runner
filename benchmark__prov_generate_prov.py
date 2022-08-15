import os
import random

import rm_mock_generation
import demographic_api
import prov_api
import benchmark_utils
from time_measurement import Timed

timed = Timed(1100)
WARMUP = 5
REPEAT = 1000

@timed.measure("get_provenance")
def get_prov_of_patient(patient_id):
    return prov_api.get_prov_of_patient(patient_id)

def main():
    mock_patients = []

    # cria os pacientes com 1 versão cada
    random.seed(1)
    for i in range(0, WARMUP + REPEAT):
        mock_patient_data = rm_mock_generation.generate_mock_patient()
        version_id = demographic_api.create_patient(mock_patient_data)
        mock_patients.append({
            "version_id": version_id,
            "amount": 1
        })

    dir_name = benchmark_utils.time_formatted() + "--PROV--GENERATE_PROV"
    os.mkdir(dir_name)

    for desired_versions in [ 1, 10, 100 ]:
        timed.clear_all()
        prov_api.clear_statistics()
        
        for i in range(0, WARMUP + REPEAT):
            mock_patient = mock_patients[i]

            # cria as versões faltantes do paciente.
            for i in range(0, desired_versions - mock_patient["amount"]):
                mock_patient_data = rm_mock_generation.generate_mock_patient()
                mock_patient["version_id"] = demographic_api.update_patient(mock_patient["version_id"], mock_patient_data)
            
            # extrai o ID e gera o PROV
            mock_patient_id = benchmark_utils.extract_versioned_object_id_from_version_id(mock_patient["version_id"])
            get_prov_of_patient(mock_patient_id)

        api_statistics = prov_api.get_statistics()

        get_provenance_samples_local = timed.get_group("get_provenance").get_samples()[-REPEAT:]
        get_provenance_samples_remote = api_statistics["usage_statistics"]["get_provenance"]["samples"][-REPEAT:]

        with open(dir_name + f"/get_provenance_with_{desired_versions}_versions_local.txt", mode="w", encoding="utf-8") as f:
            benchmark_utils.save_stats(get_provenance_samples_local, f)
        with open(dir_name + f"/get_provenance_with_{desired_versions}_versions_remote.txt", mode="w", encoding="utf-8") as f:
            benchmark_utils.save_stats(get_provenance_samples_remote, f)

main()