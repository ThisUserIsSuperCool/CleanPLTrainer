"""
Simple example of how to use optuna to optimize hyperparameters for a multiseed experiment.

Since the cfg is controlled by hydra, we need to **change the seed** and **output dir** for each trial.

Expected directory structure:
- output_dir
    - param_set_0
        - seed_0
        - seed_1
    - param_set_1
        - seed_0
        - seed_1

This file cal
"""
def single_run(cfg):
    seed_everything(cfg.seed)

    data_plm = init_data(cfg)
    plm = init_plm(cfg, data_plm)
    trainer = init_trainer(cfg, plm, data_plm)

    trainer.fit(plm, data_plm)
    result = trainer.callback_metrics[cfg.monitor]
    return result

from hydra.core.utils import configure_log
def change_log_pth(cfg,new_pth):
    """
    change the log path for each trial
    """
    cfg_hydra_log_dict = OmegaConf.to_container(cfg.hydra_log)
    cfg_hydra_log_dict['handlers']['file']['filename'] = os.path.join(new_pth,'run.log')
    cfg_hydra_log = OmegaConf.create(cfg_hydra_log_dict)
    configure_log(cfg_hydra_log, False)

@hydra.main(**_HYDRA_PARAMS)
def main(cfg: DictConfig) -> None:
    results = []
    for seed in range(cfg.seed_list):
        cur_output_dir = os.path.join(cfg.base_dir, f"seed_{cfg.seedl}")
        cfg.seed = seed
        cfg.output_dir = cur_output_dir
        create_dir(cur_output_dir)
        change_log_pth(cfg,cur_output_dir) # change the log path for each trial
        
        result = single_run(cfg)
        results.append(result)
    
    change_log_pth(cfg,cfg.base_dir) # change the log path back to the base dir for main process
    mean_result = np.mean(results)
    logger.info(f"Mean result: {mean_result}")
    return mean_result

if __name__ == "__main__":
    main()




