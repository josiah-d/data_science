# Linear models case study

- [Linear models case study](#linear-models-case-study)
  - [Topic Choices](#topic-choices)
    - [Choice 1: Forecast HIV incidence in US counties](#choice-1-forecast-hiv-incidence-in-us-counties)
      - [Major challenges](#major-challenges)
    - [Choice 2: Predict the sale price of heavy equipment at auction](#choice-2-predict-the-sale-price-of-heavy-equipment-at-auction)
      - [Major challenges](#major-challenges-1)
  - [Deliverables](#deliverables)

## Topic Choices

Depending on your campus (check with your instructors), you and your group have 
two options for this case study.


### Choice 1: [Forecast HIV incidence in US counties](forecast_HIV_infections/README.md)

**Using data merged from several databases, you are asked to build a model that
predicts HIV incidence for US counties.**  You should also identify and report
the most significant drivers of HIV infection and how they vary between counties.

Read more [here](./forecast_HIV_infections/README.md).

#### Major challenges
1. Non-normal distribution of features, possibly requires thoughtful, domain knowledge based feature engineering, data preprocessing or feature tranformation
2. Require manual splitting of training data and test data.
3. Data comes from various sources, which requires careful reading to understand the exact meaning of the data.
4. Need to be aware of possible data leaking

### Choice 2: [Predict the sale price of heavy equipment at auction](predict_auction_price/README.md)

**Predict the sale price of a particular piece of heavy equipment at auction based
on its usage, equipment type, and configuration.**  The data is sourced from auction
result postings and includes information on usage and equipment configurations.

Read more [here](./predict_auction_price/README.md).

#### Major challenges
1. Need to learn to use script to evaluate results
2. Instruction information for completion is more than [Choice 1: Forecast HIV incidence in US counties](#choice-1-forecast-hiv-incidence-in-us-counties).
3. Lots of missing data in data set.
4. Need to be aware of possible data leaking

## Deliverables

At the end of the day your group will be expected to present for 5-10
minutes on your findings.  Present results from your README.md.

Cover the following in your presentation.

   1. Talk about what you planned to accomplish
   2. How you organized yourselves as a team (including your git workflow)
   3. Description of the problem and the data
   4. What you accomplished (how you chose model, performance metric, validation)
   5. Performance on unseen data
   5. Anything new you learned along the way
