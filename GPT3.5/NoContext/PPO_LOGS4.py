nohup: ignoring input
/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: The following directories listed in your path were found to be non-existent: {PosixPath('http'), PosixPath('//xen03.iitd.ac.in'), PosixPath('3128')}
  warn(msg)
/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: The following directories listed in your path were found to be non-existent: {PosixPath('/usr/local/cuda/lib64')}
  warn(msg)
/home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:136: UserWarning: WARNING: No libcudart.so found! Install CUDA or the cudatoolkit package (anaconda)!
  warn(msg)
wandb: Currently logged in as: gurushajuneja (vgg16). Use `wandb login --relogin` to force relogin
wandb: wandb version 0.15.3 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.15.2
wandb: Run data is saved locally in /home/gurusha/wandb/run-20230606_125815-0sek6j1h
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run GPT3
wandb: ⭐️ View project at https://wandb.ai/vgg16/Reasoning_no_context
wandb: 🚀 View run at https://wandb.ai/vgg16/Reasoning_no_context/runs/0sek6j1h
Overriding torch_dtype=None with `torch_dtype=torch.float16` due to requirements of `bitsandbytes` to enable model loading in mixed int8. Either pass torch_dtype=torch.float16 or don't pass this argument at all to remove this warning.

===================================BUG REPORT===================================
Welcome to bitsandbytes. For bug reports, please submit your error trace to: https://github.com/TimDettmers/bitsandbytes/issues
================================================================================
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching /usr/local/cuda/lib64...
CUDA SETUP: Highest compute capability among GPUs detected: 8.0
CUDA SETUP: Detected CUDA version 117
CUDA SETUP: Loading binary /home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_cpu.so...
Loading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]Loading checkpoint shards:  33%|███▎      | 1/3 [00:09<00:18,  9.14s/it]Loading checkpoint shards:  67%|██████▋   | 2/3 [00:18<00:09,  9.18s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:24<00:00,  7.64s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:24<00:00,  8.06s/it]
  0%|          | 0/32 [00:00<?, ?it/s]  3%|▎         | 1/32 [04:42<2:26:09, 282.90s/it]  6%|▋         | 2/32 [09:06<2:15:42, 271.43s/it]  9%|▉         | 3/32 [13:56<2:15:13, 279.78s/it]REWARD +100
REWARD +100
REWARD +100
REWARD +100
RESPONSE LLAMA [' \n                    \nWhat is the discounted price of the item?\nWhat is the original price of the item?\nWhat is the total price of the item?\nWhat is the difference between the total price and the discounted price?\nWhat is the difference between the difference and the original price?</s>', ' \n                    \n                    \n    \n    \n</s>', ' \n                    \n                    ', ' \n                    \n                    ']
REWARD +100
################IMPROEMENT################# 0 The original price of an item is discounted 22%. A customer buys the item at this discounted price using a $20-off coupon. There is no tax on the item, and this was the only item the customer bought. If the customer paid $1.90 more than half the original price of the item, what was the original price of the item? A)$61  B)$65  C)$67.40  D)$70  E)$78.20  
  
                    
What is the discounted price of the item?
What is the original price of the item?
What is the total price of the item?
What is the difference between the total price and the discounted price?
What is the difference between the difference and the original price?</s> 
 . 
 
 Step 1: The original price of the item is x. 
 
 Step 2: The customer pays $1.90 more than half the original price of the item. 
 
 So, x/2 + 1.90 = x 
 
 Solving for x, we get x = 3.90 
 
 Therefore, the original price of the item is $3.90. 
 
 Answer: [[E]]. $3.90. 
 tensor(1.8791)
[0, 4, 0] [0, 1, 0]
REWARD +100
REWARD +100
REWARD +100
REWARD +100
REWARD +100
RESPONSE LLAMA [' \n                    \nWhat is the total number of components produced every month?\nWhat is the total cost of production every month?\nWhat is the total revenue from sales every month?\nWhat is the total profit every month?\nWhat is the total profit for the year?\nWhat is the minimum selling price per component that will guarantee that the yearly profit will be at least $626,400?</s>', ' \n                    \n                    \n                    \n                    ', ' \n                    \n                    ']
REWARD +100
################IMPROEMENT################# 2 Add: +45 and -30 A)-30  B)+30  C)0  D)15  E)-15  
  
                    
                     
 .
 
 +45 and -30
 
 We can think of this as +45 + (-30)
 
 So, the answer is +15
 
 Therefore, the answer is [[D]]. 
 tensor(1.)
