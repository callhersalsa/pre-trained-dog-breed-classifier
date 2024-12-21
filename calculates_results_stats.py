# PROGRAMMER: Salsabila Syahirah
# DATE CREATED:  27 November, 2024                                
# REVISED DATE: 

def calculates_results_stats(results_dic):
         
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    results_stats_dic = {}

    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    for key in results_dic:
        # number of dog images
        if results_dic[key][3] == 1:
                results_stats_dic['n_dogs_img'] += 1
        
        # number of not dog images
        else:
                results_stats_dic['n_notdogs_img'] +=1

        # number of correct dog matches
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        # number of correct non dog matches
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
        
        # number of correct breed matches
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
        
        # number of label matches
        if results_dic[key][2] == 1:
                results_stats_dic['n_match'] += 1

    # objective 1a
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs']/results_stats_dic['n_dogs_img']) * 100

    # objective 1b
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = results_stats_dic['n_correct_notdogs']/results_stats_dic['n_notdogs_img'] * 100

    # obejctive 2
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = results_stats_dic['n_correct_breed']/results_stats_dic['n_dogs_img'] * 100

    # objective 3
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = results_stats_dic['n_match']/results_stats_dic['n_images'] * 100

    return results_stats_dic


