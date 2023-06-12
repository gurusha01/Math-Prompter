wandb: Currently logged in as: gurushajuneja (vgg16). Use `wandb login --relogin` to force relogin
wandb: - Waiting for wandb.init()...
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.15.2
wandb: Run data is saved locally in /home/gurusha/wandb/run-20230611_235313-7me6o5zy
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run LLAMA13B-GPT-Finetuned
wandb: ⭐️ View project at https://wandb.ai/vgg16/Reasoning_no_context
wandb: 🚀 View run at https://wandb.ai/vgg16/Reasoning_no_context/runs/7me6o5zy
Overriding torch_dtype=None with `torch_dtype=torch.float16` due to requirements of `bitsandbytes` to enable model loading in mixed int8. Either pass torch_dtype=torch.float16 or don't pass this argument at all to remove this warning.

===================================BUG REPORT===================================
Welcome to bitsandbytes. For bug reports, please submit your error trace to: https://github.com/TimDettmers/bitsandbytes/issues
================================================================================
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching /usr/local/cuda/lib64...
CUDA SETUP: Highest compute capability among GPUs detected: 8.0
CUDA SETUP: Detected CUDA version 117
CUDA SETUP: Loading binary /home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_cpu.so...

/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: The following directories listed in your path were found to be non-existent: {PosixPath('3128'), PosixPath('//xen03.iitd.ac.in'), PosixPath('http')}
  warn(msg)
/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: The following directories listed in your path were found to be non-existent: {PosixPath('/usr/local/cuda/lib64')}
  warn(msg)
/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: No libcudart.so found! Install CUDA or the cudatoolkit package (anaconda)!
  warn(msg)
wandb: Currently logged in as: gurushajuneja (vgg16). Use `wandb login --relogin` to force relogin
wandb: - Waiting for wandb.init()...
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.15.2
wandb: Run data is saved locally in /home/gurusha/wandb/run-20230611_235403-3mcb04gk
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run LLAMA13B-GPT-Finetuned
wandb: ⭐️ View project at https://wandb.ai/vgg16/Reasoning_no_context
wandb: 🚀 View run at https://wandb.ai/vgg16/Reasoning_no_context/runs/3mcb04gk
Overriding torch_dtype=None with `torch_dtype=torch.float16` due to requirements of `bitsandbytes` to enable model loading in mixed int8. Either pass torch_dtype=torch.float16 or don't pass this argument at all to remove this warning.

===================================BUG REPORT===================================
Welcome to bitsandbytes. For bug reports, please submit your error trace to: https://github.com/TimDettmers/bitsandbytes/issues
================================================================================
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching /usr/local/cuda/lib64...
CUDA SETUP: Highest compute capability among GPUs detected: 8.0
CUDA SETUP: Detected CUDA version 117
CUDA SETUP: Loading binary /home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_cpu.so...




Overriding torch_dtype=None with `torch_dtype=torch.float16` due to requirements of `bitsandbytes` to enable model loading in mixed int8. Either pass torch_dtype=torch.float16 or don't pass this argument at all to remove this warning.












