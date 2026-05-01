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

### Project Name
Visual Learning

### Your Team
Joshua

### Problem Statement
- Research shows that the human brain processes visuals 60,000 times faster than text.[link](https://oit.williams.edu/files/2010/02/using-images-effectively.pdf) whereas LLMs are bad at spatial reasoning.
- I want to add a benchmark in a place where AI is not able to perform well so that we can make improvements in that area moving forward.
- In this benchmark we will be testing in-context learning of LLMs from images.

### Dataset
There are 3 datasets. All are drawn by me so there is no data leakage.

#### Dataset 1 
- Each task consists of 4 images. The first 3 show a stick figure moving right, left and up. The 4th image is a target image with initial and final stick figure positions and a red block in the middle that is meant to be jumped over.
- In the 1st image description, "Initial" and "Final" labels are provided to guide the model to understand the images, but in the later images, the model is expected to learn these conventions.
- The labels and arrows are gradually stripped away in later task to find out upto what limit the LLM required guidance in understanding an Image

#### Dataset 2
- Same as Dataset 1 but without a scale shown to the side. 
- Most LLMs reasoned saying the Stickfigure moved 6 units to the right from this coordinate to that one. So I wanted to see how they would perform if no explicit scale was provided for the LLMs to make these calculations. They have to internally form intuitions of the stickman moving up or sideways.

#### Dataset 3
- Same as Dataset 1 but the first move is "Up"
- Right and left are just opposites of each other, so it is easy for the LLM to understand and relate the labels present in the Right image to the left image.
- I now want to test if the LLM can relate labels and arrows in an "up" image to lateral movement images.


### Task & benchmark construction
- I have created 3 tasks corresponding to the 3 Datasets above. 
- Each task runs 5 trials and takes the average of them as the result.
- Therefore since each Dataset has 5 tasks, Each "Kaggle task" in the benchmark run each of these 5 tasks 5 times and takes a macro average for the final score.


### Technical details 
- This task isolates learning and reasoning as there is no element of Metacogniton, executive functions or social cognition. It may contain some attention too as to which part of the image to focus on, but all LLMs are very good at this and it does not affect the final score.


### Results, insights, and conclusions
- For the task, I modified the prompt to make it easier for the LLM to get a reasonable score. But during this I was using google/gemini 3 flash preview. It seems to have fine-tuned the task to be easy for this particular model and so gemini 3 flash preview perform consistently well. 
- Also when I ran the task on a text only model, it guessed the right answer simply by guessing what the each image and the final task would be simply based on my prompt. So maybe the LLMs are not learning purely based on what they see in the images.



### Organizational affiliations
Working in a Japanese Automobile company, nothing crazy. 

### References & citations
https://oit.williams.edu/files/2010/02/using-images-effectively.pdf