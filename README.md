# The-illusion-of-AGI
- Experiments to test the limits of state-of-the-art AI systems
- I think current AI systems can be trained to learn something, to know what area is knows and what it does not but to do them in-context is where they fail.
- So how does this affect us? We can always train a model to be good at a certain task and use it for that particular task.
- Where does this AI's lack of understanding affect us. Can all problems be solved by just big data analysis? 


## Learning
> Can LLMs learn from experience. Can they have a working memory or understand that their actions have consequences. I wanted to find out!

1) [Cognitive Maps in Rats and Men (1948)](https://personal.utdallas.edu/~tres/spatial/tolman.pdf), published in Psychological Review, discusses how rats form cognitive maps of mazes after exploring them a few times. It shows that among other things rats can learn the layout of a map by exploring it. 
I was wondering whether SOTA AI systems could also learn from exploring mazes. Turns out, this was already researched in a paper titled [MazeEval: A Benchmark for Testing Sequential Decision-Making in Language Models (2025)](https://arxiv.org/abs/2507.20395). This paper shows that LLMs fail for large mazes and that performance significantly degrades when the language used is changed to Icelandic. It suggests that spatial reasoning in LLMs emerges from linguistic patterns rather than language-agnostic mechanisms. 

2. My next thought was to explore whether AI systems could go through a simulated environment and reach a particular goal when they have a set of moves to choose from at each stage. A shift from static benchmarks to interactive reasoning environments. This has already been done by [ARC-AGI-3](https://arcprize.org/arc-agi/3), they have given a benchmark (a set of tasks) that almost impossible for AI systems but feasible for humans.


## Metacognition - thinking about thinking
Confidence calibration done during testing itseems - [Reasoning models get higher scores.](https://arxiv.org/abs/2505.14489)
1. So how about putting the bullshit benchmark questions and testing whether the AI agrees, if it does, how much is it's confidence score.
2. How about adding the prompt like - "Answer only if you are 100 percent sure" or "Make sure what you are saying makes sense" and then evaluating the system.
