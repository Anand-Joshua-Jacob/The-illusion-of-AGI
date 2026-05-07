

- Sometimes the model reason right and learn the conventions but are not able to form the concept of a stickman moving properly. They are able to understand that say this image represent a stickman moving upwards even without the arrows or labels. But they are unable to reason the correct combination of moves to achieve the target.
- The google models take a lot of time to run (around 30 min) but the other models are much faster. Maybe this has something to do with the way google
processes images?
- Models that did not perform well also did not think for a lot of time. Maybe if they reason for more time they might perform better?

- Deepseek v3.2 - reasoning:"Since no images were provided, I will assume a generic case. Typically in stickman puzzle games, actions are: A = jump, B = crouch/duck, C = move sideways. The GOAL says 'avoid red', implying the stickman must not touch red obstacles. Without seeing the images, the shortest safe sequence to avoid red might involve jumping over a low obstacle (A) and then moving sideways to avoid a subsequent threat (C). Assuming one jump is enough, sequence 'AC' could work. But to match a common minimal pattern for 'avoid red' with two actions, I'll propose 'AC'. If the environment requires only a single action, like just jumping, then 'A' would be shortest, but 'avoid red' often implies multiple hazards. Since the instructions ask for the shortest sequence given the GOAL image, and the image isn't shown, I'll assume a plausible minimal sequence based on typical puzzles: 'AC' (jump, then move sideways)."
sequence:"AC"


- Maybe the task was too simple, Wonder what would happen if it were a bit complicated.
- Wonder how the models would perform if all of them had equal amounts of reasoning tokens (add something like "reason using about 500 tokens").
- Finetuned the prompt for Google Gemini 3 flash preview model. How can I get a general prompt that is not finetuned to any model.
- Claude Opus still performed surprisingly good.

- Task 2 shows that removing the explicit scale in the image does diminish the model's ability to understand.
- Task 3 shows that learning conventions from the "up" image and applying them to horizontal movement is harder for the LLMs (since task 3_4, 3_5 results are worse かな)

