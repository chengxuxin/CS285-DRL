### Experiment 1 (CartPole)

```bash
python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 1000 \
-dsa --exp_name q1_sb_no_rtg_dsa

python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 1000 \
-rtg -dsa --exp_name q1_sb_rtg_dsa

python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 1000 \
-rtg --exp_name q1_sb_rtg_na

python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 5000 \
-dsa --exp_name q1_lb_no_rtg_dsa

python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 5000 \
-rtg -dsa --exp_name q1_lb_rtg_dsa

python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 5000 \
-rtg --exp_name q1_lb_rtg_na
```



### Experiment 2 (InvertedPendulum)

```bash
python cs285/scripts/run_hw2.py --env_name InvertedPendulum-v2 \
--ep_len 1000 --discount 0.9 -n 100 -l 2 -s 64 -b 500 -lr 0.01 -rtg \
--exp_name q2_b30000_r0.01
```



### Experiment 3 (LunarLander)

```bash
python cs285/scripts/run_hw2.py \
--env_name LunarLanderContinuous-v2 --ep_len 1000
--discount 0.99 -n 100 -l 2 -s 64 -b 40000 -lr 0.005 \
--reward_to_go --nn_baseline --exp_name q3_b40000_r0.005
```



### Experiment 4 (HalfCheetah)

substitute \<b> with [10000, 30000, 50000], \<r> with [0.005, 0.01, 0.02].

```bash
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
--discount 0.95 -n 100 -l 2 -s 32 -b <b> -lr <r> -rtg --nn_baseline \
--exp_name q4_search_b<b>_lr<r>_rtg_nnbaseline
```



```bash
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
--discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 \
--exp_name q4_b30000_r0.02

python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
--discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 -rtg \
--exp_name q4_b30000_r0.02_rtg

python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
--discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 --nn_baseline \
--exp_name q4_b30000_r0.02_nnbaseline

python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
--discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 -rtg --nn_baseline \
--exp_name q4_b30000_r0.02_rtg_nnbaseline
```



### Bonus (GAE)

```bash
python cs285/scripts/run_hw2.py --env_name Walker2d-v2 --ep_len 1000 \
--discount 0.99 -n 100 -l 2 -s 64 -b 10000 -lr 0.005 --nn_baseline --gae \
--exp_name bonus_b10000_lr0.005_gae_normalize_adv
```

```bash
python cs285/scripts/run_hw2.py --env_name Walker2d-v2 --ep_len 1000 \
--discount 0.99 -n 100 -l 2 -s 64 -b 10000 -lr 0.005 --nn_baseline -rtg \
--exp_name bonus_b10000_lr0.005_no_gae
```



### Bonus (Multi-step PG)

```bash
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
--discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 -rtg --nn_baseline \
--exp_name bonus_b30000_r0.02_rtg_nnbaseline_update_per_iter4 --num_agent_train_steps_per_iter 4
```



See ```plot.ipynb``` for code for plotting results.