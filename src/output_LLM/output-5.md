```markdown
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 2.4. ESTIMATING THE PARAMETERS OF THE NORMAL

**Proof.** Write

$$
\sum_{i=1}^{n} Z_i^2 = \sum_{i=1}^{n} (Z_i - \bar{Z})^2 + n \bar{Z}^2. \tag{2.3}
$$

(This is just a restatement of the equivalent formulas in (2.2) with \( Z \) instead of \( Y \).) Then use an argument based on MGFs.

1. On the right of (2.3), denote by \( M(t) \) the MGF of \( \sum_{i=1}^{n} (Z_i - \bar{Z})^2 \). This sum is the random variable of interest in Theorem 2.1. By finding its MGF, we will identify its distribution.

2. In the second term on the right of (2.3), \( \bar{Z} \sim N(0, 1/n) \), so that \( n \bar{Z} \sim N(0, 1) \). Hence, \( n \bar{Z}^2 \sim \chi^2_1 \) with MGF \( (1 - 2t)^{-1/2} \) (see Exercise 2.3). 

3. We also note that \( Z_i - \bar{Z} \) and \( \bar{Z} \) are independent (use the result of Exercise 2.8 in the special case of \( Z \) with \( \mu = 0 \) and \( \sigma^2 = 1 \) instead of \( Y \)). Thus, the two terms on the right of (2.3) are independent and by Lemma 1.3 their sum has MGF \( M(t) \times (1 - 2t)^{-1/2}. \)

4. On the left of (2.3), Lemma 2.1 says that \( \sum_{i=1}^{n} Z_i^2 \) has a \( \chi^2_n \) distribution with MGF \( (1 - 2t)^{-n/2}. \) 

5. Hence, equating the MGFs of the left and right of (2.3),

$$
(1 - 2t)^{-n/2} = M(t) \times (1 - 2t)^{-1/2},
$$
and \( M(t) = (1 - 2t)^{-(n-1)/2} \), which is the MGF of a \( \chi^2_{n-1} \) random variable. The consequence of Theorem 2.1 is that \( S^2/\sigma^2 \) has the same distribution as that of a \( \chi^2_{n-1} \) random variable divided by \( n - 1. \)

### 2.4.3 Distribution of the standardized sample mean (unknown variance)

At the end of Section 2.4.1 we looked ahead to making statistical inference about the mean \( \mu \) based on the sample mean, \( \bar{Y} \). We noted that in practice \( \sigma^2 \) will have to be estimated in the standardized sample mean,

$$
\frac{\bar{Y} - \mu}{\sqrt{\sigma^2/n}},
$$
in (2.1). The obvious strategy is to use the sample variance, \( S^2 \), as it is an unbiased estimator of \( \sigma^2 \). The standardized mean becomes

$$
\frac{\bar{Y} - \mu}{\sqrt{S^2/n}}. $$

Replacing \( \sigma^2 \) by \( S^2 \) will change the standard normal distribution on the right of (2.1). It becomes a \( t_{n-1} \) distribution. To see this, we write

$$
\frac{\bar{Y} - \mu}{\sqrt{\sigma^2/n}} = \frac{\bar{Y} - \mu}{\sqrt{S^2/n} \cdot \frac{S^2}{\sigma^2}}. \tag{2.4}
$$

We then argue as follows about the numerator and denominator of this expression.

- The numerator, \( \frac{\bar{Y} - \mu}{\sqrt{\sigma^2/n}} \) is back to the random variable in (2.1) and therefore has the same distribution as \( Z \sim N(0, 1) \). 

- The denominator is \( S^2/\sigma^2 \). At the end of Section 2.4.2, we concluded that \( S^2/\sigma^2 \) has the same distribution as that of a \( \chi^2_{n-1} \) random variable divided by \( n - 1 \). Thus, the denominator has the same distribution as \( X_{n-1}/(n - 1) \), where \( X_{n-1} \sim \chi^2_{n-1}. \)

- The random variables in the numerator and denominator are \( \bar{Y} \) and \( S^2 \), respectively. Now, \( S^2 \) is a function of \( Y_i - \bar{Y} \) \( (i = 1, \ldots, n), \) and Exercise 2.8 shows that \( \bar{Y} \) and \( Y_i - \bar{Y} \) are independent. Therefore, \( \bar{Y} \) and \( S^2 \) are independent, and the numerator and denominator of (2.4) are independent. These properties of the numerator and denominator of 2.4 are those leading to the \( t \) distribution in Lemma 2.2. Thus,

$$
\frac{\bar{Y} - \mu}{\sqrt{S^2/n}} \sim t_{n-1}. \tag{2.5}
$$

In Lemma 2.2, the degrees of freedom are given by \( d = n - 1 \), because we related \( S^2/\sigma^2 \) to \( \chi^2_{n-1} \). Thus, we will use the \( t_{n-1} \) distribution for inference about the mean of a normal distribution when the variance is unknown. This is the result derived by Student (1908), which was motivated by his analysis of experimental results at Guinness Breweries in Dublin. 

### Example 2.1 (Lung function: confidence interval for the normal mean)

Schlaich et al. (1998) conducted a study on reduced pulmonary (i.e., lung) function in patients with spinal osteoporosis (“manifest osteoporosis”). Their objective was to compare pulmonary function between patients with this manifest osteoporosis and patients without the condition. For now we will consider only the manifest osteoporosis data here. The measure of lung function was forced expiratory volume in 1 second (FEV1). The raw measure is adjusted for sex, age, and body height, leading to a percentage (FEV1%) relative to a standard, called \( y \) below. (The calculations in this example are based on data adjusted for current body height.) Data for \( n = 34 \) patients with manifest osteoporosis were collected, which we will treat as a random sample from a larger population of interest. The authors checked that the data are consistent with arising from a normal distribution. They were interested in estimating the mean, \( \mu \), of the normal distribution when \( \sigma^2 \) is unknown. The data summaries for the sample of size 34 are:

$$
\bar{y} = 94.3
$$

and 

$$
s = 14.7,
$$

where \( s \) is the sample standard deviation. The estimate of \( \mu \) is \( \bar{y} = 94.3 \) here. How much error could there be in this estimate just by chance due to random sampling? The analysis Schlaich et al. conducted was based on the exact \( t \) distribution in (2.5), i.e.,

$$
\frac{\bar{Y} - \mu}{\sqrt{S^2/n}} \sim t_{n-1}. 
$$

Given \( 0 < \alpha < 1 \), by definition the quantiles \( t_{n-1,\alpha/2} \) and \( t_{n-1,1-\alpha/2} \) cut off a probability of \( \alpha/2 \) in each tail of the \( t_{n-1} \) distribution, and

$$
P\left( \frac{\bar{Y} - \mu}{\sqrt{S^2/n}} < t_{n-1,1 - \alpha/2} \right) = 1 - \alpha.
$$

Rearrangement gives

$$
P\left( \bar{Y} + t_{n-1,\alpha/2} \frac{S}{\sqrt{n}} < \mu < \bar{Y} + t_{n-1,1 - \alpha/2} \frac{S}{\sqrt{n}} \right) = 1 - \alpha,
$$

which is a probabilistic bound on \( \mu \). Figure 2.6 illustrates. Note that the random variables here are the estimators \( \tilde{\mu} = \bar{Y} \) and \( \tilde{\sigma} = S \). When we replace them by the numerical estimates \( \bar{y} \) and \( s \) from the data, we have a \( 100(1 - \alpha)\% \) confidence interval for \( \mu \):

$$
\bar{y} + t_{n-1,\alpha/2} \frac{s}{\sqrt{n}} < \mu < \bar{y} + t_{n-1,1 - \alpha/2} \frac{s}{\sqrt{n}}.
$$

(Chapter 3 develops the distinction between estimators and estimates.) Because the \( t \) distribution is symmetric, \( t_{n-1,\alpha/2} = -t_{n-1,1 - \alpha/2}. \) With \( n = 34 \) as in the Schlaich et al. study, and \( \alpha = 0.05 \) for 95% confidence, 

```R
qt(0.975, df = 33)
```

in R gives \( t_{n-1,1 - \alpha/2} = t_{33,0.975} = 2.035. \) A 95% confidence interval for \( \mu \) is therefore 

$$
\bar{y} \pm t_{n-1,0.975} \frac{s}{\sqrt{n}} = 94.3 \pm 2.035 \frac{14.7}{\sqrt{34}} = 94.3 \pm 5.1 = [89.2, 99.4]. 
$$

(The units of the interval, percentage points, are the same as for the FEV1% measurements.)

♢♢♢

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## CHAPTER 2. THE NORMAL DISTRIBUTION IN STATISTICS

$$
f(t) 
$$

![](image-placeholder) 

### Figure 2.6: Quantiles of the \( t \) distribution with \( n-1 \) degrees of freedom. The quantiles \( t_{n-1,\alpha/2} = -t_{n-1,1 - \alpha/2} \) and \( t_{n-1,1 - \alpha/2} \) cut off the probability \( \alpha/2 \) in each tail. The PDF shown has \( n - 1 = 33 \) degrees of freedom as in the Schlaich et al. study, and the quantiles shown are for \( \alpha = 0.05 \), leading to a 2-sided 95% confidence interval.

## 2.5 Limiting Normal Distributions

### 2.5.1 Convergence in distribution

**Definition 2.1 (Convergence in distribution)**  
Let \( X_1, X_2, \ldots \) be a sequence of random variables with CDFs \( F_{X_1}(x), F_{X_2}(x), \ldots \), respectively. Suppose there exists a CDF \( F_X(x) \) such that 

$$
\lim_{n \to \infty} P(X_n \leq x) = F_X(x),
$$

for all \( x \) where \( F_X(x) \) is continuous. Then we say that the sequence of random variables \( X_n \) converges in distribution to \( F_X(x). \) The random variables \( X_1, X_2, \ldots \) here are not the individual elements of a sample. Rather, \( X_n \) will be based on a summary like the sample mean of the entire sample. In the next example, we work with a standardized version of the sample total. The example also demonstrates that the limiting distribution may be found from the limiting MGF. 

### Example 2.2 (Binomial distribution: normal approximation)

Let \( X_n \sim Bin(n, \pi) \) with PMF

$$
f_{X_n}(x) = \binom{n}{x} \pi^x (1 - \pi)^{n-x} \quad (x = 0, 1, \ldots, n).
$$

We will show that a standardized version of \( X_n \) has a distribution that converges to the standard normal distribution as \( n \to \infty. \) We want the limiting distribution of \( X_n \) as \( n \to \infty. \) But the limit cannot possibly be a fixed distribution. We know that

$$
E(X_n) = n \pi \quad \text{and} \quad Var(X_n) = n \pi (1 - \pi);
$$

both are changing (increasing) with \( n. \) But

$$
Z_n = \frac{X_n - E(X_n)}{\sqrt{Var(X_n)}} = \frac{X_n - n \pi}{\sqrt{n \pi (1 - \pi)}} \tag{2.6}
$$

has mean 0 and variance 1. It is the distribution of this standardized quantity that converges to a fixed distribution, namely the standard normal. The key steps are: (1) to find the MGF of \( Z_n \) in (2.6); and (2) to show that the MGF tends to that of the standard normal as \( n \to \infty. \) Derivation of the MGF of \( Z_n \) is based on Lemma 1.2 for the MGF of a linear function of a random variable. Write \( Z_n \) in (2.6) as 

$$
Z_n = a_n + b_n X_n,
$$ 

where 

$$
a_n = -\frac{\sqrt{n\pi}}{c}, \quad b_n = \frac{1}{\sqrt{c n}},
$$ 

and \( c = \pi(1 - \pi) \) to simplify notation. From Table 1.3 the MGF of the binomial random variable \( X_n \) is 

$$
M_{X_n}(t) = (1 - \pi + \pi e^t)^n. 
$$

Applying Lemma 1.2 gives

$$
M_{Z_n}(t) = e^{a_n t} M_{X_n}(b_n t) = e^{- \frac{\sqrt{n\pi}}{c} t} \left( (1 - \pi + \pi e^{\frac{1}{\sqrt{c n}}})^n \right). 
$$

which can be rearranged as 

$$
M_{Z_n}(t) = \left( (1 - \pi)e^{\frac{t}{\sqrt{c n}}} + \pi e^{\frac{t}{\sqrt{c n}}} \right)^n.
$$

This completes the first step. To find the limiting MGF of \( Z_n \) as \( n \to \infty \), first make Taylor series expansions of the exponential functions in \( M_{Z_n}(t) \):

$$
M_{Z_n}(t) = (1 - \pi) \left( 1 - \frac{\sqrt{t}}{c} + \frac{t^2}{2c^2} + O\left( \frac{1}{n^{3/2}} \right) \right).
$$

The MGF here is a function of \( t \) and \( n \), but for any fixed value of \( t \), we are interested in the behavior as \( n \to \infty. \) The notation \( O(1/n^{3/2}) \) represents further terms that are decreasing at a rate \( 1/n^{3/2} \) or faster. Technically, if \( m(t, n) \) is the sum of all terms after the \( t^2 \) term, then \( m(t, n) \) is \( O(1/n^{3/2}) \) says that \( |m(t, n)| < a(t)/n^{3/2} \) for some positive constant \( a(t) \) and sufficiently large \( n. \) Thus, \( m(t, n) \) gives a negligible contribution for large \( n, \) providing the leading terms in \( 1/n \) and \( 1/n \) do not both cancel. Collecting terms of order \( t^0, t^1, \) and \( t^2 \) gives

$$
M_{Z_n}(t) = 1 + \frac{(1 - \pi) \pi^2 + \pi(1 - \pi)^2}{2c^2 n} + O\left( \frac{1}{n^{3/2}} \right),
$$

which further simplifies to 

$$
M_{Z_n}(t) = 1 + \frac{t^2}{2} + O\left( \frac{1}{n^2} \right),
$$ 

recalling that \( c = \pi(1 - \pi). \) As \( n \to \infty, \) the \( O(1/n^{3/2}) \) term can be ignored, and 
$$
(1 + \frac{t^2/2}{n})^n \to e^{t^2/2} 
$$ 
(recall that \( (1 + x/n)^n \to e^x \) as \( n \to \infty \)). Thus, 

$$
M_{Z_n}(t) \to e^{t^2/2} 
$$ 

as \( n \to \infty, \)

i.e., the limiting MGF is that of the standard normal (see Table 1.4). Theorem 1.3 says that the MGF uniquely identifies a distribution, and hence the distribution of \( Z_n \) converges to the standard normal distribution as \( n \to \infty. \) 

♢♢♢

### 2.5.2 Limiting distributions and large-sample approximations in statistics

Results on limiting distributions like the result in Example 2.2 show convergence in distribution for a standardized version of a random variable. The sample size, \( n, \) becomes infinitely large. In statistical practice, however, sample sizes are finite. Furthermore, to a statistician the statistic of interest is often an unstandardized random variable. Limiting distributions of standardized random variables justify the use of approximate distributions for finite samples and unstandardized quantities. For instance, let \( X_n \) be a sample from a \( Bin(n, \pi) \) distribution. The sample proportion, \( X_n/n, \) is often used to estimate \( \pi. \) This is not the standardized random variable \( Z_n \) in Example 2.2. We can write \( X_n/n \) in terms of \( Z_n, \) however, by rearranging (2.6):

$$
X_n = n \pi + n \pi (1 - \pi) Z_n,
$$
and hence

$$
\frac{X_n}{n} = \pi + \frac{Z_n \sqrt{\pi(1 - \pi)}}{n}.
$$

For a finite sample, \( Z_n \) has an approximately standard normal distribution, and the theory says that the approximation will become better as the sample size increases. Furthermore, \( X_n/n \) is a linear function of \( Z_n, \) and using the result that a linear function of a normal random variable also has a normal distribution (Example 1.30), \( X_n/n \) has the following approximate distribution:

$$
\frac{X_n}{n} \sim N\left(\pi, \frac{\pi(1 - \pi)}{n}\right). \tag{2.7}
$$

This is the argument for quantifying how accurate \( X_n/n \) is as an estimator of \( \pi \) in a statistical sense. 

### Example 2.3 (Opinion polls: margin of error (confidence interval))

Opinion polls are typically conducted with sample sizes like \( n = 1000 \) or \( n = 3000 \) from a large population such as all adult Canadians. Often, the results will be qualified with a statement like, “These results have a margin of error of 3 percentage points 19 times out of 20.” Let’s see how such a statement can be justified. For definiteness, take the Nanus poll taken in September 2016 commissioned by Clean Energy Canada (available at [this link](http://cleanenergycanada.org/wp-content/uploads/2016/09/Clean-Energy-Canada-Nanos-Climate-Policy-Polling-Report-Oct-2016.pdf)). It asked 1000 randomly selected Canadian adults a number of questions about climate change. The findings included:

- 48% agreed with the statement, “A changing climate presents a significant threat to our economic future” (and a further 23% somewhat agreed). 
- 33% supported, “Having a price on carbon to reduce the use of fossil fuels such as coal, oil or natural gas” (and a further 26% somewhat supported the statement). 

In the methodology section of the report, we find, “The margin of error is ±3.1 percentage points 19 times out of 20.” The margin of error is a measure of sampling variability. Thus, to check the calculation, we treat the sample as a random sample from a large population. Then, the number of people agreeing with a particular statement (e.g., the question about significant threat to our economic future) is a binomial random variable with \( n = 1000 \) (the sample size here) and probability \( \pi. \) The parameter \( \pi \) represents the unknown proportion of people in the population who agree with this particular statement. The Nanos poll was stratified by age, gender, and region and not a simple random sample, which implies our binomial model probability is oversimplified. Nonetheless, the impact on the margin of error calculation is usually small. 

The approximate distribution of \( X_n/n \) in (2.7) implies that approximately 

$$
\frac{X_n - \pi}{\sqrt{n}} \sim N(0, \frac{\pi(1 - \pi)}{n}). 
$$

On the left is the error in estimating \( \pi \) by \( X_n/n \). The normal distribution has the property that 95% of the probability (“19 times out of 20”) lies within ±1.96 standard deviations of the mean. Thus, the error is within

$$
\pm 1.96 \sqrt{\frac{\pi(1 - \pi)}{n}} \tag{2.8}
$$

approximately 19 times out of 20. There are two further practical difficulties in completing the computation.

- What value should be used for \( \pi \) in the error calculation? Recall that the purpose of the poll is to estimate \( \pi, \) which is unknown. 

- Most polls, like the Nanos poll, ask several questions. Each question could have a different true value of \( \pi. \) It would be overly complicated to give a different error calculation for every question. 

To overcome both of these difficulties, pollsters will often report (2.8) for \( \pi = 0.5. \) This is the value of \( \pi \) that maximizes the variance in the approximate normal distribution of the error and hence gives the widest, worst-case bounds on the margin of error. 

Returning to the Nanos poll, with \( n = 1000 \) the worst-case margin of error from (2.8) is

$$
\pm 1.96 \frac{\sqrt{0.5(1 - 0.5)}}{\sqrt{1000}} = \pm 1.96(0.0158) = \pm 0.031,
$$

i.e., 3.1%, which is the margin of error reported. 

♢♢♢

Error bounds like those in Example 2.3 are also called confidence intervals and are tackled more generally in Section 4.6. 

### 2.5.3 Central limit theorem

The normal approximation to the binomial distribution is just a special case of the central limit theorem (CLT). 

**Theorem 2.2 (Central limit theorem (CLT))**  
Let \( Y_1, Y_2, \ldots \) be a sequence of IID random variables with mean \( \mu, \) variance \( \sigma^2, \) and MGF defined in a neighborhood of zero. Define the sum 

$$
X_n = \sum_{i=1}^{n} Y_i.
$$

The standardized sum,

$$
Z_n = \frac{X_n - n\mu}{\sqrt{\sigma^2 n}} \tag{2.9}
$$ 

converges in distribution to \( N(0, 1). \) Referring back to Definition 2.1 for convergence in distribution, the CLT says that the CDF of \( Z_n \) approaches that of the standard normal as \( n \to \infty, \) i.e., 

$$
P(Z_n < z) \to P(Z < z), 
$$ 

where \( Z \sim N(0, 1). \) This is sufficient for statistical purposes: in Example 2.3, for instance, the limits for the 95% confidence interval use \( z_{0.975} = 1.96, \) a quantile of the standard normal defined by the CDF. Note, however, that the speed of convergence will be slower in the extreme tails of the \( Z_n \) distribution.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 2.6 GETTING IT DONE IN R

### 2.6.1 Sample mean, standard deviation, and variance

The functions `mean`, `sd`, and `var` are useful for obtaining the sample mean, standard deviation, and variance, respectively. 

### 2.6.2 Quantiles of the t distribution

R has functions to compute quantiles for commonly used distributions. Corresponding to the functions in Table 1.9 with names starting with `d` for PMFs and PDFs, names starting with `q` compute quantiles. For instance, to compute a confidence interval in the lung-function study of Example 2.1, quantiles of the \( t \) distribution are computed by `qt`.

```R
> qt(p = 0.025 , df = 33)
[1] -2.034515
> qt(p = 0.975 , df = 33)
[1] 2.034515
```

Here, \( p \) is the probability to the left of the quantile, and there are 33 degrees of freedom because \( n = 34 \) in the particular study. Whereas `pt(y, ...)` returns a CDF probability for a given value or quantile of a random variable with a \( t \) distribution, the function `qt(p, ...)` returns a quantile for a given probability. Thus, the quantile function is the inverse cumulative distribution function. In general, for given probability \( p, \) the quantile function returns \( y \) such that \( P(Y \leq y) = F_Y(y) = p, \) or equivalently \( y = F^{-1}(p), \) where \( F^{-1} \) is the inverse function of the CDF. 

### 2.6.3 Limiting normal distributions

Similarly, in Example 2.3 we needed quantiles of the standard normal distribution, which are available from `qnorm`. 

```R
> qnorm(p = 0.025)
[1] -1.959964
> qnorm(p = 0.975)
[1] 1.959964
```

Quantiles of the normal distribution with non-standard mean and variance are obtained via the arguments `mean` and `sd` of `qnorm`. 

## 2.7 LEARNING OUTCOMES

On completion of this chapter you should be able to demonstrate the following skills. 

1. Normal distribution
   (a) Use the MGF to derive the mean, variance, and distribution of a linear function of a normal random variable. (You can interpret “derive” here as justify via an appropriate result.)
   (b) Derive the mean, variance, and distribution of a linear combination of normal random variables. 
   (c) Standardize a normal random variable to have a standard normal distribution. 

2. \( \chi^2 \) distribution
   (a) Derive the MGF of the \( \chi^2_1 \) distribution. 
   (b) Show via the MGF that the square of a standard normal random variable has a \( \chi^2_1 \) distribution. 
   (c) Find the MGF of the \( \chi^2_d \) distribution. 
   (d) Show that the sum of squares of \( d \) independent standard normal random variables has a \( \chi^2_d \) distribution. 

3. Random sample from a normal distribution
   Let \( Y_1 , \ldots , Y_n \) be a random sample of independent \( N(\mu, \sigma^2) \) random variables.
   (a) Derive the mean and variance of the sample mean, \( \bar{Y}. \) 
   (b) Write down unstandardized and standardized distributions of \( \bar{Y} \) when \( \sigma^2 \) is known. 
   (c) Write down the distribution of the sample variance, \( S^2. \) 
   (d) Show that the sample mean and sample variance are statistically independent. 
   (e) Write down a standardized version of \( \bar{Y} \) when \( \sigma^2 \) is unknown. Argue that the standardized random variable has the properties leading to a \( t \) distribution with specified degrees of freedom. 
   (f) Use the \( t \) distribution to compute a confidence interval for \( \mu \) when \( \sigma^2 \) is unknown for given data. 

4. Central Limit Theorem
   (a) Apply the CLT to establish convergence in distribution to the standard normal for a random variable with a specified distribution (e.g., binomial). Included here is the formulation of the random variable as a sample mean or sample sum, standardizing it, and checking the conditions of the CLT. A detailed proof of the theorem is not expected. 
   (b) Under a binomial probability model, convert the standard normal distribution of a standardized version of the sample proportion as \( n \to \infty \) to an approximate normal distribution of the unstandardized sample proportion and a finite sample size. 
   (c) Compute the “margin of error” in estimating the parameter \( \pi \) in the binomial distribution for given data.

5. Explanation
   Explain your reasoning by describing the results you are using, along with any assumptions that are necessary. 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## Exercises

**Exercise 2.1**  
Let \( Y \sim N(\mu, \sigma^2) \). Show that the standardized random variable \( Z = (Y - \mu)/\sigma \) has a \( N(0, 1) \) distribution.

**Exercise 2.2**  
Let \( Y_1 , \ldots , Y_n \) be independent \( N(\mu, \sigma^2) \) random variables. 
1. Write down the MGF of \( Y_i. \) 
2. Derive the MGF of \( Y_1 + \cdots + Y_n. \) 
3. Hence, derive the MGF of \( \bar{Y} = (Y_1 + \cdots + Y_n)/n. \) 
4. Hence, derive the MGF of \( Z = (\bar{Y} - \mu)/(\sigma/\sqrt{n}) \) and identify its distribution. In parts 2–4, you may use without proof general properties in Chapter 1 on MGFs. When you use a property, however, remember to state it, make clear how it is being applied, and check any assumptions required for the result. 

**Exercise 2.3**  
Let \( Y \sim \chi^2_1 \). Show that the MGF of \( Y \) is \( (1 - 2t)^{-1/2}. \) 

**Exercise 2.4**  
[Quiz #1, 2010-11, Term 2, except that showing “Var(Z^2) = 2” was not included]  
Let \( Z \) have a standard normal distribution with expectation 0 and variance 1, i.e., \( Z \sim N(0, 1). \) 
1. Write down the definition of \( M_{Z^2}(t), \) the moment generating function (MGF) of \( Z^2. \) 
2. From the definition, show \( M_{Z^2}(t) = (1 - 2t)^{-1/2}. \) 
3. Use \( M_{Z^2}(t) \) to show that \( E(Z^2) = 1 \) and \( Var(Z^2) = 2. \) 
4. Argue that the distribution of \( Z^2 \) is \( \chi^2_1. \) 

**Exercise 2.5**  
Show that the MGF of a random variable with a \( \chi^2_d \) distribution is \( (1 - 2t)^{-d/2}. \)

**Exercise 2.6**  
[Quiz #1, 2011-12, Term 1, except that part 5 was not included]  
Let \( Z_1 , \ldots , Z_d \) be \( d \) independent \( N(0, 1) \) random variables, and let

$$
Y = Z_1^2 + \cdots + Z_d^2.
$$ 

You may use without proof the result that \( Z_i^2 \sim \chi^2_1 \) for \( i = 1, \ldots, d, \) and that the moment generating function (MGF) of the \( \chi^2_1 \) distribution is \( (1 - 2t)^{-1/2} \) (see Exercise 2.4).
```