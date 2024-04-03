import subprocess
#subprocess.run(['composer', '--version'])

subprocess.run(['composer', 'train/train.py','train/yamls/pretrain/mpt-125m.yaml', 'data_local=my-copy-c4', 'train_loader.dataset.split=train_small', 'eval_loader.dataset.split=val_small', 'max_duration=10ba', 'eval_interval=0', 'save_folder=mpt-125m'])

