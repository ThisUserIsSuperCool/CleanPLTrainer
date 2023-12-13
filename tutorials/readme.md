# My Trainer

For my trainer, I categorize the code to three kinds to ensure strict and clear hierachy:
- Basic code: code about the structure. Provide fundimental code for easy-to-use trainer.
- Task-specific code: task-specific evaluations and metrics.
- Method-specific code: losses, models.

```python
class BasePLmodule(pl.LightningModule):
	# structure, general methods, properties
	...
class TaskPLmodule(BasePLmodule):
	# evaluation and metrics
	...
class MethodPLmodule(TaskPLmodule):
	# model structure and optimization
	...

method_task_plm = MethodPLmodule(cfg)
```
File Orgnization:
```
├── CleanPLTrainer.code-workspace
├── core
│   ├── hooks
│   ├── PLBase
│   │   ├── Base_plm.py
│   │   ├── base_util.py
│   │   └── todos.py
│   └── module # research-related
│   └── util # engineering-related
├── proj
│   ├── Method_plm.py
│   └── Task_plm.py
```
### Init a plm: plm = Methodplm + Taskplm

You are suggested to write several `TaskPLmodule` and several `MethodPLmodule`. Thus, say you want to choose to run Method B for Task A, you could:
```python
tA_mB_obj = task_method_class(
			task=taskA,
			method=methodB,
		)(param_to_pass)
```

## 1 Modules
### 1 LossDataPackDict
Use `LossDataPackDict` to store your losses.
```python
loss_data_pack = LossDataPackDict() # loss = 0
loss_data_pack.update(loss_1 = loss_1) # loss += loss1
loss_data_pack.update(loss_2 = loss_2) # loss += loss2

# get the loss and backprob
loss = loss_data_pack.loss_dict['loss']
loss.backward()

# loss1 = loss_data_pack.loss_dict['loss1']
# loss2 = loss_data_pack.loss_dict['loss2']
```
The losses you saved to `LossDataPackDict` will be automatically logged to pytorch-lightning loggers.

## 2 Sweep
We consider the following Three sweeping senoarios:
1. run a trial several times with different seed.
2. perform grid search over several hyper-params manually.
3. perform auto hyper-params search using advanced tools like Optuna.
