# vencover

# Executive summary:

# Car Insurance is the more important/applicable problem, so I thought about that one first.

- My only real insight beyond chatGPT is the [bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html).  Where chatGPT implements a polynomial calculate_premium and categorical determine_policy_eligibility, I start with the idea that "premiums must cover payouts".
- If we have or can build a table of claims, with all existing columns + a column "claim cost", then we can train a NN to predict the chance and cost of a claim given all columns.  
- The (expected cost) of any given policy is integral[f(cost*chance)]*dt, and we can set a policy's premium to be (expected cost * margin-of-error) / (expected lifetime), where margin-of-error is calculated from the loss of the NN and expected lifetime is the upper bound of dT.
- At worst this can be benchmarked against any polynomial solution's accuracy, and at best replaces any debates e.g. "well EV's catch fire, but not always, but .. but.." 

Very interested in your thoughts here.

# Drone Simulation was the less interesting problem until last night's tragedy.  

- I was much more impressed with chatGPT's zero-shot solution, and ended up developing a simulator/visualizer entirely as a manager of chatGPT.
- See below for the simulation_report.csv and frame where a collision occurs generated via matplotlib.
- For this problem I'm more interested in your devtools--assuming I have your expected output

```
time,collision
3,"([458.6666666666667, 658.6666666666666, 129.33333333333334], [349.5537985160413, 549.5537985160413, 106.51793283868044])"
```

![Figure_1](https://github.com/user-attachments/assets/cbef3568-cc00-41d7-b895-3ece4df7431c)
