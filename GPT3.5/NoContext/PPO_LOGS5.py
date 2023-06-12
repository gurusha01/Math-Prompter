wandb: Currently logged in as: gurushajuneja (vgg16). Use `wandb login --relogin` to force relogin
wandb: wandb version 0.15.3 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.15.2
wandb: Run data is saved locally in /home/gurusha/wandb/run-20230606_145234-4i9rhzpn
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run GPT3
wandb: ⭐️ View project at https://wandb.ai/vgg16/Reasoning_no_context
wandb: 🚀 View run at https://wandb.ai/vgg16/Reasoning_no_context/runs/4i9rhzpn
Overriding torch_dtype=None with `torch_dtype=torch.float16` due to requirements of `bitsandbytes` to enable model loading in mixed int8. Either pass torch_dtype=torch.float16 or don't pass this argument at all to remove this warning.

===================================BUG REPORT===================================
Welcome to bitsandbytes. For bug reports, please submit your error trace to: https://github.com/TimDettmers/bitsandbytes/issues
================================================================================
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching /usr/local/cuda/lib64...
CUDA SETUP: Highest compute capability among GPUs detected: 8.0
CUDA SETUP: Detected CUDA version 117
CUDA SETUP: Loading binary /home/gurusha/alpaca-lora/finetune-llama/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_cpu.so...
Loading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]Loading checkpoint shards:  33%|███▎      | 1/3 [00:09<00:19,  9.59s/it]Loading checkpoint shards:  67%|██████▋   | 2/3 [00:18<00:09,  9.40s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:24<00:00,  7.90s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:24<00:00,  8.32s/it]
  0%|          | 0/22 [00:00<?, ?it/s]RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:Julie’s yard is rectangular. One side of the yard is 100 feet wide. The total area of the yard is 3,000 square feet. What is the length of the other side of the yard? A)30 feet  B)20 feet  C)10 feet  D)50 feet  E)60 feet ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:A square piece of cloth is trimmed by 4 feet on one edge to form a rectangular piece, which is then cut diagonally in half to create two triangles. If the area of each of triangle is 70 square feet, what was the perimeter (in feet) of the original piece of square cloth? A)56  B)58  C)60  D)62  E)64 ?\n Answer: \n Let us think step by step', '\n Question:The length of the ribbon was originally 30 cm. It was reduced in the ratio 5 : 3. What is its length now? A)18  B)30  C)6  D)15  E)12 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step', '\n Question:If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now? A)37  B)41  C)40  D)42  E)43 ?\n Answer: \n Let us think step by step'] . 
 
 Arjun has x amount of money. 
 
 Sajal has y amount of money. 
 
 When Arjun gives $30 to Sajal, Sajal will have twice the money left with Arjun. 
 
 So, y + 30 = 2x 
 
 When Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. 
 
 So, x + 10 = 3y 
 
 Solving the two equations, we get 
 
 x = 62 
 
 y = 34 
 
 Therefore, the answer is C)34, 62.
RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:Julie’s yard is rectangular. One side of the yard is 100 feet wide. The total area of the yard is 3,000 square feet. What is the length of the other side of the yard? A)30 feet  B)20 feet  C)10 feet  D)50 feet  E)60 feet ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:A square piece of cloth is trimmed by 4 feet on one edge to form a rectangular piece, which is then cut diagonally in half to create two triangles. If the area of each of triangle is 70 square feet, what was the perimeter (in feet) of the original piece of square cloth? A)56  B)58  C)60  D)62  E)64 ?\n Answer: \n Let us think step by step', '\n Question:The length of the ribbon was originally 30 cm. It was reduced in the ratio 5 : 3. What is its length now? A)18  B)30  C)6  D)15  E)12 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step', '\n Question:If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now? A)37  B)41  C)40  D)42  E)43 ?\n Answer: \n Let us think step by step'] . 
 
 We know that the width of the yard is 100 feet. 
 We also know that the total area of the yard is 3,000 square feet. 
 
 We can use the formula for area of a rectangle to solve this problem. 
 
 Area = Length x Width 
 
 3,000 = Length x 100 
 
 Length = 3,000/100 
 
 Length = 30 feet 
 
 Therefore, the length of the other side of the yard is 30 feet. 
 
 Answer: [[A]]
RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:Julie’s yard is rectangular. One side of the yard is 100 feet wide. The total area of the yard is 3,000 square feet. What is the length of the other side of the yard? A)30 feet  B)20 feet  C)10 feet  D)50 feet  E)60 feet ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:A square piece of cloth is trimmed by 4 feet on one edge to form a rectangular piece, which is then cut diagonally in half to create two triangles. If the area of each of triangle is 70 square feet, what was the perimeter (in feet) of the original piece of square cloth? A)56  B)58  C)60  D)62  E)64 ?\n Answer: \n Let us think step by step', '\n Question:The length of the ribbon was originally 30 cm. It was reduced in the ratio 5 : 3. What is its length now? A)18  B)30  C)6  D)15  E)12 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step', '\n Question:If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now? A)37  B)41  C)40  D)42  E)43 ?\n Answer: \n Let us think step by step'] . 
 
 The greatest common factor of two positive integers is 11. 
 
 This means that the two integers have 11 as a common factor. 
 
 The least common multiple of these two integers is 7700. 
 
 This means that the two integers have 7700 as their least common multiple. 
 
 We know that one of the integers is 350. 
 
 We can use the fact that the greatest common factor of two integers is the product of the two integers divided by their least common multiple. 
 
 Therefore, the other integer is (11 x 350) / 7700 = 412. 
 
 Hence, the answer is [[D]].
RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:Julie’s yard is rectangular. One side of the yard is 100 feet wide. The total area of the yard is 3,000 square feet. What is the length of the other side of the yard? A)30 feet  B)20 feet  C)10 feet  D)50 feet  E)60 feet ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:A square piece of cloth is trimmed by 4 feet on one edge to form a rectangular piece, which is then cut diagonally in half to create two triangles. If the area of each of triangle is 70 square feet, what was the perimeter (in feet) of the original piece of square cloth? A)56  B)58  C)60  D)62  E)64 ?\n Answer: \n Let us think step by step', '\n Question:The length of the ribbon was originally 30 cm. It was reduced in the ratio 5 : 3. What is its length now? A)18  B)30  C)6  D)15  E)12 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step', '\n Question:If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now? A)37  B)41  C)40  D)42  E)43 ?\n Answer: \n Let us think step by step'] . 
 
 Step 1: The original piece of cloth is a square. 
 
 Step 2: The square is trimmed by 4 feet on one edge to form a rectangular piece. 
 
 Step 3: The rectangular piece is cut diagonally in half to create two triangles. 
 
 Step 4: The area of each of the triangles is 70 square feet. 
 
 From the given information, we can calculate the perimeter of the original square piece of cloth. 
 
 The area of a triangle is given by A = 1/2 * b * h, where b is the base and h is the height. 
 
 Since the area of each triangle is 70 square feet, we can calculate the base and height of each triangle. 
 
 b = 14 feet 
 
 h = 10 feet 
 
 The perimeter of the original square piece of cloth is given by P = 4 * b = 4 * 14 = 56 feet. 
 
 Therefore, the answer is [[A]].
RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:Julie’s yard is rectangular. One side of the yard is 100 feet wide. The total area of the yard is 3,000 square feet. What is the length of the other side of the yard? A)30 feet  B)20 feet  C)10 feet  D)50 feet  E)60 feet ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:A square piece of cloth is trimmed by 4 feet on one edge to form a rectangular piece, which is then cut diagonally in half to create two triangles. If the area of each of triangle is 70 square feet, what was the perimeter (in feet) of the original piece of square cloth? A)56  B)58  C)60  D)62  E)64 ?\n Answer: \n Let us think step by step', '\n Question:The length of the ribbon was originally 30 cm. It was reduced in the ratio 5 : 3. What is its length now? A)18  B)30  C)6  D)15  E)12 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step', '\n Question:If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now? A)37  B)41  C)40  D)42  E)43 ?\n Answer: \n Let us think step by step'] .
 
 Step 1: The ratio of reduction is 5:3.
 
 Step 2: This means that the ribbon was reduced by 5 parts out of 8 parts.
 
 Step 3: The length of the ribbon was originally 30 cm.
 
 Step 4: So, the length of the ribbon now is 30 cm - (5/8) × 30 cm = 18 cm.
 
 Hence, the answer is [[A]].
RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:Julie’s yard is rectangular. One side of the yard is 100 feet wide. The total area of the yard is 3,000 square feet. What is the length of the other side of the yard? A)30 feet  B)20 feet  C)10 feet  D)50 feet  E)60 feet ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:A square piece of cloth is trimmed by 4 feet on one edge to form a rectangular piece, which is then cut diagonally in half to create two triangles. If the area of each of triangle is 70 square feet, what was the perimeter (in feet) of the original piece of square cloth? A)56  B)58  C)60  D)62  E)64 ?\n Answer: \n Let us think step by step', '\n Question:The length of the ribbon was originally 30 cm. It was reduced in the ratio 5 : 3. What is its length now? A)18  B)30  C)6  D)15  E)12 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step', '\n Question:If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now? A)37  B)41  C)40  D)42  E)43 ?\n Answer: \n Let us think step by step'] .
 
 M = abc
 
 N = cba
 
 M > N
 
 M - N + 396c = 990
 
