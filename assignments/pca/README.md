# Principal Component Analysis

## Intro
High-dimensional data comes with challenges. Here's some examples of high-dimensional data.

#### Example high-dimensional datasets:
* Rideshare customers: **15 features**!
* Online shopping customers: each feature is the number of times the customer has purchased an item in the store. **Thousands, maybe hundreds of thousands of features.**
* Heartrate of patients: each sample is a time series of the patient's heartrate. If the frequency of the time series is 1 second, a time series for 24 hours would have **86400 features**.
* A dataset of full-color 28-by-28 images: 3 colors × 28 wide × 28 high = **2352 features** per image.
* A dataset of full-color videos 30 fps, 5 minutes long, 1000-by-1000 frames: 30 frames/second × 5 minutes × 60 seconds/minute × 3 colors × 1000 wide × 1000 high = **27,000,000,000 features** per video.

#### Some challenges of high-dimensional data:
* The Curse of Dimensionality: Even your nearest neighbors are very far
* Visualization: Anything beyond 3 is tricky

#### Interesting opportunities of high-dimensional data
* Transformed feature space: Latent features, linear separation

In this sprint we will talk about ways to address both scenarios and techniques to make our analyses much more tractable.
