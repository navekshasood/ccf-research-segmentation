import torch


def config(VERSION):
    config = {
        'VERSION':VERSION,
        'OUTPUT_PATH':f'./result/{VERSION}/',
        'INPUT_PATH':'/N/u/soodn/Carbonate/colon-data-reprocessed/',
        'device':torch.device("cuda" if torch.cuda.is_available() else "cpu"),
        'tile_size':1024,
        'batch_size':16,
        'shift_h':0,
        'shift_w':0,
    }
    return config

def config_shift(VERSION):
    config = {
        'VERSION':VERSION,
        'OUTPUT_PATH':f'./result/{VERSION}/',
        'INPUT_PATH':'/N/u/soodn/Carbonate/colon-data-reprocessed/',
        'device':torch.device("cuda" if torch.cuda.is_available() else "cpu"),
        'tile_size':1024,
        'batch_size':16,
        'shift_h':512,
        'shift_w':512,
    }
    return config

VERSION = "02"
def train_config():
    config = {
        'split_seed_list':[0],
        'FOLD_LIST':[0,1,2,3],
        'VERSION':VERSION,
        'OUTPUT_PATH':f'./result/{VERSION}/',
        'INPUT_PATH':'/N/u/soodn/Carbonate/colon-data-reprocessed/',
        
        'train_data_path_list':[
            'result/01_01/', 
            'result/01_02/',
        ],
        
        'model_name':'seresnext101',
        
        'pretrain_path_list':[
            f'./hubmap-new-03-03/model_seed0_fold0_bestscore.pth',
            f'./hubmap-new-03-03/model_seed0_fold1_bestscore.pth',
            f'./hubmap-new-03-03/model_seed0_fold2_bestscore.pth',
            f'./hubmap-new-03-03/model_seed0_fold3_bestscore.pth',
        ],
        'trn_idxs_list_path':None, 
        'val_idxs_list_path':None,
        
        'num_classes':1,
        'input_resolution':(320,320),
        'resolution':(1024,1024),
        'dice_threshold':0.5,
        'small_mask_threshold':0,
        'multiplier_bin':20,
        'binned_max':4,
        'deepsupervision':True,
        'clfhead':True,
        'clf_threshold':None,
        
        'tta':1,
        'trn_batch_size':8,
        'test_batch_size':8,        
        'Adam':{
            'lr':1e-4,
            'betas':(0.9, 0.999),
            'weight_decay':1e-5,
        },
        'SGD':{
            'lr':0.01,
            'momentum':0.9,
        },

        'lr_scheduler_name':'CosineAnnealingLR', #'OneCycleLR', #'ReduceLROnPlateau', #'StepLR',#'WarmUpLinearDecay', 

        'lr_scheduler':{
            'ReduceLROnPlateau':{
                'factor':0.8,
                'patience':5,
                'min_lr':1e-5,
                'verbose':True,
            },
            'OneCycleLR':{
                'pct_start':0.1,
                'div_factor':1e3, 
                'max_lr':1e-2,
                'epochs':25,
            },
            'CosineAnnealingLR':{
                'step_size_min':1e-6,
                't0':19,
                'tmult':1,
                'curr_epoch':-1,
                'last_epoch':-1,
            },
            'WarmUpLinearDecay':{
                'train_steps':40,
                'warm_up_step':3,
            },
            'StepLR':{
                'milestones':[1,2,3,20,40],
                'multipliers':[0.5,0.3,0.1,0.03,0.003],
            },
        },
        'snapshot':True,
        
        'restart_epoch_list':[1,1,1,1,1], 
        'unfreeze_epoch':1,
        'num_epochs':100,
        'early_stopping':True,
        'patience':50,

        #'FP16':True, always True
        'num_workers':0,
        'device':torch.device("cuda" if torch.cuda.is_available() else "cpu"),
    }
    return config