[0, 9, 0] [0, 2, 0]
REWARD +100
RESPONSE LLAMA [' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n', ' \n                    \n                    ', ' \n                    \n                    What is the value of 5 + 5?\n                    What is the value of 5 + 5 + 5?\n                    What is the value of 5 + 5 + 5 + 5?\n                    What is the value of 5 + 5 + 5 + 5 + 5?\n                    What is the value of 5 + 5 + 5 + 5 + 5 + 5?\n                    What is the value of 5 + 5 + 5 + 5 + 5 + 5 + ', ' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n', ' \n                    \n                    ', ' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n', ' \n                    \n</s>']
[0, 10, 0] [0, 2, 0]
REWARD +100
REWARD +100
REWARD +100
RESPONSE LLAMA  12%|█▎        | 4/32 [19:14<2:17:40, 295.01s/it] 16%|█▌        | 5/32 [23:36<2:07:21, 283.01s/it] 19%|█▉        | 6/32 [28:28<2:03:58, 286.08s/it] 22%|██▏       | 7/32 [33:24<2:00:38, 289.56s/it] 25%|██▌       | 8/32 [37:44<1:52:00, 280.04s/it][' \n                    \n                    ', ' \n                    \nWhat is the equation for the computer routine?\nWhat is the equation for the first number?\nWhat is the equation for the second number?\nWhat is the equation for the first number squared?\nWhat is the equation for the second number?\nWhat is the equation for the first number squared minus the second number?\nWhat is the equation for the first number?\nWhat is the equation for the second number?\nWhat is the equation for the first number squared minus the second number?\nWhat is the equation for the first number?\nWhat is the equation for the second number?\nWhat is', ' \n                    \n                    ', ' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n', ' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n']
[0, 13, 0] [0, 2, 0]
REWARD +100
REWARD +100
REWARD +100
RESPONSE LLAMA [' \n                    \n</s>', ' \n                    \n                    ', ' \n                    \n                    ', ' \n                    \n                    \n                    \n                    \n                    ', ' \n                    \n                    \n                    ']
[0, 16, 0] [0, 2, 0]
REWARD +100
REWARD +100
REWARD +100
REWARD +100
RESPONSE LLAMA [' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n', ' \n                    \nHow many hours did it take hose A to fill the pool?\nHow many hours did it take hose B to fill the pool?\nWhat is the equation to be solved?</s>', ' \n                    \n    \n    \n    \n</s>', ' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n']
[0, 20, 0] [0, 2, 0]
REWARD +100
REWARD +100
RESPONSE LLAMA [' \n                    \n                    ', ' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    ', ' \n                    \n                    ', ' \n                    \n                    How many ways can 2 oranges be chosen from a basket of 10 oranges?\n                    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n    \n', ' \n                    \nHow many houses are to be painted?\nHow many days will it take Mr.Brown to paint 1 house?\nHow many days will it take Mr.Black to paint 1 house?\nHow many days will it take Mr.Blue to paint 1 house?\nHow many houses are to be painted?\nHow many days will it take Mr.Brown to paint 1 house?\nHow many days will it take Mr.Black to paint 1 house?\nHow many days will it take Mr.Blue to paint 1 house?\nHow many houses are to be painted?</s>', ' \n                    \n                    ']
[0, 22, 0] [0, 2, 0]
REWARD +100
REWARD +100
REWARD +100
REWARD +100
RESPONSE LLAMA [' \n                    \n                    ', ' \n                    \nWhat is the total number of chocolates?\nWhat is the number of chocolates that are cocoa flavored?\nWhat is the number of chocolates that are vanilla flavored?\nWhat is the number of chocolates that are not squashed?\nWhat is the number of chocolates that are both vanilla flavored and not squashed?</s>', ' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n', ' \n                    \n                    ']
[0, 26, 0] [0, 2, 0]
REWARD +100
 28%|██▊       | 9/32 [42:38<1:48:59, 284.31s/it] 31%|███▏      | 10/32 [46:31<1:38:26, 268.46s/it]