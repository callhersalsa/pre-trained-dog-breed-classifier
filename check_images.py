# PROGRAMMER: Salsabila Syahirah
# DATE CREATED: 26 November, 2024                                 
# REVISED DATE: 


# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # TODO 0: Measures total program runtime by collecting start time
    start_time = time()

    # TODO 1: Define get_input_args function within the file get_input_args.py
    # This function retrieves 3 Command Line Arguments from user as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these command line arguments from the function call as
    # the variable in_arg
    in_arg = get_input_args()
    print("1: Image directory   : ", in_arg.dir)
    print("2: Model architecture: ", in_arg.arch)
    print("3: Image file        : ", in_arg.dogfile)

    # Function that checks command line arguments using in_arg  
    check_command_line_arguments(in_arg)
    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results    
    check_creating_pet_image_labels(results)

    # Creates Classifier Labels with classifier function, Compares Labels, 
    # and adds these results to the results dictionary - results
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results    
    check_classifying_images(results)    

    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)

    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)
    print_results(results, results_stats, in_arg.arch, True, True)
    
    end_time = time()
    
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
