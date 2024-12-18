# Consistency_Quantised_Constraints
CS 5891 Special Topics - Algorithms for Decision-Making Final Project

## About Me

#### Young-jae Moon
* M.Sc. in computer science and Engineering Graduate Fellowship recipient at Vanderbilt University.
* Incoming Online Master in computer science student at Georgia Tech.
* Email: youngjae.moon@Vanderbilt.Edu

Note: Weizhe Jiao was part of our team, but he decided to leave this project (he was busy with other courses).

## Course Instructor

#### Professor Ayan Mukhopadhyay
* Assistant Professor in the Computer Science at Vanderbilt University
* Email: ayan.mukhopadhyay@vanderbilt.edu

## Project Overview
This project explores the trade-offs between efficiency and performance in decision-making systems by quantising neural network policies and verifying their consistency with unquantised models. Using the CartPole environment in Gymnasium, the project evaluates both Post-Training Quantisation (PTQ) and Quantisation-Aware Training (QAT), comparing their impact on decision accuracy, inference speed, and robustness.

Additionally, the project implements Interval Neural Networks (INNs) to investigate that the quantised networks remain consistent with the original models, ensuring reliability in decision-making under quantised constraints.

## Key Features
- Reinforcement Learning:
  - Train a neural network policy using an reinforcement learning algorithm in the CartPole environment.
- Quantisation Techniques:
  - Apply and compare PTQ and QAT for model optimisation.
- Verification with Interval Neural Networks (INNs):
  - Use INNs to verify decision consistency between unquantised and quantised models.
- Performance Metrics:
  - Measure total rewards, inference speed, and memory usage for quantised and unquantised models.
- Robustness Testing:
  - Test the consistency of decisions under quantisation-induced errors and adversarial inputs.


## Tools and Technologies

1. Python
2. PyTorch
3. Gymnasium

## Installation Instructions

Clone the repository and install dependencies:
```
git clone https://github.com/Pingumaniac/Consistency_Quantised_Constraints.git
cd Consistency_Quantised_Constraints
pip3 install -r requirements.txt
```

## Instructions to execute the software

1. Train the Policy: Train a neural network policy for the CartPole environment:
```
python3 train_policy.py
```

2. Apply Quantisation: Apply PTQ or QAT to the trained model:
```
python3 apply_quantisation.py
```

3. Evaluate Models: Compare the performance of baseline, PTQ, and QAT models:
```
python3 evaluate_models.py
```

4. Verify Consistency: Verify the consistency between quantised and unquantised models using INNs:
```
python3 verify_consistency.py
```

## Project structure
```
Consistency_Quantised_Constraints/
├── src/                      # Source code directory
│   ├── models.py             # Contains the PolicyNetwork class definition
│   ├── policy_model.py       # Contains the PolicyNetwork class definition and utilities for baseline model
│   ├── train_policy.py       # Script to train the baseline policy
│   ├── apply_quantisation.py # Script to apply PTQ and QAT
│   ├── verify_consistency.py # Script to verify consistency using INNs
│   ├── evaluate_models.py    # Script to evaluate and compare models
│   └── interval_nn.py        # Implementation of the interval neural network functionality
│   └── models/                   # Directory for storing models
│       ├── policy.pth            # Saved baseline trained policy
│       └──  ptq_policy.pth        # Saved sed PTQ policy
├── doc/                      # Documentation directory
│   └── final_presentation.pdf # Final presentation slides
├── requirements.txt          # List of required dependencies
└── README.md                 # Project documentation

```


## Bug tracking

* All users can view and report a bug in "GitHub Issues" of our repository.
* Please include: a clear description of the issue, steps to reproduce the issue, and environment details (e.g., Python version, OS).
