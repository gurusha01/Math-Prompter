nohup: ignoring input
/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: The following directories listed in your path were found to be non-existent: {PosixPath('http'), PosixPath('3128'), PosixPath('//xen03.iitd.ac.in')}
  warn(msg)
/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: The following directories listed in your path were found to be non-existent: {PosixPath('/usr/local/cuda/lib64')}
  warn(msg)
/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: No libcudart.so found! Install CUDA or the cudatoolkit package (anaconda)!
  warn(msg)
wandb: Currently logged in as: gurushajuneja (vgg16). Use `wandb login --relogin` to force relogin
wandb: wandb version 0.15.3 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.15.2
wandb: Run data is saved locally in /home/gurusha/wandb/run-20230606_212458-v1rcqn7m
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run GPT3
wandb: ⭐️ View project at https://wandb.ai/vgg16/Reasoning_context
wandb: 🚀 View run at https://wandb.ai/vgg16/Reasoning_context/runs/v1rcqn7m
Overriding torch_dtype=None with `torch_dtype=torch.float16` due to requirements of `bitsandbytes` to enable model loading in mixed int8. Either pass torch_dtype=torch.float16 or don't pass this argument at all to remove this warning.

===================================BUG REPORT===================================
Welcome to bitsandbytes. For bug reports, please submit your error trace to: https://github.com/TimDettmers/bitsandbytes/issues
================================================================================
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching /usr/local/cuda/lib64...
CUDA SETUP: Highest compute capability among GPUs detected: 8.0
CUDA SETUP: Detected CUDA version 117
CUDA SETUP: Loading binary /home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_cpu.so...

