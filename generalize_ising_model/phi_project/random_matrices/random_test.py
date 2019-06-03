from generalize_ising_model.phi_project.random_matrices.phi_sim_save import phiSimSave
from generalize_ising_model.ising_utils import makedir

output_directory = '/home/user/Desktop/phiTest/randomTest'

size_list = [3, 4, 5, 6, 7, 8, 9]
number_entities = 20

for size in size_list:
    sub_output_path = output_directory + '/' + str(size)
    makedir(sub_output_path)

    for entity in range(number_entities):
        phiSimSave(size, sub_output_path, entity)
