# Enhancing-Fairness-and-Utility-in-Dynamic-Matching-Markets

The repo includes the code for the paper budgted_reinforcement_learning_for_fairness_in_real_time_dispatching_system. The code can be executed with the command:

```python
python train.py
```

At line 178 of python file train/train.py:  parameter 0 means experiment_using_fvr_as_fairness_definition; 1 means experiment_using_min_max_as_fairness_definition

/data/fairness.npy: fvr budget
/data/fairness_min_max: min_max budget

/data/utils include a download module to get file dis_CBD_twoPs_03_19.csv by http handler, if you failed because of network error, could download the csv file directly by below share link:
https://1drv.ms/u/s!AlDeipOkaENXazCoXrgWvD0uaX0?e=WA3imt