../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [1,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [2,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [3,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [4,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [5,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [6,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [7,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [8,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [9,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [10,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [11,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [12,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [13,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [14,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [15,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [16,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [17,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [18,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [19,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [20,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [21,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [22,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [23,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [24,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [25,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [26,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [27,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [28,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [29,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [30,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [31,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [32,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [33,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [34,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [35,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [36,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [37,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [38,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [39,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [40,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [41,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [42,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [43,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [44,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [45,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [46,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [47,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [48,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [49,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [50,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [51,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [52,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [53,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [54,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [55,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [56,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [57,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [58,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [59,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [60,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [61,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [62,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [63,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [64,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [65,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [66,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [67,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [68,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [69,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [70,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [71,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [72,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [73,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [74,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [75,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [76,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [77,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [78,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [79,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [80,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [81,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [82,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [83,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [84,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [85,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [86,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [87,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [88,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [89,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [90,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [91,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [92,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [93,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [94,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [95,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [96,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [97,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [98,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [99,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [100,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [101,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [102,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [103,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [104,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [105,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [106,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [107,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [108,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [109,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [110,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [111,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [112,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [113,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [114,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [115,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [116,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [117,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [118,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [119,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [120,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [121,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [122,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [123,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [124,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [125,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [126,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [53,0,0], thread: [127,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [96,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [97,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [98,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [99,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [100,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [101,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [102,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [103,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [104,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [105,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [106,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [107,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [108,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [109,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [110,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [111,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [112,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [113,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [114,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [115,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [116,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [117,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [118,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [119,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [120,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [121,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [122,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [123,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [124,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [125,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [126,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [127,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [64,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [65,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [66,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [67,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [68,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [69,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [70,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [71,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [72,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [73,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [74,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [75,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [76,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [77,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [78,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [79,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [80,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [81,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [82,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [83,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [84,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [85,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [86,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [87,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [88,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [89,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [90,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [91,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [92,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [93,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [94,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [95,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [32,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [33,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [34,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [35,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [36,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [37,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [38,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [39,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [40,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [41,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [42,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [43,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [44,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [45,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [46,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [47,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [48,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [49,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [50,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [51,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [52,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [53,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [54,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [55,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [56,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [57,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [58,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [59,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [60,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [61,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [62,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [63,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [0,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [1,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [2,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [3,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [4,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [5,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [6,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [7,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [8,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [9,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [10,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [11,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [12,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [13,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [14,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [15,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [16,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [17,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [18,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [19,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [20,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [21,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [22,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [23,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [24,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [25,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [26,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [27,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [28,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [29,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [30,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [34,0,0], thread: [31,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [64,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [65,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [66,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [67,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [68,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [69,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [70,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [71,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [72,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [73,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [74,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [75,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [76,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [77,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [78,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [79,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [80,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [81,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [82,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [83,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [84,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [85,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [86,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [87,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [88,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [89,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [90,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [91,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [92,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [93,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [94,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [6,0,0], thread: [95,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [0,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [1,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [2,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [3,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [4,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [5,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [6,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [7,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [8,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [9,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [10,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [11,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [12,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [13,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [14,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [15,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [16,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [17,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [18,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [19,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [20,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [21,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [22,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [23,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [24,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [25,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [26,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [27,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [28,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [29,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [30,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [31,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [32,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [33,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [34,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [35,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [36,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [37,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [38,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [39,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [40,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [41,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [42,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [43,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [44,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [45,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [46,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [47,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [48,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [49,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [50,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [51,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [52,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [53,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [54,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [55,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [56,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [57,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [58,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [59,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [60,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [61,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [62,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [63,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [64,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [65,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [66,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [67,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [68,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [69,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [70,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [71,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [72,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [73,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [74,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [75,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [76,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [77,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [78,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [79,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [80,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [81,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [82,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [83,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [84,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [85,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [86,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [87,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [88,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [89,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [90,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [91,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [92,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [93,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [94,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [95,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [96,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [97,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [98,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [99,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [100,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [101,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [102,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [103,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [104,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [105,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [106,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [107,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [108,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [109,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [110,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [111,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [112,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [113,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [114,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [115,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [116,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [117,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [118,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [119,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [120,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [121,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [122,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [123,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [124,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [125,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [126,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [48,0,0], thread: [127,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [96,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [97,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [98,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [99,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [100,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [101,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [102,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [103,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [104,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [105,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [106,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [107,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [108,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [109,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [110,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [111,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [112,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [113,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [114,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [115,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [116,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [117,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [118,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [119,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [120,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [121,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [122,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [123,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [124,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [125,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [126,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [127,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [0,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [1,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [2,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [3,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [4,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [5,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [6,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [7,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [8,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [9,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [10,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [11,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [12,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [13,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [14,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [15,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [16,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [17,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [18,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [19,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [20,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [21,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [22,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [23,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [24,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [25,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [26,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [27,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [28,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [29,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [30,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [31,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [32,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [33,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [34,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [35,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [36,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [37,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [38,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [39,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [40,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [41,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [42,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [43,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [44,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [45,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [46,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [47,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [48,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [49,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [50,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [51,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [52,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [53,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [54,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [55,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [56,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [57,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [58,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [59,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [60,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [61,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [62,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [63,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [64,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [65,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [66,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [67,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [68,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [69,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [70,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [71,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [72,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [73,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [74,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [75,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [76,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [77,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [78,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [79,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [80,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [81,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [82,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [83,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [84,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [85,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [86,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [87,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [88,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [89,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [90,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [91,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [92,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [93,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [94,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
../aten/src/ATen/native/cuda/Indexing.cu:1093: indexSelectSmallIndex: block: [16,0,0], thread: [95,0,0] Assertion `srcIndex < srcSelectDimSize` failed.

RESPONSE LLAMA [' \n                    \n                    How many black cards are in pile $A$?\nHow many red cards are in pile $A$?\nHow many black cards are in pile $B$?\nHow many red cards are in pile $B$?\n</s>']
[0, 0, 0, 0] [0, 0, 0, 0] [0, 0, 0, 1]
RESPONSE LLAMA [' \n                    What is the graph of $f(x)=\\frac{2x}{x^2-5x-14}$?\nWhat are the vertical asymptotes of the graph?\nWhat is the horizontal asymptote of the graph?\nWhat is the sum of the vertical asymptotes and the horizontal asymptote?\n</s>']
Traceback (most recent call last):
  File "/home/gurusha/Galacticia30B/NoContext/ppo_train_13B.py", line 408, in <module>
    dones, outputs, rewards, cot = env.step(False, response, questions_n, answers_n, dones_0, 0.95)
  File "/home/gurusha/Galacticia30B/NoContext/Environment.py", line 87, in step
    dones, outputs, rewards = self.generate_env(input, answers, dones_prev, T)
  File "/home/gurusha/Galacticia30B/NoContext/Environment.py", line 130, in generate_env
    outputs = self.generate(outs, T)
  File "/home/gurusha/Galacticia30B/NoContext/Environment.py", line 163, in generate
    outputs=self.model.generate(
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/transformers/generation/utils.py", line 1406, in generate
    return self.greedy_search(
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/transformers/generation/utils.py", line 2201, in greedy_search
    outputs = self(
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/transformers/models/opt/modeling_opt.py", line 930, in forward
    outputs = self.model.decoder(
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/transformers/models/opt/modeling_opt.py", line 696, in forward
    layer_outputs = decoder_layer(
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/transformers/models/opt/modeling_opt.py", line 326, in forward
    hidden_states, self_attn_weights, present_key_value = self.self_attn(
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/transformers/models/opt/modeling_opt.py", line 171, in forward
    query_states = self.q_proj(hidden_states) * self.scaling
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/nn/modules.py", line 242, in forward
    out = bnb.matmul(x, self.weight, bias=self.bias, state=self.state)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/autograd/_functions.py", line 488, in matmul
    return MatMul8bitLt.apply(A, B, out, bias, state)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/torch/autograd/function.py", line 506, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/autograd/_functions.py", line 303, in forward
    CA, CAt, SCA, SCAt, coo_tensorA = F.double_quant(A.to(torch.float16), threshold=state.threshold)
  File "/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/functional.py", line 1634, in double_quant
    nnz = nnz_row_ptr[-1].item()
RuntimeError: CUDA error: device-side assert triggered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

wandb: Waiting for W&B process to finish... (failed 1). Press Control-C to abort syncing.
wandb: - 0.006 MB of 0.006 MB uploaded (0.000 MB deduped)
wandb: Run history:
wandb:             env/reward_dist ▁
wandb:             env/reward_mean ▁
wandb:           objective/entropy ▁
wandb:                objective/kl ▁
wandb:           objective/kl_coef ▁
wandb:           objective/kl_dist ▁
wandb:           ppo/learning_rate ▁
wandb:             ppo/loss/policy ▁
wandb:              ppo/loss/total ▁
wandb:              ppo/loss/value ▁
wandb:   ppo/mean_non_score_reward ▁
wandb:  ppo/policy/advantages_mean ▁
wandb:         ppo/policy/approxkl ▁
wandb:         ppo/policy/clipfrac ▁
wandb:          ppo/policy/entropy ▁
wandb:         ppo/policy/policykl ▁
wandb:            ppo/returns/mean ▁
wandb:             ppo/returns/var ▁
wandb: ppo/time/ppo/optimizer_step ▁
wandb:            ppo/val/clipfrac ▁
wandb:               ppo/val/error ▁
wandb:                ppo/val/mean ▁
wandb:                 ppo/val/var ▁
wandb:       ppo/val/var_explained ▁
wandb:               ppo/val/vpred ▁
wandb:         time/ppo/calc_stats ▁
wandb:    time/ppo/compute_rewards ▁
wandb:       time/ppo/forward_pass ▁
wandb:      time/ppo/optimize_step ▁
wandb:              time/ppo/total ▁
wandb: 
wandb: Run summary:
wandb:             env/reward_dist 0.57945
wandb:             env/reward_mean 0.57945
wandb:              env/reward_std nan
wandb:           objective/entropy 50.62499
wandb:                objective/kl 6.00302
wandb:           objective/kl_coef 0.01
wandb:           objective/kl_dist 6.00302
wandb:           ppo/learning_rate 1e-05
wandb:             ppo/loss/policy -0.0
wandb:              ppo/loss/total 0.0225
wandb:              ppo/loss/value 0.22499
wandb:   ppo/mean_non_score_reward -0.00107
wandb:  ppo/policy/advantages_mean 0.0
wandb:         ppo/policy/approxkl 0.0
wandb:         ppo/policy/clipfrac 0.0
wandb:          ppo/policy/entropy 0.71338
wandb:         ppo/policy/policykl 0.0
wandb:            ppo/returns/mean 0.3932
wandb:             ppo/returns/var 0.03122
wandb: ppo/time/ppo/optimizer_step 1e-05
wandb:            ppo/val/clipfrac 0.32143
wandb:               ppo/val/error 0.3902
wandb:                ppo/val/mean 0.20777
wandb:                 ppo/val/var 0.49218
wandb:       ppo/val/var_explained -11.49716
wandb:               ppo/val/vpred 0.25349
wandb:         time/ppo/calc_stats 0.01822
wandb:    time/ppo/compute_rewards 0.047
wandb:       time/ppo/forward_pass 1.90472
wandb:      time/ppo/optimize_step 5.10837
wandb:              time/ppo/total 7.4681
wandb: 
wandb: 🚀 View run LLAMA13B-GPT-Finetuned at: https://wandb.ai/vgg16/Reasoning_no_context/runs/3mcb04gk
wandb: Synced 5 W&B file(s), 1 media file(s), 1 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20230611_235403-3mcb04gk/logs