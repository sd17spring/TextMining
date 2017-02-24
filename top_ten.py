import texttmining as tm
from texttmining import get_pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


# Alfred_list = tm.most_frequent(get_pickle('Alfred_Edward_Bland_text.pickle'))
# Anna_list = tm.most_frequent(get_pickle('Anna_Katharine_Green_text.pickle'))
# Arthur_list = tm.most_frequent(get_pickle('Arthur_Christopher_Benson_text.pickle'))
# Dickens_list = tm.most_frequent(get_pickle('dickens_texts.pickle'))
# Donald_list = tm.most_frequent(get_pickle('Donald_Maxwell_text.pickle'))
# Frances_list = tm.most_frequent(get_pickle('Frances_Lilian_Taylor_text.pickle'))
# Helen_list = tm.most_frequent(get_pickle('Helen_Huber_text.pickle'))
# James_list = tm.most_frequent(get_pickle('James_Elroy_Flecker_text.pickle'))
# Maria_list = tm.most_frequent(get_pickle('Maria_Stewart_text.pickle'))
# Mary_J_list = tm.most_frequent(get_pickle('Mary_Rowles_Jarvis_text.pickle'))
# Mary_W_list = tm.most_frequent(get_pickle('Mary_Wade_text.pickle'))
# Mildred_list = tm.most_frequent(get_pickle('Mildred_Wirt_text.pickle'))
# Mrs_list = tm.most_frequent(get_pickle('Mrs_Henry_Wood_text.pickle'))
# Myrtle_list = tm.most_frequent(get_pickle('Myrtle_Reed_text.pickle'))
Rebecca_list = tm.most_frequent(get_pickle('Rebecca_Agatha_Armour_text.pickle'))
# Richard_list = tm.most_frequent(get_pickle('Richard_Jefferies_text.pickle'))
# Titus_list = tm.most_frequent(get_pickle('Titus_Maccius_Plautus_text.pickle'))
Walter_list = tm.most_frequent(get_pickle('Walter_M_Miller_text.pickle'))
# Wilkie_list = tm.most_frequent(get_pickle('Wilkie_Collins_text.pickle'))


print(Walter_list)
print(analyzer.polarity_scores(str(get_pickle('Walter_M_Miller_text.pickle'))))
print(Rebecca_list)
print(analyzer.polarity_scores(str(get_pickle('Rebecca_Agatha_Armour_text.pickle'))))
