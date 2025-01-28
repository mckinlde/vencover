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



# -----

Company insures 10 people

premiums must cover payouts

payouts are a f(cost of claim, # of claims)

premiums can be weighted so riskier driver/car combinations pay more, to discount safer combos
- if premium weighting was perfect, then every driver would pay their full expected cost


num of claims is integral(chance of claim, time)
- chance of claim can be weighted by columns
- cost of claim can be weighted by columns

the bitter lesson - scaled compute is more powerful than human insight

If we have a dataset "claims" that includes the props at time of a claim, then we can use it to train a NN to predict the cost of a claim for a given propset

We can also train a NN to predict the likelyhood of claim for a given propset

Then the expected cost of a driver is integral[f(cost*chance)]*dt


# -----

With above notes, I've decided to create some fake data in a 'claims' table and use it to train NN's.

Before doing that, I used the instructions to prompt chatGPT for a zero-shot solution; chatGPT came up with the same kind of math/human-insight approach that I convinced myself misses 'the bitter lesson' above.

Cest la vie, time to train a model.


# -----

First I generate a table of fake claims; it's just the normal customer data, plus these 3 cols:

claim-cost: cost of claim in $; range 0-1mil
claim-date: date that claim occurred
policy-age: age of policy when claim occurred

I'm imagining rows in this table as discrete moments in time, and I want to be able to predict their values based on props of a prospective customer.

# -----

My week is getting pretty busy, here's the link for 'the bitter lesson' just in case you haven't seen it: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
