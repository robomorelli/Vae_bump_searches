
root_folder = 'root_data/'

splitted_numpy_bkg = 'splitted_numpy_bkg/'
splitted_numpy_bkg_pre = 'splitted_numpy_bkg/preselection/'
splitted_numpy_bkg_middle = 'splitted_numpy_bkg/middle/'

splitted_numpy_sig = 'splitted_numpy_sig/'
splitted_numpy_sig_pre = 'splitted_numpy_sig/preselection/'
splitted_numpy_sig_middle = 'splitted_numpy_sig/middle/'

numpy_bkg = 'numpy_data/background/'
numpy_bkg_pre = 'numpy_data/background/preselection/'
numpy_bkg_middle = 'numpy_data/background/middle/'

numpy_sig = 'numpy_data/signal/'
numpy_sig_pre = 'numpy_data/signal/preselection/'
numpy_sig_middle = 'numpy_data/signal/middle'

numpy_sig_syst_down = 'numpy_data/signal_sys/down/'
numpy_sig_syst_up = 'numpy_data/signal_sys/up/'

numpy_sig_syst_down_pre = 'numpy_data/signal_sys/down/preselection/'
numpy_sig_syst_up_pre = 'numpy_data/signal_sys/up/preselection/'

numpy_sig_syst_down_middle = 'numpy_data/signal_sys/down/middle/'
numpy_sig_syst_up_middle = 'numpy_data/signal_sys/up/middle/'

train_val_test = 'numpy_data/train_val_test/'
train_val_test_mod_dep = 'numpy_data/train_val_test/model_dependent/'
train_val_test_mod_dep_boot_30_30_40 = 'numpy_data/train_val_test/bootstrap/model_dependent/bck_sig_30_30_40_bootstrap/'

model_results_single = 'model_results/single_train/'
model_results_multiple = 'model_results/multiple_train/'
model_results_bump_single = 'model_results/bump_single_train/'
model_results_bump_multiple = 'model_results/bump_multiple_train/'

model_dep_results_single = 'model_results/model_dependent/single_train/'
model_dep_results_multiple = 'model_results/model_dependent/multiple_train/'
model_dep_results_bump_single = 'model_results/model_dependent/bump_single_train/'
model_dep_results_bump_multiple = 'model_results/model_dependent/bump_multiple_train/'

model_dep_results_boot = 'model_results/model_dependent/boot/'

dict_results_exc_reg_mod = 'dictionary_results/exclusion_region/model_independent/'
dict_results_exc_reg_mod_dep = 'dictionary_results/exclusion_region/model_dependent/'

plot_results = 'plot_results/'

columns = ['met', 'mt', 'mbb', 'mct2',
           'mlb1', 'nJet30', 'lep1Pt', 'nBJet30_MV2c10', 'jet1Pt',
           'trigMatch_metTrig', 'jet2Pt',
           'jet3Pt','jet4Pt', 'nLep_signal',
           'genWeight','eventWeight', 'pileupWeight',
           'leptonWeight','bTagWeight','jvtWeight']

columns_sig = ['met', 'mt', 'mbb', 'mct2',
               'mlb1', 'nJet30', 'lep1Pt', 'nBJet30_MV2c10',
               'genWeight','eventWeight', 'pileupWeight',
               'leptonWeight','bTagWeight','jvtWeight',
               'trigMatch_metTrig', 'nLep_signal']

cols = ['met', 'mt', 'mbb', 'mct2',
        'mlb1', 'lep1Pt', 'nJet30','nBJet30_MV2c10', 'weight']
