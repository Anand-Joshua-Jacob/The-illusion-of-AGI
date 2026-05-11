- Research shows that the human brain processes visuals 60,000 times faster than text.[link](https://oit.williams.edu/files/2010/02/using-images-effectively.pdf)
- LLMs are bad at spatial reasoning
- I want to add a benchmark in a place where AI is not able to perform well so that we can make improvements in that area moving forward.
- This task isolates learning as there is no element of Metacogniton, executive functions or social cognition.(also attention?)
- For many current systems, learning occurs only during training or in-context. However, for truly robust and adaptive behavior, AI systems should be able to learn (and retain) new knowledge and skills over time (e.g., as part of a continuous
learning process). In this benchmark we will be testing in-context learning. But the context will contain (Choices the AI made and the outcomes??)
- Task 1 (_1, _2(1,2 and 1, 3), _3)
  - Has to learn initial and final from the first 2 images.
- Task 2 (_1, _2, _3)
  - Has to learn initial and final and arrows.
  - We have provided arrows in the first 2 images but expect the LLM to learn to understand even without the arrows in the later images.
- Task 3 (_1, _2, _3)
  - The scale of the stick figures are different
  - The stick figure has to move down by 2 units.
- Task 4, 5, 6 (_1, _2, _3)
  - No scale provided, just intuition


- LLMs know about inertia but have they seen it in action (very little image training compared to text) (assume)


### Problem Statement
- Research shows that the human brain processes visuals 60,000 times faster than text.[link](https://oit.williams.edu/files/2010/02/using-images-effectively.pdf) whereas LLMs are bad at spatial reasoning.
- I want to add a benchmark in a place where AI is not able to perform well so that we can make improvements in that area moving forward.
- In this benchmark we will be testing in-context learning of LLMs from images.

This is benchmark test [learning ability](https://github.com/Anand-Joshua-Jacob/The-illusion-of-AGI/tree/main) of LLMs
You can look at the chat logs [here](https://github.com/Anand-Joshua-Jacob/The-illusion-of-AGI/tree/main/LearningFromImages/results/html)

## Datasets and Tasks

There are 3 Kaggle datasets, each with an associated Kaggle task:
Each image in the Datasets were drawn by me, so they should not appear in any model’s training data.

1. [Dataset 1 – Jumping Task](https://www.kaggle.com/datasets/anandjoshuajacob/task-jumping)
2. [Dataset 2 – No Explicit Scale](https://www.kaggle.com/datasets/anandjoshuajacob/stickfigures-without-explicit-scale)
3. [Dataset 3 – Relabelled Directions](https://www.kaggle.com/datasets/anandjoshuajacob/visual-learning-3)


---

### Core Task Setup (All Datasets)

- Each dataset has 5 subtasks (e.g., `task1_1` to `task1_5`)
- Each subtask has 4 images:
  - **3 example images** (options A, B, C): show basic movements to the right, left and up.
  - **1 target image** (image 4): same for all subtasks in all 3 datasets.  
  - The first 3 images are presented to the LLM as **option A**, **option B**, and **option C**.
  - Target Image:  
    <img src="database/task1/task1_1/4.jpg" alt="Sample Image" width="300" style="margin-left:50px;">  
  - The **fourth image** (target) always shows:
    - Initial stickman position on the **left**
    - Final stickman position on the **right**
    - A **red region** between them that must be avoided
  - The LLM is told:
    - To avoid red.
    - Normal laws of physics apply.
    - It must find the **shortest sequence of moves** (a sequence over {A, B, C}) that reproduces the motion in the target image.
  
  
  ---
  ### Dataset 1 – Task Jumping
  **Link:** [Dataset 1 on Kaggle](https://www.kaggle.com/datasets/anandjoshuajacob/task-jumping)  
  - Contains **5 subtasks**: `task1_1` to `task1_5`. Each subtask has 4 images.
  #### Progressive removal of cues
  - **`task1_1`**:
    - Each of the 4 images shows **two stickmen**:
      - **Gray stickman**: initial position
      - **Black stickman**: final position
    - The 3 images indicating movement have:
      - **Labels** for initial and final positions.
      - **Arrows** indicating direction of motion.
    - Target image:
      - Only shows gray and black stickmen (no labels, no arrows).
    - LLM has to **learn** the gray and black stickman represents initial and final positions.
  - **`task1_2` to `task1_4`**:
    - The first image still has labels and arrows.
    - Labels/arrows are **gradually removed** in images 2 and 3.
    - Target image is same as earlier.
    - The LLM has fewer explicit cues to interpret the motions and target image.
  - **`task1_5`**:
    - Only the **first** image includes labels and arrows.
    - The remaining two images and the target image:
      - Show only gray and black stickmen.
      - No labels or arrows.
    - The LLM has only one image with cues and has to interpret the other images from that one shot example.
  #### Additional Visual Cues
  - A **scale** is shown in both the **X and Y directions**.
  - This allows the LLM to see that the stickman moves specific distances from one position to another and to compare these movements to the target image.
  
  #### Challenge for the LLM
    - **Learn** what the Gray and Black stick man represent.
    - **Infer** what each option (A, B, C) does in the images.
    - **Infer** what kind of motion the target image represents.
    - **Reason** and come up with a minimal action sequence that matches the target.

  #### Correct reasoning:  
  - Moving right first leads the stickman directly into the red region. The shortest valid sequence is:
    1. **Jump (up)** to clear the obstacle.
    2. **Move right** and then fall due to gravity.
  - So the correct sequence in Dataset 1 is `"CA"` (jump, then move right).
  ---
### Dataset 2 – Without Explicit Scale
  **Link:** [Dataset 2 on Kaggle](https://www.kaggle.com/datasets/anandjoshuajacob/stickfigures-without-explicit-scale)
  - Contains **5 subtasks**: `task2_1` to `task2_5`.
  - Structurally the **same as Dataset 1**, but:
    - There is **no explicit X/Y scale** in the images.
  #### Motivation
  In Dataset 1, many LLMs responded by reasoning in terms of exact units, e.g.,  
  “The stick figure moved X units to the right from coordinate (a, b) to (c, d).”
  For Dataset 2:
  - The scale is **removed**.
  - The LLM must:
    - Internally form approximate representations of vertical and lateral movements.
    - Compare these to the target image to determine which sequence recreates the target displacement.  

    
 The **correct sequence** remains:
   - Jump, then move right → `"CA"`.
  ---
### Dataset 3 – Relabelled Directions
  **Link:** [Dataset 3 on Kaggle](https://www.kaggle.com/datasets/anandjoshuajacob/visual-learning-3)
  - Contains **5 subtasks**: `task3_1` to `task3_5`.
  - Structurally the **same as Dataset 1**, but **option meanings are permuted**.
  #### Changed Option Mapping
  - **Option A** → movement up
  - **Option B** → movement left
  - **Option C** → movement right
 #### Motivation
  - Left and right are opposites, so it is relatively easy for an LLM to relate labels and arrows between left/right images.
  - This dataset tests whether the LLM can:
    - Transfer what it learns from an **“up”** image (jump) to **lateral** movement images and to the target image.  


The **correct sequence** is:
  - Jump, then move right → `"AC"`.


### Benchmark Construction and Scoring

- There are 3 Kaggle tasks (one per dataset).
- Each Kaggle task has 5 subtasks.
- For each subtask:
  - The model is run for 5 trials.
  - Each correct final answer sequence irrespective of reasoning quality = 1 point, incorrect = 0.
- Score per Kaggle task:
  - Average over 25 runs (5 subtasks × 5 trials).
- Overall benchmark score:
  - Average of the 3 Kaggle task scores.

---

### Technical details 
- This task isolates learning and reasoning as there is no element of Metacogniton, executive functions or social cognition. It may contain some attention too as to which part of the image to focus on, but all LLMs are very good at this and it does not affect the final score.


### Results, insights, and conclusions
- For the task, I modified the prompt to make it easier for the LLM to get a reasonable score. But during this I was using google/gemini 3 flash preview. It seems to have fine-tuned the task to be easy for this particular model and so gemini 3 flash preview perform consistently well. 
- Also when I ran the task on a text only model, it guessed the right answer simply by guessing what the each image and the final task would be simply based on my prompt. So maybe the LLMs are not learning purely based on what they see in the images.



### Organizational affiliations
Working in a Japanese Automobile company, nothing crazy. 

### References & citations
https://oit.williams.edu/files/2010/02/using-images-effectively.pdf