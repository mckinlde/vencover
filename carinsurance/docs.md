Instructions:

* Car Insurance Underwriting Model assignment for technical candidates

** Objective: Develop a simple underwriting model for car insurance that determines whether the customer should get a policy, and if so, the premium amount given their rish profile.  The model can be built using either a spreadsheet, in python, or whatever language you prefer.

** Background: Underwriting in car insurance involves assessing the risk associated with insuring a driver and their vehicle.  Factors that typically affect car insurance premiums include the driver's age, credit score, job title, driving history, type of vehicle, location, vehicle telematics, and other relevant variables.  This assignment will require you to develop a model that calculates the insurance premium for different customers based on these factors.

** Data Inputs: sample data is showin in the tab "data inputs" for 500 potential customers.  Please feel free to add columns with other factors you feel would help to model the risk.

** Model Logic: The model should compute a base premium and adjust it based on risk factors:

- Base Premium: A starting premium amount before adjustments.
- Adjustments: Increase or decrease the premium based on each input variable.  For example:
    - Higher premiums for younger drivers or those with less driving experience.
    - Discounts for drivers with a clean driving history.
    - Higher premiums for high-risk vehicle types (e.g., sports cars).
    - Location-based adjustments (e.g., urban areas may have higher rates due to higher traffix risk).

Define the logic and formulas for how each factor affects the premium.

** Evaluation Criteria

- Clarity: Clear documentation and explanation of the logic and assumptions behind the model.
- Code/Spreadsheet Quality: Formatting, use of formulas, functions, or Python code with appropriate comments.
- Creativity: Consideration of additional factors, assumptions, or potential improvements.
- Whiteboarding, presentation, Q&A: after assignment completed



-----

Company insures 10 people

premiums must cover payouts

payouts are a f(cost of claim, # of claims)

premiums can be weighted so riskier driver/car combinations pay more, to discount safer combos
- if premium weighting was perfect, then every driver would pay their full expected cost


num of claims is integral(chance of claim, time)

chance of claim can be weighted by columns

cost of claim can be weighted by columns

the bitter lesson - scaled compute is more powerful than human insight

miles -1> wrecks -2> fires

First arrow is based on the driver, second is weighted on the car

If we have a dataset "claims" that includes the props at time of a claim, then we can use it to train a NN to predict the cost of a claim for a given propset

We can also train a NN to predict the likelyhood of claim for a given propset

And weight premium as f(cost*chance)
