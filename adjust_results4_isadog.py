# PROGRAMMER: Salsabila Syahirah
# DATE CREATED:        27 November, 2024                         
# REVISED DATE: 

def adjust_results4_isadog(results_dic, dogfile):
         
    with open('dognames.txt', 'r') as file:
      dog_name_list = file.readlines()
      dog_name_list = [dog.strip() for dog in dog_name_list]
    
    for key in results_dic:
      is_petimage_dog = 1 if results_dic[key][0] in dog_name_list else 0
      is_classifier_dog = 1 if results_dic[key][1] in dog_name_list else 0
      
      results_dic[key].extend([is_petimage_dog, is_classifier_dog])


