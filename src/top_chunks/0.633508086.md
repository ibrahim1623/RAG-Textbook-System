```markdown
Again, particularly for complex problems, this is not easy. 4. Use the probability model to answer questions of scientific interest, make predictions, etc. 3.2

## The Frequentist Philosophy

This chapter concentrates on the second of the steps outlined above: estimating the parameters of a given (chosen) distribution. In general, let \( \theta \) be a parameter of interest (e.g., \( \pi \) for the binomial distribution). We use some method to generate an estimate, \( \hat{\theta} \), from the data. When we compute a numeric value for \( \hat{\theta} \) this is an estimate. For instance, consider Example 2.3 where the parameter \( \pi \) of interest was the proportion in a large population agreeing with the statement that Trudeau was the best Prime Minister. The binomial distribution was the probability model, and \( \pi \) had the estimate \( \hat{\pi} = 0.36 \). In general, an estimate of a parameter is based on one or more statistics, functions of the data like the sample mean or sample proportion. Without knowing the true value of the parameter we cannot say how good an estimate is. Furthermore, a number has no statistical properties. It is just a number. In the frequentist philosophy of statistics, we consider the values of \( \hat{\theta} \) that would have occurred in repeated random samples from the assumed probability distribution for the data. (The term “frequentist” here parallels the frequentist interpretation of probability, where probabilities are defined by long-run relative frequencies in repetitions of an experiment like rolling a die.) Often, this is a hypothetical argument as there is only one sample of data values. Nonetheless, if we consider other samples that might have occurred, each sample would generate its own value of \( \hat{\theta} \), and now \( \hat{\theta} \) has a sampling distribution, i.e., it is a random variable. The random variable is called an estimator of \( \theta \) and will be denoted by \( \tilde{\theta} \). The statistical properties of the random variable \( \tilde{\theta} \), explored in the next subsection, can be used to make statements about how accurate \( \tilde{\theta} \) is in estimating \( \theta \) over repeated random samples of data.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

### 3.2. THE FREQUENTIST PHILOSOPHY

| Faults | Frequency | (y) observed | expected |
|--------|-----------|--------------|----------|
| 0      | 1         | 1.5          | 1        |
| 5      | 3.7       | 2            | 3        |
| 4      | 3.6       | 4            | 2        |
| 5      | 1.0       | >5           | 0        |
| 0      | 0.6       | 17           | 17.0     |

**Table 3.1:** Observed numbers of faults on data lines of length about 170 km, and the expected numbers under a Poisson probability model.

Many textbooks and articles use the notation \( \hat{\theta} \) both for an estimate, i.e., a number for a specific data set, and for the estimator. The context has to guide the reader whether this refers to an estimate or an estimator. In our text, however, the distinction between \( \tilde{\theta} \) and \( \hat{\theta} \) is just like that between a random variable, \( Y \), and one of its values, \( y \), and hopefully helps the reader better understand the frequentist concept of properties over hypothetical repeated samples. The \( \tilde{\theta} \) versus \( \hat{\theta} \) notation is borrowed from my colleagues Professors MacKay and Oldford, with whom I taught at the University of Waterloo. 

#### Example 3.1 (Faults on data lines: estimating the Poisson mean)

The number of faults (y) over a period of time was collected for a sample of 17 data-transmission lines, all of length about 170 km. The observed frequencies are in Table 3.1. For instance, there are 5 lines with exactly 1 fault. The data are displayed as a histogram in Figure 3.1(a). Suppose the number of faults per line in the population of all lines is represented by a Poisson distribution, i.e., \( \text{Pois}(\mu) \), which has PMF

\[
f_Y(y) = \frac{e^{-\mu} \mu^y}{y!} \quad (y = 0, 1, \ldots , \infty; \mu > 0).
\]

(There are good engineering reasons for using the Poisson distribution here.) The parameter \( \mu \) is the expectation or mean of the \( \text{Pois}(\mu) \) distribution, which we need to estimate to assess the reliability of the system. As \( \mu \) is the mean of the assumed distribution, we use the sample mean, \( \bar{y} \), as an obvious estimate of \( \mu \) from the data. The observed sample mean is

\[
\bar{y} = \frac{1}{17} \sum_{i=1}^{17} y_i = \frac{0 \times 1 + 1 \times 5 + 2 \times 3 + 3 \times 4 + 4 \times 2 + 5 \times 2}{17} = 2.41
\]

for the faults data. We write \( \hat{\mu} = 2.41 \) for the estimate of \( \mu \) here.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

![Histogram of the faults data in Table 3.1.](Figure_3.1_a.png)

- (b) Poisson sample \( (\mu = 2.41, y = 2.06) \)
  
| Frequency |          |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |
|-----------|----------|----|----|----|----|----|----|----|----|----|
|           |          |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |
|           |          |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |

- (a) Faults data \( (y = 2.41) \)

![Histogram of three random samples of size n = 17 from a Poisson distribution with the parameter \( \mu \) set to 2.41, which is the value of \( \bar{y} \) observed for the faults data.](Figure_3.1_b.png)

How good is this estimate? This question is difficult to answer for the specific sample, but we can look at properties over random samples. Such properties are defined mathematically in Section 3.3. For now, we can informally compare the sample data with random samples of size \( n = 17 \) drawn from a \( \text{Pois}(\mu) \) distribution. The value of \( \mu \) is unknown—the objective here is to estimate it—but we proceed by setting \( \mu \) to 2.41, the estimate from the data. This gives an idea of how much the data and hence \( \hat{\mu} \) vary from one sample to another just by chance if \( \mu \) is about 2.41. The histograms in Figures 3.1(b), (c), and (d) show three such random samples created via rpois in R. 

Two features of the plots are worth noting.

- There is a fair amount of difference in shape in the histograms of Figures 3.1(b), (c), and (d) because the sample size is small. The histogram of the faults data in Figure 3.1(a) does not stand out compared to the Poisson samples.
- The sample mean, \( \bar{y} \), is reported for the three samples from a \( \text{Pois}(\mu = 2.41) \) distribution. It ranges from 2.06 to 3.00. Thus, just by chance, the sample mean varies from one random sample to another. Such sampling variation across repeat random samples is the basis for treating the sample mean as a random variable, \( \bar{Y} \). 

The variation in \( \bar{Y} \) across samples defines the uncertainty attached to an estimate in this chapter: the frequentist paradigm. Although Figure 3.1 demonstrates considerable variation in the sample mean here just due to chance, the data are good enough to narrow down the range of possible values of \( \mu \) in a statistical sense. 

![Histogram of the faults data in Table 3.1.](Figure_3.2_a.png)

Figure 3.2 repeats Figure 3.1, but now \( \mu = 5 \) when generating three random samples from the \( \text{Pois}(\mu) \) distribution. The histogram of the data in Figure 3.2(a) now stands out: The other three histograms are shifted to the right. Furthermore, the sample means from the \( \text{Pois}(\mu = 5) \) distributions still vary but take values much larger than \( \bar{y} = 2.41 \) for the faults data. We really need more random samples to say much more, but it looks like the data rule out \( \mu = 5 \) via this statistical sampling argument. 

Is the Poisson distribution a reasonable probability model here? If we set \( \mu \) to the estimate 2.41, the Poisson PMF is

\[
f_Y(y) = \frac{e^{-2.41} (2.41)^y}{y!}.
\]

Thus, in a sample of size 17 we would expect \( 17 f_Y(0) = 17 \times 0.0898 = 1.5 \) values of 0, \( 17 f_Y(1) = 17 \times 0.216 = 3.7 \) values of 1, etc. These expected frequencies are also given in Table 3.1. The agreement between observed and expected frequencies appears good. Goodness of fit between data and a hypothesized distribution is taken up more formally in Section 8.4.

### 3.3. PROPERTIES OF AN ESTIMATOR

Let \( \tilde{\theta} \) be an estimator of the parameter \( \theta \). How good is \( \tilde{\theta} \): How much error does it have in estimating \( \theta \)? We can answer this question, at least probabilistically, by examining the statistical properties of \( \tilde{\theta} \) and hence its error, \( \tilde{\theta} - \theta \). All the properties, like expectation and variance of \( \tilde{\theta} \), are with respect to its sampling distribution over repeated random samples. 

#### 3.3.1 Bias

The bias of \( \tilde{\theta} \) as an estimator of \( \theta \) follows from its expectation. 

**Definition 3.1 (Bias)**  
The bias of the estimator \( \tilde{\theta} \) of a parameter \( \theta \) is 

\[
\text{Bias}(\tilde{\theta}) = E(\tilde{\theta}) - \theta.
\] 

Rewriting the bias as 

\[
\text{Bias}(\tilde{\theta}) = E(\tilde{\theta}) - \theta = E(\tilde{\theta} - \theta),
\]

we see that the bias is the mean of the error distribution. If \( E(\tilde{\theta}) = \theta \), then the bias is zero, and we say that \( \tilde{\theta} \) is unbiased. Unbiasedness means that the sampling distribution of \( \tilde{\theta} \) is centred on the true value, \( \theta \), in the sense that the error might be positive or negative from one sample to another, but these errors cancel out on average. Thus, unbiasedness is desirable. 

#### 3.3.2 Variance

The variance of \( \tilde{\theta} \) as an estimator of \( \theta \) is defined just like the variance of any random variable (Definition 1.3). Small values of \( \text{Var}(\tilde{\theta}) \) are desirable in the sense that the estimator has small variability over random samples. 

#### 3.3.3 Mean squared error

A measure of accuracy summarizing the distribution of the error \( \tilde{\theta} - \theta \) is the mean squared error (MSE), the expectation of the squared error.

**Definition 3.2 (Mean squared error (MSE))**  
The mean squared error of \( \tilde{\theta} \) as an estimator of \( \theta \) is 

\[
\text{MSE}(\tilde{\theta}) = E(\tilde{\theta} - \theta)^2.
\] 

It can be decomposed as 

\[
\text{MSE}(\tilde{\theta}) = \text{Var}(\tilde{\theta}) + \text{Bias}^2(\tilde{\theta}).
\]

The MSE combines the bias and variance properties of \( \tilde{\theta} \) in a single measure. The decomposition of the MSE into its two components can be seen by writing:

\[
\text{MSE}(\tilde{\theta}) = E\left(\tilde{\theta} - \theta\right)^2 = E\left(\tilde{\theta} - E(\tilde{\theta}) + E(\tilde{\theta}) - \theta\right)^2
\]

\[
= E\left(\tilde{\theta} - E(\tilde{\theta})\right)^2 + 2E\left(\tilde{\theta} - E(\tilde{\theta})\right) \text{Bias}(\tilde{\theta}) + \text{Bias}^2(\tilde{\theta}).
\]

From the definition of variance, we know \( E\left(\tilde{\theta} - E(\tilde{\theta})\right) = 0 \), thus finally getting:

\[
\text{MSE}(\tilde{\theta}) = \text{Var}(\tilde{\theta}) + \text{Bias}^2(\tilde{\theta}).
\]

Thus, mean squared error penalizes an estimator both for having bias (i.e., the wrong expectation or mean) and for its variance. As MSE decreases, the accuracy of \( \tilde{\theta} \) in estimating \( \theta \) increases in this statistical sense. If \( \tilde{\theta} \) is unbiased, then \( \text{MSE}(\tilde{\theta}) = \text{Var}(\tilde{\theta}) \). This is often the case, exactly or approximately, hence the emphasis on variance calculations in statistical inference about parameters. 

#### Example 3.2 (Faults on data lines: properties of the estimator of \( \mu \))

Example 3.1 used \( \hat{\mu} = \bar{y} = 2.41 \) as an obvious estimate of the Poisson parameter, \( \mu \), for the faults data with \( n = 17 \). To assess the accuracy of this estimate we can think in terms of repeated random samples of the data and the estimator \( \tilde{\mu} \). How far can \( \tilde{\mu} \) stray from \( \mu \) in a probabilistic sense just by chance sampling variation? The sample mean \( \bar{Y} \) is the mean of 17 IID Poisson random variables here. From the properties in Table 1.3, a Poisson random variable \( Y \) has mean \( \mu \) and variance \( \mu \). The following properties of \( \bar{Y} \) are shown more generally in Section 2.4.1.

- **Unbiasedness**: As \( \bar{Y} = \frac{1}{17} \sum_{i=1}^{17} Y_i \) has the same expectation as \( E(Y_i) = \mu \), we have \( E(\bar{Y}) = \mu \) and \( \tilde{\mu} \) is an unbiased estimator of \( \mu \) for any value of \( n \).
  
- **Variance**: As \( \bar{Y} \) has variance \( \text{Var}(Y_i)/17 \), we have \( \text{Var}(\tilde{\mu}) = \mu/17 \).

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

- **Estimated standard deviation or standard error**: Because \( \text{Var}(\tilde{\mu}) = \mu/17 \) depends on \( \mu \), in practice it has to be estimated. An obvious estimate is 

\[
\hat{d} = \frac{\hat{\mu}}{17} = \frac{2.41}{17} = 0.142.
\]

Equivalently, the estimated standard deviation of \( \tilde{\mu} \) is 

\[
sd(\tilde{\mu}) = 0.142 = 0.38.
\]

An estimated standard deviation is often called a standard error, which we write as \( se(\tilde{\mu}) \) here. Note that only a random variable, here \( \tilde{\mu} \), can have a variance or standard deviation, whether it is estimated or not. Thus, \( sd(\tilde{\mu}) = se(\tilde{\mu}) = 0.38 \) makes statistical sense, but \( sd(\hat{\mu}) \) or \( se(\hat{\mu}) \) do not. Authors will often write a looser statement like, “an estimate \( \hat{\mu} = 2.41 \) with a standard error of 0.38,” but we need to interpret “with” in the sense of a property of \( \tilde{\mu} \) not \( \hat{\mu} \). 

- **Mean squared error**: Because \( \tilde{\mu} \) is an unbiased estimator of \( \mu \), the MSE of \( \tilde{\mu} \) is also \( \mu/17 \). To summarize, while the estimate \( \hat{\mu} = 2.41 \) is a number with no statistical properties, the corresponding estimator \( \tilde{\mu} \) is unbiased over repeated samples of size \( n = 17 \). Hence, the MSE of the estimator is entirely due to its variance, namely \( \mu/17 \). The estimator has an estimated variance of 0.142 or equivalently an estimated standard deviation of 0.38.

♢♢♢

Several facts specific to the Poisson distribution were used in Example 3.2 to obtain statistical properties of the estimator of \( \mu \). Chapter 4 takes a general approach, the method of maximum likelihood, for estimation and quantification of the uncertainty of estimators. It relies less on knowledge of specific properties and can be extended to applications where exact properties are unavailable. 

#### 3.3.4 Practical perspective

Estimation bias is usually of little practical consequence, as it is typically zero or small relative to the standard deviation of an estimator. The following example questions whether a familiar unbiasedness argument is compelling.

#### Example 3.3 (Sample variance: divisor of \( n - 1 \) or \( n \)?)

Let \( Y_1 , \ldots , Y_n \) have constant mean \( \mu \) and constant variance \( \sigma^2 \). A vexing question to countless students of statistics is why not define their sample variance with a divisor of \( n \), i.e.,

\[
\sigma_e^2 = \frac{1}{n} \sum_{i=1}^{n} (Y_i - \bar{Y})^2,
\]

instead of the familiar 

\[
S^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (Y_i - \bar{Y})^2?
\]
```