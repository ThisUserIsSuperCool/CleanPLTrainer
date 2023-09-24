# CleanPLTrainer

I am currently exploring a decent lightning trainer. The aim is to develop a powerful tool to aid my research: writing the least code with maximum flexibility.

Currently I am thinking and sharing about the rules and philosophy of the design. Based on the rules, I will explore how to use the powerful tools provided by lightning properly (I mean to avoid chaos). Short snapshot code may be availble.
The completed template will be released after I test the system on a completed project first.

For the previous version of Trainer, please see https://github.com/ThisUserIsSuperCool/dist_optuna_plus_wandb.

## Current Rules/Philosophy
1. There should be one -- and preferably only one -- obvious way to do it.
2. Always ensure clear boundaries among modules. Minimize their dependence.
3. Files always stay at correct place. Easy to find them when you need them.

## Overview
Catgorization of code:

**Lightning**: 

there are three main parts of lightning that we need to consider:
- data lightning module: 
- lightning module: 
- trainer: 