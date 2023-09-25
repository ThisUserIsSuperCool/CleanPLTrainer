# CleanPLTrainer

I am currently exploring a decent lightning trainer. The aim is to develop a powerful tool to aid my research: writing the least code with maximum flexibility.

Currently I am thinking and sharing about the rules and philosophy of the design of my own trainer. Based on the rules, I will explore how to use the powerful tools provided by lightning properly (I mean to avoid chaos).

Short snapshots of code may be availble. The completed template will be released after I test the system on a completed project first.

For the previous version of Trainer, please see https://github.com/ThisUserIsSuperCool/dist_optuna_plus_wandb.

## Current Rules/Philosophy
1. There should be one -- and preferably only one -- obvious way to do it.
2. Always ensure clear boundaries among modules. Minimize their dependence.
3. Files/codes/modules always stay at correct place. Easy to find them when you need them.

In details, to ensure greatest flexibility, we should give up some auto operations supported by lightning, currently for me they are:
1. manually control backward() for loss, and step() for opt and sch.
2. manually control computation of metrics if torchmetrics is used. That is to say, pass values to self.log(), rather than the whole object. In addition, spend a few more seconds to think about if there is any reset operation needed.

## Overview

**Lightning**: 

There are three main parts of lightning that we need to consider:
- data lightning module: prepare dataset, dataloader, statistical data...
- lightning module: optimization, model, evaluation...
- trainer: training settings (devices, log frequency...)... (passing args is all you need)

**My Trainer**:

For my trainer, I categorize the code to three kinds to ensure strict and clear hierachy:
- Basic code: code about the structure. Provide fundimental code for easy-to-use trainer.
- Task-specific code: task-specific evaluations and metrics.
- Method-specific code: losses, models.