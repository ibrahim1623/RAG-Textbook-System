```markdown
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 2.8. EXERCISES

### 2-23
1. Write down the definition of \( M_Y(t) \), the MGF of \( Y \).
2. Show that the MGF of \( Y \) is \( (1 - 2t)^{-d/2} \), either directly starting from the definition or by stating and applying an appropriate result. In either case be sure to explain the assumption(s) you are using.
3. Hence, what is the distribution of \( Y \)? Explain briefly.
4. From the MGF find \( E(Y) \).
5. From the MGF find \( \text{Var}(Y) \).

### Exercise 2.7
Let \( X_1 \) and \( X_2 \) have independent \( \chi^2 \) distributions with degrees of freedom \( d_1 \) and \( d_2 \), respectively. Show that \( X_1 + X_2 \) has a \( \chi^2_{d_1 + d_2} \) distribution.

### Exercise 2.8
Let \( Y_1, \ldots, Y_n \) be independent random variables with mean \( \mu \) and variance \( \sigma^2 \), and let \( \bar{Y} = \frac{1}{n} \sum_{i=1}^n Y_i \).
1. Show that the covariance between \( \bar{Y} \) and \( Y_i - \bar{Y} \) is zero.
2. Assume also that \( Y_1, \ldots, Y_n \) are normally distributed. Are \( \bar{Y} \) and \( Y_i - \bar{Y} \) independent? Why?

### Exercise 2.9
Let \( Y_1, \ldots, Y_n \) be independent random variables, each with mean \( \mu \) and variance \( \sigma^2 \). The values of \( \mu \) and \( \sigma^2 \) are both unknown. Consider the sum of squares
\[
X = \sum_{i=1}^n (Y_i - \bar{Y})^2 = \sum_{i=1}^n Y_i^2 - n\bar{Y}^2.
\]
1. Show that \( E(X) = (n - 1)\sigma^2 \).
2. Hence give an estimator of \( \sigma^2 \) based on \( X \) that has expectation \( \sigma^2 \).

### Exercise 2.10
In this exercise we calculate further confidence intervals for the study in Example 2.1. Recall that Schlaich et al. (1998) collected data on adjusted forced expiratory volume for \( n = 34 \) patients with manifest osteoporosis. The data summaries for the sample are:
\[
\bar{y} = 94.3 \quad \text{and} \quad s = 14.7,
\]
where the units are percentage points. As before, we will assume that the \( n = 34 \) data values are a random sample from a \( N(\mu, \sigma^2) \) distribution, and that the objective is to estimate \( \mu \).

1. Compute 90% and 99% confidence intervals for \( \mu \) based on Student’s t distribution. What are their widths?
2. Before Student derived the t distribution, common practice was to carry out calculations as above using the standard normal distribution rather than the t distribution.
   (a) Use R to plot the PDF of the standard normal for values in the range \([-4, 4]\). You can set up such a grid of values at spacing of 0.01 using
   ```R
   x <- seq(-4, 4, by = 0.01)
   ```
   When you use `plot` with \( x \) on the x-axis and the corresponding values of the normal PDF on the y-axis, include the argument `type = "l"` to tell R to join the coordinates as lines to create a curve.
   (b) Add the PDF of the t distribution (with appropriate degrees of freedom) to your plot. Using `lines` rather than `plot` will add to the current plot rather than generating a new one. To distinguish the two curves, the argument `lty = 2` will make the new curve from dashed lines.
   (c) Comment on how well the standard normal approximates the t distribution here.
3. Recompute the 90% and 99% confidence intervals in part 1 but use the standard normal rather than the t distribution. What are their widths?
4. How much wider are the confidence intervals using the t distribution relative to those using the standard normal? (“Relative” here is a ratio of widths.)
5. Look again at your plots of the standard normal and t PDFs. Why is there more discrepancy in the confidence interval from the t distribution relative to the normal distribution as the confidence level increases?

### Exercise 2.11
Example 2.1 analyzed data collected by Schlaich et al. (1998) on lung function in patients with manifest osteoporosis. The investigators also collected data on a second sample of \( n = 51 \) patients without manifest osteoporosis. The second sample is a “control” group for comparison. The definition of the measure \( \text{FEV}_1\% \) we will use for the control group is the same as in Example 2.1 and is again called \( y \). The control sample gives the following data summaries:
\[
\bar{y} = 96.1 \quad \text{and} \quad s = 14.4,
\]
where \( s \) is the sample standard deviation. We will again assume the data are a random sample from a normal distribution and that interest centers on estimation of the mean of the distribution.
1. Based on the above description, write down a formal probability model for the way that the control-sample data, \( y_1, \ldots, y_{51} \), arose. Be sure to specify:
   (a) the random variable(s);
   (b) the distribution of the random variable(s);
   (c) a description of any parameters of the distribution;
   (d) any other assumption(s) about the random variable(s).
2. Assuming the probability model holds, calculate:
   (a) an estimate of the mean of the distribution;
   (b) an estimate of the standard deviation of the sample mean over repeated samples;
   (c) a 95% confidence interval for the mean of the assumed distribution.
3. Again assuming the probability model is correct, are there any approximations in the confidence-interval calculation? Briefly explain why or why not.
4. Compare the confidence intervals in Example 2.1 and in this exercise, and comment briefly.

### Exercise 2.12
[Parts 1–5 appeared on Quiz #1, 2010-11, Term 2] Suppose a random sample of size \( n = 2 \) is drawn from a \( N(\mu, \sigma^2) \) distribution to estimate \( \mu \) when \( \sigma^2 \) is unknown. There is a big impact on the 95% confidence interval for \( \mu \) from using the t distribution instead of the standard normal.
```
> qnorm(0.975)
[1] 1.959964
> qt(0.975, df = 1)
[1] 12.7062
```
Thus, a confidence interval for \( \mu \) based on the t distribution will be much, much wider. Why? And why does the t distribution have 1 degree of freedom here (and not 2 from \( n = 2 \))? The exercise sheds some light on these questions. Let \( Y_1 \) and \( Y_2 \) be independent random variables sampled from a \( N(\mu, \sigma^2) \) distribution. For such a sample of size \( n = 2 \) it is easily shown that the sample variance,
\[
S^2 = \frac{1}{n-1} \sum_{i=1}^n (Y_i - \bar{Y})^2,
\]
simplifies to
\[
S^2 = \left(\frac{Y_1 - Y_2}{\sqrt{2}}\right)^2.
\]
You may use this result without proof.
1. Let \( V = \frac{Y_1 - Y_2}{\sqrt{2}} \). Show the following properties of \( V \). Carefully state any result you are using (no proof of the result required).
   (a) \( E(V) = 0 \).
   (b) \( \text{Var}(V) = \sigma^2 \).
   (c) \( V \) has a normal distribution.
2. Explain why the distribution of \( \frac{V}{\sigma} \) is standard normal.
3. Hence argue that when \( n = 2 \), the distribution of \( \frac{S^2}{\sigma^2} \) is \( \chi^2_1 \). (A result on the connection between \( N(0, 1) \) and \( \chi^2_1 \) random variables may be stated and used without proof.)
4. Using (without proof) the properties of the \( \chi^2_1 \) distribution, what are the expectation and variance of \( \frac{S^2}{\sigma^2} \) when \( n = 2 \)?
5. Hence, what is the expectation of \( S^2 \) when \( n = 2 \)?
6. What is the variance of \( S^2 \) when \( n = 2 \)?
7. Use `qchisq` in R to find quantiles \( l \) and \( u \) such that
\[
\Pr\left(\frac{S^2}{\sigma^2} < l\right) = 0.025 \quad \text{and} \quad \Pr\left(\frac{S^2}{\sigma^2} > u\right) = 0.025.
\]
Hence, \( l \) and \( u \) are lower and upper bounds on \( \frac{S^2}{\sigma^2} \) in the sense that
\[
\Pr(l < \frac{S^2}{\sigma^2} < u) = 0.95.
\]
8. Suppose \( S^2 \) is used to estimate \( \sigma^2 \) from a sample of size \( n = 2 \). Comment on the values of \( \frac{S^2}{\sigma^2} \) that could occur.

### Exercise 2.13
[Parts 1–3 appeared on the final exam, 2010-11, Term 1.] Let \( Y_1, \ldots, Y_n \) be independent \( N(\mu, \sigma^2) \) random variables. Their sample variance is
\[
S^2 = \frac{1}{n - 1} \sum_{i=1}^n (Y_i - \bar{Y})^2.
\]
This question explores the properties of \( \frac{S^2}{\sigma^2} \) and why the \( t_{n-1} \) distribution approaches the standard normal as \( n \to \infty \). Section 2.4.2 argued that \( \frac{S^2}{\sigma^2} \) has the same distribution as \( \frac{X}{n - 1} \), where \( X \sim \chi^2_{n-1} \). You may use this result and properties of the \( \chi^2 \) distribution without proof.
1. Find \( E\left(\frac{S^2}{\sigma^2}\right) \).
2. Find \( \text{Var}\left(\frac{S^2}{\sigma^2}\right) \).
3. Let \( \epsilon > 0 \) be a fixed constant representing an arbitrarily small “error”.
   (a) As \( n \to \infty \), what is the limiting probability
   \[
   \Pr(1 - \epsilon < \frac{S^2}{\sigma^2} < 1 + \epsilon)?
   \]
   (b) Briefly describe how you would justify the limiting probability (a complete proof is not required).
4. In Section 2.4.3 the sample mean was standardized by its expectation and sample variance and then expanded in equation (2.4):
\[
\frac{\bar{Y} - \mu}{S/\sqrt{n}}.
\]
It was shown that this quantity has a \( t_{n-1} \) distribution. As \( n \to \infty \), it is known that the \( t_{n-1} \) distribution converges to \( N(0, 1) \). Use the above results to justify this convergence.

### Exercise 2.14
Let \( X \) have a \( \chi^2_d \) distribution. Show that a standardized version of \( X \) has a limiting standard normal distribution as \( d \to \infty \). Be sure to be specific about the standardization of \( X \) and to check the conditions of any result on limiting distribution that you use.

### Exercise 2.15
This exercise demonstrates the CLT via simulation.
1. In R, generate a sample of 1000 independent \( \text{Unif}(-1, 1) \) random variables.
```R
n <- 1000
x <- runif(n, min = -1, max = 1)
```
Take a look at the first 10 elements of the vector \( x \) that contains the sample using `x[1:10]`, and make sure they look good. For example, all values should be in \([-1, 1]\)!
2. Use `hist` to draw a histogram of all the data in \( x \). Look at `help(hist)` to find out how to do this.
3. Compute the sample mean and sample variance of the data. Compare with the theoretical mean and variance of the \( \text{Unif}(-1, 1) \) distribution. Why do the sample and theoretical quantities not agree exactly?
4. Generate a second, independent sample
```R
y <- runif(n, min = -1, max = 1)
```
and then compute the sums \( z[1] = x[1] + y[1] \), \( z[2] = x[2] + y[2] \), etc. using
```R
z <- x + y
```
Note that R will apply the sum operator element-wise to the vectors. Take a look at the first few elements of \( x \), \( y \), \( z \) to make sure the summation has worked correctly. Thus, \( z \) contains 1000 values, where each element is generated as the sum of a sample of two independent \( \text{Unif}(-1, 1) \) random variables.
5. Draw a histogram of the sample data in \( z \). Does the histogram look more normal than a single sample from the uniform distribution?
6. Repeat Steps 4–5 to generate a total of 5 independent samples, and compute \( z \) as the sum across all 5 vectors. Does the histogram of \( z \) have a shape that looks fairly normal?
7. Why do the \( z \) values not appear to be from a standard normal distribution? What would we have to do to the \( z \) values to standardize them?

### Exercise 2.16
Throughout this question, whenever you use a general result, make sure you state it clearly and check its conditions (if any).
1. Let \( U \sim \text{Unif}(-1, 1) \), i.e., \( U \) has a uniform distribution with parameters \( a = -1 \) and \( b = 1 \) in Table 1.4.
   (a) From the definition of expectation, find \( E(U) \).
   (b) From the definition of variance, find \( \text{Var}(U) \).
   (c) From the definition of the moment generating function, find \( M_U(t) \).
   (d) From the moment generating function, find \( E(U) \) and \( \text{Var}(U) \). (As in Example 1.29, you may find it easier to expand the exponential functions, collect leading terms, then differentiate.)
2. Let \( U_1, \ldots, U_n \) be independent \( \text{Unif}(-1, 1) \) random variables. Consider the random variable
\[
Y = \sum_{i=1}^n U_i.
\]
(a) What is \( E(Y) \)?
(b) What is \( \text{Var}(Y) \)?
(c) What is the MGF of \( Y \)?
3. Now standardize \( Y \) to find a new random variable, \( Z \), with mean 0 and variance 1.
   (a) What is \( Z \)?
   (b) What is the MGF of \( Z \)?
   (c) What is the MGF of \( Z \) as \( n \to \infty \)? One approach is to expand the exponential functions and collect terms before taking the limit. Note also that \( (1 + a/n)^n \to e^a \) as \( n \to \infty \).
   (d) What is the distribution of \( Z \)?
   (e) You have just proved a special case of a more general theorem. What is it?

### Exercise 2.17
Example 2.2 worked through the normal approximation to \( X_n \), a \( \text{Bin}(n, \pi) \) random variable. It was shown that
\[
Z = \frac{X_n - n\pi}{\sqrt{n\pi(1 - \pi)}}
\]
is approximately \( N(0, 1) \) for large \( n \). Here, \( X_n \) is a discrete random variable, whereas \( Z \) is continuous. How can a random variable with a discrete PMF be approximated by another with a continuous PDF?

### Exercise 2.18
[This exercise appeared on Quiz #1, 2011-12, Term 1 without Parts 3 and 5. The quiz included the fact that the R function `qnorm(0.975)` returns 1.959964.] Let \( Y_1, \ldots, Y_n \) be independent random variables, each with mean \( \mu \) and variance \( \sigma^2 \). Note that we are not necessarily assuming any distribution for the \( Y_i \) yet. Consider using 
\[
\bar{Y} = \frac{1}{n}  \sum_{i=1}^n Y_i
\]
to estimate \( \mu \). 
1. Show that \( E(\bar{Y}) = \mu \).
2. Show that \( \text{Var}(\bar{Y}) = \frac{\sigma^2}{n} \).
3. What does Chebyshev’s inequality give for the probability \( \Pr(|\bar{Y} - \mu| > \epsilon) \), where \( \epsilon = \frac{1.96\sigma}{\sqrt{n}} \)?
4. What does the CLT say about the distribution of \( \bar{Y} \) as \( n \to \infty \)?
5. Give an approximation based on the CLT to \( \Pr(|\bar{Y} - \mu| > \epsilon) \), where \( \epsilon = \frac{1.96\sigma}{\sqrt{n}} \). Explain briefly.
6. Suppose \( Y_1, \ldots, Y_n \) also have a normal distribution.
   (a) What is the distribution of \( \bar{Y} \)? Explain briefly.
   (b) What is \( \Pr(|\bar{Y} - \mu| > \epsilon) \), where \( \epsilon = \frac{1.96\sigma}{\sqrt{n}} \)? Explain briefly.
   (c) Is the calculated probability a large-sample approximation? Explain briefly.

### Exercise 2.19
Example 2.2 argued that a standardized version of a binomial random variable has a limiting standard normal distribution as \( n \to \infty \). Outline the key steps in the argument, pointing to results that would be used, without tedious algebraic detail. For instance, you might start with:
**Step 1.** Let \( X_n \sim \text{Bin}(n, \pi) \). Its MGF, \( M_{X_n}(t) \), can be obtained from Table 1.3. In other words, there is no need to derive \( M_{X_n}(t) \) for this first step. Indeed, there is no need even to give an explicit expression for \( M_{X_n}(t) \) as you will not be manipulating it algebraically in subsequent steps. On the other hand, you will need to define carefully and mathematically various terms like \( M_{X_n}(t) \) as you go along, just to make your argument clear.

### Exercise 2.20
This exercise explores the shape of the Poisson distribution, via simulation and via a limiting-distribution argument.
1. Using `rpois` in R, generate a random sample of 1000 values from a \( \text{Pois}(\mu = 0.35) \) distribution and plot the values using `hist`. Does the empirical distribution have a roughly normal shape?
2. Repeat part 1 but sample from a \( \text{Pois}(\mu = 25) \) distribution.
3. What do the two simulations suggest about the condition(s) for the normal distribution to be a good approximation to the Poisson distribution?
4. Let \( Y \sim \text{Pois}(\mu) \). The standardized variable 
\[
Z = \frac{Y - \mu}{\sqrt{\mu}}
\]
has mean 0 and variance 1. The MGF of \( Z \) can be written as
\[
M_Z(t) = \exp\left(\frac{t^2}{2\mu} + O\left(\frac{1}{\mu}\right)\right).
\]
The notation \( O\left(\frac{1}{\mu}\right) \) says that, for any \( t \), the sum of all terms after the \( t^2 \) term becomes negligible for sufficiently large \( \mu \). Also, see the last part of this question for the derivation of the expansion here. What is the limiting distribution of \( Z \) as \( \mu \to \infty \)?

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

```
