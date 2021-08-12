# Maximum Likelihood Estimation Examples
### Bernoulli Distribution - Maximum Likelihood Estimate of *p*  
$$\begin{aligned}
P(X = x | x \in \{0, 1\} &= p^x (1-p)^{1-x} \\\\
L(p|x_1, x_2, x_3, ... , x_n) &= \left(p^{x_1} (1-p)^{1-x_1}\right) \left(p^{x_2} (1-p)^{1-x_2}\right) \left(p^{x_3} (1-p)^{1-x_3}\right) \cdots \left(p^{x_n} (1-p)^{1-x_n}\right) \\\\
&=\prod_{i=1}^n p^{x_i} (1-p)^{1-x_i} \\\\
&= p^{\sum_{i=1}^n x_i} (1-p)^{\sum_{i=1}^n 1-x_i} \\\\
&= p^{\sum_{i=1}^n x_i} (1-p)^{n - \sum_{i=1}^n x_i} \\\\
\ell(p | x_1, x_2, x_3, ... , x_n) &= \sum_{i=1}^n x_i \ln(p) + \left(n - \sum_{i=1}^n x_i\right)\ln(1 - p) \\\\
\frac{d\ell}{dp} &= \frac{\sum_{i=1}^n x_i}{p} - \frac{n - \sum_{i=1}^n x_i}{1 - p}
    \end{aligned}$$
Set the derivative equal to 0.
$$\begin{aligned}
\frac{\sum_{i=1}^n x_i}{p} - \frac{n - \sum_{i=1}^n x_i}{1 - p} &= 0 \\\\
\frac{\sum_{i=1}^n x_i}{p} &= \frac{n - \sum_{i=1}^n x_i}{1 - p} \\\\
\sum_{i=1}^n x_i - p \sum_{i=1}^n x_i &= np - p \sum_{i=1}^n x_i \\\\
\sum_{i=1}^n x_i &= np \\\\
p &= \frac{\sum_{i=1}^n x_i}{n} \\\\
\hat{p}_{MLE} &= \bar{x}
\end{aligned}$$
The maximum likelihood estimator of *p* is the sample mean.
​
​
### Poisson Distribution - Maximum Likelihood Estimate of $\lambda$  
$$\begin{aligned}
P(X = x | x \in N_0 \equiv \{0, 1, 2, 3, ...\}) &= \frac{\lambda^x e^{-\lambda}}{x!}\\\\
L(\lambda | x_1, x_2, x_3, ..., x_n) &= \left(\frac{\lambda^{x_1} e^{-\lambda}}{x_1!}\right) \left(\frac{\lambda^{x_2} e^{-\lambda}}{x_2!}\right) \left(\frac{\lambda^{x_3} e^{-\lambda}}{x_3!}\right) \cdots \left(\frac{\lambda^{x_n} e^{-\lambda}}{x_n!}\right)\\\\
&= \frac{\lambda^{\sum_{i=1}^n x_i} e^{-\lambda}}{\prod_{i=1}^n x_i!}\\\\
\ell(\lambda | x_1, x_2, x_3, ..., x_n) &= \sum_{i=1}^n x_i \ln(\lambda) - n \lambda - \ln\left(\prod_{i=1}^n x_i!\right)\\\\
&= \sum_{i=1}^n x_i \ln(\lambda) - n \lambda - \sum_{i=1}^n\ln( x_i!)\\\\
\frac{d\ell}{d\lambda} &= \frac{\sum_{i=1}^n x_i}{\lambda} - n
\end{aligned}$$
Set the derivative equal to 0.
$$\begin{aligned}
\frac{\sum_{i=1}^n x_i}{\lambda} - n &= 0\\\\
\frac{\sum_{i=1}^n x_i}{\lambda} &= n\\\\
\lambda &= \frac{\sum_{i=1}^n x_i}{n}\\\\
\hat{\lambda}_{MLE} &= \bar{x}
\end{aligned}$$
The maximum likelihood estimator of $\lambda$ is the sample mean.
