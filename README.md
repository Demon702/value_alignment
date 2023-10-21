# value_alignment
A large scale dataset for multi cultural value alignment based upon World Values Survey

value_alignment

- question_metadata.json
    - Contains mapping from question_id to question text
- question_metadata_detailed.json
    - Contains mapping from question_id to question text and some extra metadata about the question
- value_alignment_full_dataset
    - full_data
        - participant_demographics.tsv
            - Contains participants’ demographics with D_INTERVIEW as the unique participant identifier. 93278 participants x 46 columns
        - participant_qa.tsv
            - Contains participants' answer to different questions with D_INTERVIEW as the unique participant identifier. 93278 participants x 240 columns
    - train
        - Same as before but with 70% participants
    - dev
        - Same as above but with 15% participants
    - test
        - Same as above but with 15% participants
- value_alignment_probe_dataset
    - participant_demographics.tsv
        - Contains 12 most important demographic information with D_INTERVIEW as the unique participant identifier. 13991 participants x 12 columns
    - probe_dataset.tsv
        - Contains 12145 (participant, question) pairs sampled from the dev split. Overall there are 32 hard questions(with the most variance in user reponses). For each question, we sample roughly 225 users stratified across continent, sex and religion.