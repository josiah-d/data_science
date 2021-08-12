
## Bayesian A/B Testing 

While A/B testing with frequentist and Bayesian methods can be incredibly useful for determining the effectiveness of various changes to your products, better algorithms exist for making educated decision on-the-fly. Two such algorithms that typically out-perform A/B tests are extensions of the [Multi-armed bandit problem](http://stevehanov.ca/blog/index.php?id=132) which uses an _epsilon-greedy_ strategy. Using a combination of exploration and exploitation, this strategy updates the model with each successive test, leading to higher overall click-through rate. An improvement on this algorithm uses an _epsilon-first_ strategy called [UCB1](http://www.chrisstucchio.com/blog/2012/bandit_algorithms_vs_ab.html). Both can be used in lieu of traditional A/B testing to optimize products and click-through rates.

## References

* [Bayesian Statistics in One Hour](https://datajobs.com/data-science-repo/Bayesian-Statistics-[Patrick-Lam].pdf)
* [Conjugate Models](http://patricklam.org/teaching/conjugacy_print.pdf)
* [Introduction to Bayesian Statistics](http://patricklam.org/teaching/bayesian_print.pdf)
* [Patrick Lam's Website](http://patricklam.org/)
* [Introduction to MCMC for Machine Learning](http://www.cs.princeton.edu/courses/archive/spr06/cos598C/papers/AndrieuFreitasDoucetJordan2003.pdf)
* [Conjugate Prior Diagrams](http://www.johndcook.com/conjugate_prior_diagram.html)
* [A Short Intro to Bayesian Statistics](http://aleph0.clarku.edu/~djoyce/ma218/bayes2.pdf)
* [Conjugate Priors](http://stats.stackexchange.com/questions/58564/help-me-understand-bayesian-prior-and-posterior-distributions)
* [Philosophy and the practice of Bayesian statistics](http://www.stat.columbia.edu/~gelman/research/published/philosophy.pdf)
* [Statistical Formulas for Programmers](http://www.evanmiller.org/statistical-formulas-for-programmers.html)
* [A Primer on A/B Testing](http://alistapart.com/article/a-primer-on-a-b-testing)

### Academia

* [Finite-Time Analysis of the Mulitarmed Bandit problem](http://homes.di.unimi.it/~cesabian/Pubblicazioni/ml-02.pdf)
* [Multiarmed Bandit Algorithms and Empirical Evaluation](http://www.cs.nyu.edu/~mohri/pub/bandit.pdf)
