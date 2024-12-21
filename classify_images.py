# PROGRAMMER: Salsabila Syahirah
# DATE CREATED:    27 November, 2024                             
# REVISED DATE: 

from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    for key in results_dic:

      model_label = f"{images_dir}/{key}"
       
      classifier_output = classifier(model_label, model)
      classifier_label = classifier_output.strip().lower()

      truth = results_dic[key][0]

      if truth in classifier_label:
        results_dic[key].extend([classifier_label, 1])
      else:
        results_dic[key].extend([classifier_label, 0])