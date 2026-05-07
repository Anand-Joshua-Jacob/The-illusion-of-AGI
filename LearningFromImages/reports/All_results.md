## Claude Opus 4.6
Number of trials passed out of 5 and Total runtime  
- {'task1_1': 5, 'task1_2': 5, 'task1_3': 5, 'task1_4': 5, 'task1_5': 5} | Runtime: 11m 56s  
- {'task2_1': 4, 'task2_2': 4, 'task2_3': 5, 'task2_4': 4, 'task2_5': 4} | Runtime: 11m 21s  
- {'task3_1': 5, 'task3_2': 5, 'task3_3': 5, 'task3_4': 4, 'task3_5': 4} | Runtime: 12m 23s

### Observations: 
- In Task 1, the model consistently learns and applies the conventions correctly, using the scale as a reference.
- Sometimes the model comes up with approximate units for movement in each of the images in task 2 suggesting ability to create internal world representations.
- The drop in later Task 3 subtasks (3_4, 3_5) may indicate difficulty in generalizing across orientation changes with limited examples, rather than in basic instruction following.


## Claude Sonnet 4.6
Number of trials passed out of 5 and Total runtime
- {'task1_1': 3, 'task1_2': 2, 'task1_3': 4, 'task1_4': 3, 'task1_5': 4} | Runtime: 14m 34s
- {'task2_1': 2, 'task2_2': 3, 'task2_3': 5, 'task2_4': 3, 'task2_5': 5} | Runtime: 11m 46s
- {'task3_1': 4, 'task3_2': 5, 'task3_3': 5, 'task3_4': 4, 'task3_5': 3} | Runtime: 11m 28s

### Observations:
- The model often produces “near‑miss” answers where the action set is correct but the order is wrong (e.g., “move right and jump” vs. “jump and move right”). This suggests that the model was able to learn the conventions about the movement properly but failed to reason that moving right first would result in hitting the red block immediately.


## Claude Haiku 4.5
Number of trials passed out of 5 and Total runtime
- {'task1_1': 0, 'task1_2': 0, 'task1_3': 0, 'task1_4': 0, 'task1_5': 0} | Runtime: 4m 56s
- {'task2_1': 0, 'task2_2': 0, 'task2_3': 1, 'task2_4': 0, 'task2_5': 0} | Runtime: 4m 47s
- {'task3_1': 0, 'task3_2': 0, 'task3_3': 1, 'task3_4': 0, 'task3_5': 0} | Runtime: 4m 51s

### Observations:
- Performance is very low across all tasks.
- In the few successful cases, the final answer is correct but the intermediate reasoning is inconsistent with the visual setup and the required steps.

## GPT 5.4
Number of trials passed out of 5 and Total runtime
- {'task1_1': 0, 'task1_2': 0, 'task1_3': 0, 'task1_4': 2, 'task1_5': 3} | Runtime: 3m 0s
- {'task2_1': 0, 'task2_2': 1, 'task2_3': 0, 'task2_4': 1, 'task2_5': 0} | Runtime: 3m 6s
- {'task3_1': 4, 'task3_2': 1, 'task3_3': 2, 'task3_4': 3, 'task3_5': 2} | Runtime: 2m 30s

### Observations: 
- Compared to Anthropic and Google models, GPT 5.4 responses use smaller reasoning fields and have shorter runtimes. Hypothesis: this reduced deliberation may be contributing to the lower accuracy.
- The explanations look very similar across different tasks, yet performance is noticeably better on Task 3 than on Tasks 1 and 2. This suggests that the model may be relying on a generic template rather than deeply adapting its reasoning to each variant.
- The model appears to have a tendency to start answer sequences with the letter “A”. In Task 3, where “A” happens to be the correct first action, this response bias may partially explain the higher success rate.

## GPT 5.4 mini
Number of trials passed out of 5 and Total runtime
- {'task1_1': 0, 'task1_2': 0, 'task1_3': 0, 'task1_4': 0, 'task1_5': 0} | Runtime: 2m 36s
- {'task2_1': 0, 'task2_2': 0, 'task2_3': 0, 'task2_4': 0, 'task2_5': 0} | Runtime: 1m 59s
- {'task3_1': 0, 'task3_2': 0, 'task3_3': 0, 'task3_4': 0, 'task3_5': 0} | Runtime: 2m 9s

### Observations: 
- Many responses are rejected because the model does not follow the required output format (a sequence containing only capital English letters), which directly lowers the measured pass rate.
- Even in format‑compliant responses, the reasoning often diverges significantly from the visual setup or from a logically correct sequence, indicating weak grounding in the task.


## GPT 5.4 nano
Number of trials passed out of 5 and Total runtime
- {'task1_1': 0, 'task1_2': 1, 'task1_3': 1, 'task1_4': 0, 'task1_5': 0} | Runtime: 2m 20s
- {'task2_1': 0, 'task2_2': 0, 'task2_3': 0, 'task2_4': 0, 'task2_5': 1} | Runtime: 2m 9s
- {'task3_1': 0, 'task3_2': 0, 'task3_3': 1, 'task3_4': 0, 'task3_5': 0} | Runtime: 2m 14s

### Observations:
- Overall accuracy is low.
- Similar to Claude Haiku, this model can sometimes guess the correct sequence while providing reasoning that does not actually justify that sequence.


## Gemini 3.1 pro preview
Number of trials passed out of 5 and Total runtime
- {'task1_1': 5, 'task1_2': 5, 'task1_3': 5, 'task1_4': 5, 'task1_5': 2} | Runtime: 23m 56s
- {'task2_1': 1, 'task2_2': 5, 'task2_3': 4, 'task2_4': 3, 'task2_5': 4} | Runtime: 15m 6s
- {'task3_1': 4, 'task3_2': 4, 'task3_3': 5, 'task3_4': 4, 'task3_5': 5} | Runtime: 22m 17s

### Observations:
- Even though Google 3.1 pro and 3 flash have the longest runtimes, their reasoning field in the response is relatively short and clean suggesting substantial internal reasoning before generating a concise explanation. 
- Even when the model fails, it's proposed sequences came close to the right answer in most of the cases suggesting that the model was able to learn the conventions from the images but not reason out the final sequence properly.


## Gemini 3 flash preview 
Number of trials passed out of 5 and Total runtime
- {'task1_1': 5, 'task1_2': 4, 'task1_3': 4, 'task1_4': 5, 'task1_5': 5} | Runtime: 34m 40s
- {'task2_1': 4, 'task2_2': 4, 'task2_3': 3, 'task2_4': 4, 'task2_5': 4} | Runtime: 38m 33s
- {'task3_1': 5, 'task3_2': 5, 'task3_3': 4, 'task3_4': 5, 'task3_5': 5} | Runtime: 23m 54s

### Observations:
- Since the model usually uses the scale as a reference in it's reasoning, removing the explicit scale from the images reduces the accuracy.


## Gemini 2.5 flash
Number of trials passed out of 5 and Total runtime
- {'task1_1': 5, 'task1_2': 4, 'task1_3': 2, 'task1_4': 1, 'task1_5': 0} | Runtime: 29m 33s
- {'task2_1': 3, 'task2_2': 1, 'task2_3': 1, 'task2_4': 1, 'task2_5': 0} | Runtime: 24m 41s
- {'task3_1': 4, 'task3_2': 5, 'task3_3': 2, 'task3_4': 4, 'task3_5': 4} | Runtime: 18m 21s

### Observations:
- Few shot learning tasks seem difficult for this model (since task 1_4, 1_5, 2_4, 2_5, 3_4, 3_5 perform worse).
- Performs well in task 3 with solid reasoning behind the correct answers.