Substituting the values of M and N,

abc - cba + 396c = 990

100a + 10b + c - 100c - 10b - a + 396c = 990

100a + 396c = 990

a = 990 - 396c/100

Now, for M to be more than 300,

abc > 300

990 - 396c/100 > 3

990 - 396c > 300

690 > 396c

c > 1.7

Since c is a single digit number, c can only be 2 or more.

Therefore, the number of values of M more than 300 is 40.

Answer: [[C]]
RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:Julie’s yard is rectangular. One side of the yard is 100 feet wide. The total area of the yard is 3,000 square feet. What is the length of the other side of the yard? A)30 feet  B)20 feet  C)10 feet  D)50 feet  E)60 feet ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:A square piece of cloth is trimmed by 4 feet on one edge to form a rectangular piece, which is then cut diagonally in half to create two triangles. If the area of each of triangle is 70 square feet, what was the perimeter (in feet) of the original piece of square cloth? A)56  B)58  C)60  D)62  E)64 ?\n Answer: \n Let us think step by step', '\n Question:The length of the ribbon was originally 30 cm. It was reduced in the ratio 5 : 3. What is its length now? A)18  B)30  C)6  D)15  E)12 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step', '\n Question:If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now? A)37  B)41  C)40  D)42  E)43 ?\n Answer: \n Let us think step by step'] .
 
 20% of the students took physics, so 80% of the students did not take physics.
 
 28% of the students took math, so 72% of the students did not take math.
 
 80% of the students did not take physics and 72% of the students did not take math.
 
 So, the least possible number of students in the school is 600.
 
 Therefore, the answer is [[C]].
RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:Julie’s yard is rectangular. One side of the yard is 100 feet wide. The total area of the yard is 3,000 square feet. What is the length of the other side of the yard? A)30 feet  B)20 feet  C)10 feet  D)50 feet  E)60 feet ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:A square piece of cloth is trimmed by 4 feet on one edge to form a rectangular piece, which is then cut diagonally in half to create two triangles. If the area of each of triangle is 70 square feet, what was the perimeter (in feet) of the original piece of square cloth? A)56  B)58  C)60  D)62  E)64 ?\n Answer: \n Let us think step by step', '\n Question:The length of the ribbon was originally 30 cm. It was reduced in the ratio 5 : 3. What is its length now? A)18  B)30  C)6  D)15  E)12 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step', '\n Question:If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now? A)37  B)41  C)40  D)42  E)43 ?\n Answer: \n Let us think step by step'] .
 
 5 years ago, Raj was 12 years old and Rahim was 36 years old.
 
 Now, Raj is 17 years old and Rahim is 5 years older than he was 5 years ago.
 
 Therefore, Rahim is now 41 years old.
 
 [[B]]
REWARD +100
REWARD +100
REWARD +100
REWARD +100
RESPONSE LLAMA [' \n                    \n</s>', ' \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n', ' \n                    \n                    ', ' \n                    \n                    ']
RESPONSE ['\n Question:Arjun and Sajal are friends, each has some money. If Arun gives $30 to Sajal, the Sajal will have twice the money left with Arjun. But, if Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. How much money does each have? A)62, 35  B)62, 34  C)34, 62  D)42, 62  E)62, 42 ?\n Answer: \n Let us think step by step', '\n Question:The greatest common factor of two positive integers is 11. The least common multiple of these two integers is 7700. If one of the integers is 350, what is the other? A)242  B)308  C)352  D)412  E)456 ?\n Answer: \n Let us think step by step', '\n Question:M = abc is a three digit number and N = cba, if M > N and M - N + 396c = 990. Then how many values of M are more than 300. A)20  B)30  C)40  D)200  E)None ?\n Answer: \n Let us think step by step', '\n Question:there are more than 501 students in a school such that 20% of them exactly took physics and 28% of them exactly took math. What could be the least possible no of students in the school? A)550  B)570  C)600  D)700  E)none of these ?\n Answer: \n Let us think step by step'] . 
 
 Arjun has x amount of money. 
 
 Sajal has y amount of money. 
 
 When Arjun gives $30 to Sajal, Sajal will have twice the money left with Arjun. 
 
 So, y + 30 = 2x 
 
 When Sajal gives $10 to Arjun, Arjun will have thrice as much as is left with Sajal. 
 
 So, x + 10 = 3y 
 
 Solving the two equations, we get 
 
 x = 62 
 
 y = 34 
 
 So, Arjun has $62 and Sajal has $34. 
 
 Answer: [[C]], 34, 62
RESPONSE 