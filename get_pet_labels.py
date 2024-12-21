# PROGRAMMER: Salsabila Syahirah
# DATE CREATED:   24 November, 2024                               
# REVISED DATE: 

# Imports python modules
from os import listdir

def get_pet_labels(image_dir):

    in_files = listdir(image_dir)
 
    results_dic = dict()
   
    for idx in range(0, len(in_files), 1):
       
       if in_files[idx][0] != ".":
           
            pet_label = ""
            
            filename = in_files[idx].lower()
            word_list_per_image = filename.split("_")
            
            for word in word_list_per_image:
               if word.isalpha():
                  pet_label += word + " "
            
            pet_label = pet_label.rstrip()
               
            if in_files[idx] not in results_dic:
               results_dic[in_files[idx]] = [pet_label]
              
            else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    return results_dic

