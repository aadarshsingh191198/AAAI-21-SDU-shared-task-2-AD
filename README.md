# SDU - Acronym Disambiguation

This repository contains training & development sets, acronym dictionary, and the evaluation scripts for acronym disambiguation task at SDU@AAA-21

# Dataset

The dataset folder contains four files:

- **diction.json**: A dictionary of the acronyms and their possible meanings. All predictions should use this dictionary to expand the ambiguous acronyms in the text.
- **train.json**: The training samples for acronym identification task. Each sample has three attributes:
  - tokens: The list of words (tokens) of the sample
  - acronym: The index of the ambiguous short-form, i.e., acronym, in the tokens.
  - expansion: The correct meaning, i.e., expansion, of the acronym in the sample. These expansions are selected from `diction.json` dictionary. 
  - id: The unique ID of the sample
- **dev.json**: The development set for acronym disambiguation task. The samples in `dev.json` have the same attributes as the samples in `train.json`.
- **predictions.json**: A sample prediction file created from `dev.json` to test the scoring script. The participants should submit the final test predictions of their model in the same format as the `predictions.json` file. Each prediction should have two attributes:
  - id: The ID of the sample (i.e., the same IDs used in the train/dev/test samples provided in `train.json`, `dev.json` and `test.json`) 
  - prediction: The correct meaning, i.e., expansion, of the acronym in the sample. These expansions should be selected from `diction.json` dictionary. 
  
  
# Code
In order to familiarize the participants with this task, we provide a rule-based baseline in `code` directory. This baseline computes the frequency of the long forms in the `train.json` file. Afterwards, to make prediction for the input file (e.g., `dev.json` file), for each acronym, it selects the long form with the highest frequency as the final prediction. If there is a tie, the long form that appears the first among all tied long forms in the dictionary is selected as the final prediction. To run this baseline, run the following command:

`python code/most_frequent.py -input <path/to/input.json> -train <path/to/train.json> -diction <path/to/diction.json> -output <path/to/output.json`

Please replace `<path/to/input.json>`, `<path/to/train.json>`, `<path/to/diction.json>`, `<path/to/output.json` with the real paths to the input file (e.g., `dataset/dev.json`), train, dictionary and output json files. The output file contains the predictions for the input file and could be consumed by the scorer described in the next section to obtain the performance of this baseline. The official scores for this baseline are: *Precision: 89.03%, Recall: 44.94%, F1: 59.73%*

# Evaluation

To evaluate the predictions (in the format provided in `dataset/predictions.json` file), run the following command:

`python scorer.py -g path/to/gold.json -p path/to/predictions.json`

The `path/to/gold.json` and `path/to/predictions.json` should be replaced with the real paths to the gold file (e.g., `dataset/dev.json` for evaluation on development set) and predictions file (i.e., the predictions generated by your system in the same format as `dataset/predictions.json` file). The official evaluation metrics are the macro-averaged precision, recall and F1 for correct expansion predictions. For verbose evaluation (including the micro-averaged precision, recall and F1 and also the accuracy of the predictions), use the following command:

`python scorer.py -g path/to/gold.json -p path/to/predictions.json -v`

# Participation

In order to participate, please first fill out this form to register for the shared tasks: https://forms.gle/NvnT549mSbyeJQAPA. The team ID that is provided in this form will be used in the subsequent submissions and communications. The shared task is organized in two separate phases:
- *Developtment Phase*: In this phase, the participants will use the training/development sets provided in this repository to design and develop their models. 
- *Evaluation Phase*: Two weeks before the system runs due, i.e., 9th November 2020, the test set is released here. The test set has the same distribution and format as the development set. Run your model on the provided test set and save the prediction results in a Json file with the same format as the "predictions.json" file. Name the prediction file as "**output.json**" and send that to the email address sdu-aaai21@googlegroups.com with title "Results of AD-[TEAM-ID]-[RUN-ID]", where "[TEAM-ID]" should be replaced with ID of your team provided in the registration form and "[RUN-ID]" with a number between 1 to 10 to identify the model run. Each participant team is allowed to submit up to 10 different model runs. Note that you official score is reported for the model run with ID 1. In addition to the "output.json" file, please include the following information in your email:
    - Model Description: A brief summary of the model architecture. If your model is using word embedding, please specify what type of word embedding your model is using.
    - Extra Data: Whether or not the model employs other resources/data, e.g., acronym glossaries, in the development or evaluation phases.
    - Training/Evaluation Time: How long the model takes to be trained/evaluated on the provided dataset
    - Run Description: A brief description on what is the difference in the recent model run compared to other runs (if it is applicable)
    - Plan for System Report: If you have any plan to submit your system report or release your model publicly, please specify that.

For more information see [SDU@AAAI-21](https://sites.google.com/view/sdu-aaai21/home)
