# PROGRAMMER: Salsabila Syahirah
# DATE CREATED:   24 November, 2024                                
# REVISED DATE: 

import argparse
def get_input_args():

    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type = str, default = 'pet_images/',
                        help = 'Input the path to the folder of pet images')
    parser.add_argument('--arch', type = str, default = 'vgg',
                        help = 'Input CNN type (vgg, resnet, alexnet)')
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt',
                        help = 'Input dog file names in dognames.txt.')

    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 
    return parser.parse_args()
