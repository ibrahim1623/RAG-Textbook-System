```markdown
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

3-10

# CHAPTER 3. STATISTICAL ESTIMATION

A standard answer is that \( \sigma_e^2 \) is biased, whereas \( S^2 \) is not (Exercise 2.9). The bias turns out to be small relative to \( sd(\sigma_e^2) \), however, in the important special case that the \( Y_i \) are also normally distributed. Then, via the arguments of Section 2.4.2,

\[
E(X) = (n - 1)\sigma^2
\]

and

\[
Var(X) = 2(n - 1)\sigma^4,
\]

whereupon 

\[
Bias(\sigma_e^2) = E(\sigma_e^2) - \sigma^2 = \frac{(n - 1)\sigma^2 - \sigma^2}{n} = -\frac{\sigma^2}{n}
\]

and 

\[
Var(X) = \frac{1}{n^2}2(n - 1)\sigma^4.
\]

We see that for any \( n \geq 2 \), the bias of \( \sigma_e^2 \) is smaller in magnitude than its standard deviation:

\[
\frac{Bias(\sigma_e^2)}{-\sigma^2/n} = \frac{1}{\sqrt{2(n - 1)}} \frac{\sigma^2}{sd(\sigma_e^2)}
\]

Of course, no bias is better than a “small” bias, but Exercise 3.4 shows that \( \sigma_e^2 \) has a smaller standard deviation and smaller MSE than \( S^2 \) and is more accurate overall. The most compelling case for the use of \( S^2 \) with divisor \( n - 1 \) is that, for IID normal random variables, \( X \) has a \( \chi^2_{n-1} \) distribution with \( n - 1 \) degrees of freedom, and hence \( S^2 \) fits the mathematical requirements of the t distribution (Section 2.4.3). ♢♢♢

Usually, the MSE of an estimator either equals its variance (unbiased estimation) or is not much larger than the variance (small squared bias). Hence, we will see that when a confidence interval is calculated to quantify error it is nearly always based on the estimator’s standard deviation only. Estimation bias may be ignorable, but there are many other possible sources of bias in an empirical study. They include sampling from a population other than the target one or bias in the measurement system producing data. Moreover, other sources are difficult to study in a quantitative way by analysis of the data (and hence will not be pursued much in this text). Best practice is to mitigate sources of bias proactively by careful study design and objective measurement. 

## 3.3.5 Consistency

### Definition 3.3 (Consistency)

The estimator \( \tilde{\theta}_n \) of a parameter \( \theta \) based on a sample of size \( n \) is consistent for estimating \( \theta \) if 

\[
Pr(|\tilde{\theta}_n - \theta| < \epsilon) \rightarrow 1 \text{ as } n \rightarrow \infty
\]

for any fixed error, \( \epsilon > 0 \). 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

3.3. PROPERTIES OF AN ESTIMATOR

3-11

Consistency of \( \tilde{\theta}_n \) is a special case of convergence in probability of a random variable \( (\tilde{\theta}_n \) here) to a constant \( (\theta) \). Consistency requires that both the bias and variance of \( \tilde{\theta} \) go to zero as \( n \rightarrow \infty \). Hence, a necessary and sufficient condition is that the mean squared error goes to zero. Many estimators are of the form of a sample mean, which includes the sample proportion, or a simple function of the sample mean. If the objective is to estimate the mean of the underlying distribution, and the sample consists of independent observations, then consistency of such estimators is easily established as a special case of the Weak Law of Large Numbers (WLLN). 

### Theorem 3.1 (Weak law of large numbers (WLLN))

Let 

\[
\overline{Y}_n = \frac{1}{n}\sum_{i=1}^{n} Y_i,
\]

where \( Y_1, \ldots, Y_n \) are \( n \) independent random variables, each with mean \( \mu \) and variance \( \sigma^2 \) (both of which must exist). Then, for any \( \epsilon > 0 \),

\[
Pr(|\overline{Y}_n - \mu| < \epsilon) \rightarrow 1 \text{ as } n \rightarrow \infty.
\]

The law of large numbers is not about large observations! It is concerned with a large sample size, \( n \). Also, the random variables are not the individual elements of the sample. Rather, as the sample size, \( n \), increases, there is a sequence of sample means \( \overline{Y}_n \), computed from more and more elements. In the WLLN, \( \epsilon \) can be made arbitrarily small as long as it is positive. Thus, the theorem says that the distribution of \( \overline{Y}_n \) is more and more concentrated around an arbitrarily small neighbourhood of \( \mu \) as the sample size grows. Thus, \( \overline{Y}_n \) is a consistent estimator of \( \mu \). 

The proof of the WLLN is straightforward. From (1.9) we have

\[
E(\overline{Y}_n) = \frac{1}{n}\sum_{i=1}^{n} E(Y_i) = \mu.
\]

Similarly, we use (1.10) to get \( Var(\overline{Y}_n) \). Because we are assuming the \( Y_i \) are independent, all the covariance terms, \( Cov(Y_i, Y_j) \) for \( i \neq j \), in (1.10) are zero. Thus,

\[
Var(\overline{Y}_n) = \frac{1}{n^2}\sum_{i=1}^{n} Var(Y_i) = \frac{\sigma^2}{n}.
\]

Clearly, \( Var(\overline{Y}_n) \rightarrow 0 \) as \( n \rightarrow \infty \), and the result follows by putting \( t = \epsilon \) in Chebyshev’s inequality (Theorem 1.1). 

### Example 3.4 (Opinion polls: weak law of large numbers)

Each voter in the population of eligible voters intends to vote for the Statistics for Everybody Party (\( y = 1 \)) or will not (\( y = 0 \)) in the next federal election. 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

3-12

# CHAPTER 3. STATISTICAL ESTIMATION

To estimate the population proportion, \( \pi \), intending to vote for Statistics for Everybody, a random sample of \( n \) eligible voters is taken. Let \( Y_i \) be the voting intention for person \( i \) in the sample; it is a Bernoulli random variable with \( Pr(Y_i = 1) = \pi \), i.e., \( Bern(\pi) \). Note that \( E(Y_i) = \pi \) and \( Var(Y_i) = \pi(1 - \pi) \). We further assume that \( Y_1, \ldots, Y_n \) are independent random variables (which would be approximately true if the population size is large relative to the sample size, which it usually is). Consider estimating \( \pi \) using the sample mean,

\[
\overline{Y}_n = \frac{1}{n} \sum_{i=1}^{n} Y_i,
\]

where the subscript \( n \) on \( \overline{Y}_n \) emphasizes that we are investigating the impact of increasing the sample size. (The sample mean is also a sample proportion here: As \( Y_i \) take values \( 0 \) and \( 1 \) only, \( \overline{Y} \) is the proportion of 1’s in the sample.) Then, from Exercise 1.17,

\[
E(\overline{Y}_n) = \pi,
\]

and 

\[
Var(\overline{Y}_n) = \frac{\pi(1 - \pi)}{n}.
\]

The variance clearly tends to zero as \( n \) increases. Thus, by Chebyshev’s inequality (Theorem 1.1), the estimator \( \overline{Y} \) is in an arbitrarily small neighbourhood of the true value \( \pi \) with probability approaching \( 1 \) as the sample size \( n \) grows, and \( \overline{Y}_n \) is a consistent estimator of \( \pi \). 

We could argue the same result directly from the WLLN. The conditions of the WLLN are easily verified: \( Y_1, \ldots, Y_n \) are independent and the mean and variance of \( Y_i \) both exist. Hence, via the WLLN, the sample mean of \( Y_1, \ldots, Y_n \) is a consistent estimator of \( E(Y_i) = \pi. \) ♢♢♢

Consistency of \( \tilde{\theta} \) is a natural requirement: an estimator that does not converge to \( \theta \) for an infinite sample size should be questioned. 

## 3.3.6 Relative Error

Implicitly, the measures of error used so far have related to absolute error. For example,

\[
Var(\tilde{\theta}) = E\left(\tilde{\theta} - \theta\right)^2,
\]

where positive and negative errors \( \tilde{\theta} - \theta \) are treated the same due to squaring. Similarly, in MSE and its squared bias component, the sign of the bias is immaterial. For some applications, relative error,

\[
\frac{\tilde{\theta} - \theta}{\theta} = \frac{\tilde{\theta}}{\theta} - 1,
\]

and summary measures based on it are more compelling, however. The following sample-size calculation illustrates that the different definitions of error can have important consequences. 

### Example 3.5 (Binomial distribution: sample size determination)

A common question is, “What should the sample size be?” For instance, the opinion poll of Example 2.3 had \( n = 1000 \). Why are the sample sizes of opinion polls typically of order one thousand? Example 2.3 boils down to estimation of \( \pi \) in a \( Bin(n, \pi) \) probability model. Suppose the requirement is to determine \( n \) such that \( sd(\tilde{\pi}) \leq 0.015 \). That requirement is often stated as 1.5 percentage points, to emphasize that it is an absolute number of “points” on the percentage scale. Rearrangement of

\[
sd(\tilde{\pi}) = \sqrt{\frac{\pi(1 - \pi)}{n}} \leq 0.015
\]

yields

\[
n = \frac{\pi(1 - \pi)}{(0.015)^2},
\]

as shown in the \( n_{abs} \) row of Table 3.2. The required sample size depends on the true value \( \pi \). It is maximized when \( \pi = 0.5 \) and decreases as \( \pi \) decreases. Similarly \( n_{abs} \) decreases as \( \pi \) increases above \( 0.5 \) (not shown) in a symmetric way. Thus, a sample size \( n_{abs} = 1112 \) will give \( sd(\tilde{\pi}) \leq 0.015 \) for any \( \pi \), and a \( 95\% \) confidence interval using the standard error and a normal approximation will be no wider than \( ±z_{0.0975} se(\tilde{\pi}) = ±1.96 \times 0.015 = ±0.0294 \), or about plus or minus 3 percentage points. As \( n_{abs} \) does not change much for, say, \( 0.2 < \pi < 0.8 \), a sample size based on the worst case, \( \pi = 0.5 \), is often employed when \( \pi \) is anticipated in such a range. The previous argument becomes less relevant when \( \pi \) is small, however. Table 3.2 gives \( n_{abs} = 44 \) for \( \pi = 0.01 \), for instance, but the requirement \( sd(\tilde{\pi}) \leq 0.015 \) probably needs tightening: the standard deviation is larger than the true value. More natural is to control the standard deviation to be small relative to the true value, e.g., \( sd(\tilde{\pi}) \leq 0.03\pi \). 

Applying the rule for the variance (hence standard deviation) of a linear function of a random variable, the new requirement is equivalent to

\[
sd\left(\frac{\tilde{\pi} - \pi}{\pi}\right) = 0.03 = \frac{sd(\tilde{\pi})}{\pi}.
\]

Solving 

\[
0.03\pi = sd(\tilde{\pi}) = \sqrt{\frac{\pi(1 - \pi)}{n}}
\]

for \( n \) yields

\[
n = \frac{\pi(1 - \pi)}{(0.03)^2\pi^2} \text{ for } \pi < 0.5.
\]

For \( \pi = 0.5 \), there is no impact on sample size as the absolute and relative requirements are chosen to be equivalent at \( \pi = 0.5 \). But \( n_{rel} \) increases rapidly as \( \pi \) approaches zero: even for a moderately small \( \pi = 0.05 \) we need a sample size of \( n_{rel} = 21,112 \), increasing to \( 110,000 \) at \( \pi = 0.01 \). Relaxing the requirement so that \( sd(\tilde{\pi}) \leq 0.1\pi \) when \( \pi = 0.01 \) still needs \( n_{rel} = 9900 \). Estimating a small probability with good relative accuracy requires a huge sample size. ♢♢♢ 

### 3.4 Comparing Estimators

Bias and variance properties allow comparison of candidate estimators when the choice of estimator is not obvious. An interesting case is the Laplace (double-exponential) distribution. As noted in Section 1.5.4, the distribution is symmetric around the location parameter \( \mu \), which is therefore both the mean and median. Should the sample mean or the sample median from a random sample be used as its estimator? (The sample median is the “middle” value in the data.) It turns out that both estimators are unbiased, but the sample median has the smaller variance for \( n \geq 3 \) (Sarhan, 1954). These results are demonstrated numerically in Exercise 3.5. The sample median is naturally more robust to unusual outlying observations that can arise due to the Laplace PDF’s fat tails, and this intuition is borne out by the theoretical properties.

### 3.5 Getting It Done in R

In Example 3.1 random samples were drawn from the Poisson distributions. R has functions to generate random numbers for all the distributions listed in Table 1.9. They have names starting with `r`. Thus, R has functions with names starting with `d` for the PDF or PMF, `p` for the CDF, `q` for a quantile, and `r` for generating random numbers. Table 3.3 lists these functions for the normal distribution, for instance. The function `rnorm` has an argument `n` for the sample size. Hence, `rnorm(n = 10)` would generate a sample of size \( n = 10 \) from the standard normal. 

### 3.6 Learning Outcomes

On completion of this chapter you should be able to carry out the following tasks. 
1. Explain the difference between an estimate and an estimator of a parameter and why the distinction is important to define statistical properties. 
2. Derive the following properties for a specific estimator: its bias (which might be zero); its variance; its mean squared error; and whether or not it is consistent. 
3. Use the WLLN (Theorem 3.1 in Section 3.3.5), and check the conditions, to show the sample mean is a consistent estimator of the mean of the underlying distribution. 
4. Explain your reasoning. When using a result such as the expectation or variance of a linear combination of random variables to derive a property of an estimator, briefly state the result you are using. If the result depends on an assumption such as statistical independence of random variables, remind the reader that you are using the assumption. 

### 3.7 Exercises

#### Exercise 3.1

Frequentist inference considers variation across hypothetical repeated random samples. In some cases, the design of a study involves a step with a probabilistic mechanism to select a sample of data. Briefly describe the probabilistic mechanism and the set of possible random samples for the following studies:
1. The opinion poll in Example 2.3; and
2. The clinical trial in Example 1.15. 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

3-16

# CHAPTER 3. STATISTICAL ESTIMATION

#### Exercise 3.2
Suppose we obtain \( n \) independent observations, \( Y_1, \ldots, Y_n \), from a Poisson probability model to estimate the Poisson parameter \( \mu \). Consider the estimator \( \tilde{\mu} = \overline{Y} \). 
1. Show \( \tilde{\mu} \) is unbiased. 
2. Find \( Var(\tilde{\mu}) \) (an exact formula for the variance). 
3. Is \( \tilde{\mu} \) a consistent estimator of \( \mu \)? 
4. Consider \( Var(\tilde{\mu}) = \frac{\tilde{\mu}}{n} \) as an estimator of \( Var(\tilde{\mu}) \).
   (a) Show that \( Var(\tilde{\mu}) \) is an unbiased estimator of \( Var(\tilde{\mu}) \).
   (b) What is the variance of \( Var(\tilde{\mu}) \)?
   (c) Is \( Var(\tilde{\mu}) \) a consistent estimator of \( Var(\tilde{\mu}) \)? 

#### Exercise 3.3
Let \( Y_1, \ldots, Y_n \) be independent \( N(\mu, \sigma^2) \) random variables. Their sample variance is 

\[
S^2 = \frac{1}{n - 1} \sum_{i=1}^n (Y_i - \overline{Y})^2.
\]

Treat \( S^2 \) as an estimator, i.e., a random variable. Is it a consistent estimator of \( \sigma^2 \)? 

#### Exercise 3.4
[Final exam, 2011–12, Term 1] Let \( Y_1, \ldots, Y_n \) be independent normal random variables, each with mean \( \mu \) and variance \( \sigma^2 \). We want to estimate \( \sigma^2 \) from such a sample of size \( n \geq 2 \) when \( \mu \) is also unknown. 

This question investigates the exact properties of \( \sigma_e^2 = \frac{X}{n} \), where \( X = \sum_{i=1}^{n} (Y_i - \overline{Y})^2 \). You may use without proof: (1) the result that \( \frac{X}{\sigma^2} \) has a \( \chi^2_{n-1} \) distribution; and (2) statistical properties of the \( \chi^2 \) distribution. 
1. Show that the expectation of \( \sigma_e^2 \) is \( \frac{\sigma^2(n - 1)}{n} \). 
2. Show that the variance of \( \sigma_e^2 \) is \( \frac{2(n - 1)\sigma^4}{n^2} \). 
3. Hence, give and simplify an expression that summarizes the accuracy of \( \sigma_e^2 \) as an estimator of \( \sigma^2 \). 
4. Is \( \sigma_e^2 \) a consistent estimator of \( \sigma^2 \)? Explain briefly. 
5. The sample variance with divisor \( n−1 \), namely \( S^2 = \frac{X}{n−1} \), has \( E(S^2) = \sigma^2 \) and \( Var(S^2) = \frac{2\sigma^4}{n − 1} \). Give one advantage and one disadvantage of \( S^2 \) relative to \( \sigma_e^2 \) as an estimator of \( \sigma^2 \). 
6. Explain which estimator of \( \sigma^2 \) is the more accurate, \( S^2 \) or \( \sigma_e^2 \).

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

3.7. EXERCISES

3-17

``` 

This formatted markdown code preserves all the details, structure, and formatting as provided in the original text, ensuring accuracy in mathematical notation and other elements as per your requirements.