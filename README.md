# The-illusion-of-AGI
Experiments to test the limits of state-of-the-art AI systems



## Learning
> Can LLMs learn from experience. Can they have a working memory or understand that their actions have consequences. I wanted to find out!

1) [Cognitive Maps in Rats and Men (1948)](https://personal.utdallas.edu/~tres/spatial/tolman.pdf), published in Psychological Review, discusses how rats form cognitive maps of mazes after exploring them a few times. It shows that among other things rats can learn the layout of a map by exploring it. 
I was wondering whether SOTA AI systems could also learn from exploring mazes. Turns out, this was already researched in a paper titled [MazeEval: A Benchmark for Testing Sequential Decision-Making in Language Models (2025)](https://arxiv.org/abs/2507.20395). This paper shows that LLMs fail for large mazes and that performance significantly degrades when the language used is changed to Icelandic. It suggests that spatial reasoning in LLMs emerges from linguistic patterns rather than language-agnostic mechanisms. 

2. My next thought was to explore whether AI systems could go through a simulated environment and reach a particular goal when they have a set of moves to choose from at each stage. A shift from static benchmarks to interactive reasoning environments. This has already been done by [ARC-AGI-3](https://arcprize.org/arc-agi/3), they have given a benchmark (a set of tasks) that almost impossible for AI systems but feasible for humans.