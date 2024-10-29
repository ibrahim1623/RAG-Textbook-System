```markdown
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 1.8. MOMENT GENERATING FUNCTIONS

1-39

In other words, if we can find the MGF of a random variable, and this MGF is on a list of MGFs we have computed (as in Tables 1.3 and 1.4), we can use the MGF to tell us the random variable’s distribution. The MGF is thus a mathematical “fingerprint” for a distribution. A human fingerprint can identify a person on a list of suspects already fingerprinted. However, if the fingerprint belongs to a person not on the list of suspects, identification is not possible. It is similarly difficult to work backwards from an MGF to its distribution without a list of suspect distributions with MGFs like those in Tables 1.3 and 1.4. Fortunately, those tables suffice for most of our needs in this book. Billingsley (2012, Sections 9 and 30) gives several proofs of Theorem 1.3, for discrete random variables and more generally. The essence of the general argument is that, if the open-interval condition of the lemma is satisfied, a probability distribution is determined by its moments, which are in turn determined by the MGF. We use Theorem 1.3 in the following examples to find various distributions of random variables derived from a linear function of a random variable or a sum of independent random variables.

## Example 1.30 (Normal distribution: linear function)

Let \( Y \) have a \( N (\mu, \sigma^2) \) distribution, and let \( Z = a + bY \). From the MGF of \( Y \) in (1.14), the MGF of \( Z \) is 

\[
M_Z(t) = e^{at} M_Y(bt) = e^{at}e^{\mu(bt) + \frac{1}{2} \sigma^2 (bt)^2} = e^{(a + b\mu)t + \frac{1}{2} b^2 \sigma^2 t^2}.
\]

This has the form of the MGF in (1.14) for a normal random variable, except that the mean \( \mu \) is replaced by \( a + b\mu \), and the variance \( \sigma^2 \) is replaced by \( b^2 \sigma^2 \). Thus, \( Z \) is identified to have a \( N (a + b\mu, b^2 \sigma^2) \) distribution. ♢♢♢

## Example 1.31 (Exponential distribution: sum of IID random variables)

Let \( Y_1, \ldots, Y_\nu \) be \( \nu \) IID \( \text{Expon} (\lambda) \) random variables. Note they have the same value of the parameter \( \lambda \). Thus, from (1.12) each \( Y_i \) has MGF \( \frac{\lambda}{\lambda - t} \). Their sum, \( Y \), has MGF 

\[
M_Y(t) = \left( \prod_{i=1}^{\nu} \frac{\lambda}{\lambda - t} \right) =  \frac{\lambda^\nu}{(\lambda - t)^\nu}.
\]

This was shown to be the MGF of a \( \Gamma (\nu, \lambda) \) random variable in Example 1.23. Thus, the sum of independent exponential random variables with the same value of \( \lambda \) follows a gamma distribution. ♢♢♢

## Example 1.32 (Normal distribution: sum of independent random variables)

Let \( Y_1 \) and \( Y_2 \) be independent normal random variables. \( Y_1 \) has mean \( \mu_1 \) and variance \( \sigma_1^2 \); similarly, \( Y_2 \) has mean \( \mu_2 \) and variance \( \sigma_2^2 \). The MGFs of \( Y_1 \) and \( Y_2 \) are available from (1.14). The sum \( X = Y_1 + Y_2 \) has MGF 

\[
M_X(t) = M_{Y_1}(t)M_{Y_2}(t) = e^{\mu_1 t + \frac{1}{2} \sigma_1^2 t^2} e^{\mu_2 t + \frac{1}{2} \sigma_2^2 t^2} = e^{(\mu_1 + \mu_2)t + \frac{1}{2} (\sigma_1^2 + \sigma_2^2) t^2}.
\]

This is seen to be the MGF of a normal random variable with mean \( \mu_1 + \mu_2 \) and variance \( \sigma_1^2 + \sigma_2^2 \). Thus, we have shown that the sum of two independent normal random variables is also normal. By repeating the argument, the obvious extension of the result holds for the sum of \( n \) independent normal random variables. (The result also holds more generally for \( n \) random variables following a multivariate normal distribution, a generalization of the bivariate normal in Section 1.7.9, even if they are not independent. Their sum or a linear combination of them has a normal distribution. When computing the variance of the sum or linear combination via (1.10), the covariance terms will have to be included.) ♢♢♢

## Example 1.33 (Casualty insurance: sum of IID geometric random variables)

An actuary models the distribution of the number of months to the first claim for drivers insured in a particular high-risk rating class. She uses a geometric distribution, i.e., \( \text{Geom}_1(\pi) \), where \( \pi \) is the probability of at least one claim in a month. A \( \text{Geom}_1(\pi) \) random variable, \( Y \), has probability mass function 

\[
f_Y(y) = (1 - \pi)^{y-1} \pi \quad (y = 1, 2, \ldots, \infty; \, 0 < \pi < 1),
\]

expectation \( \frac{1}{\pi} \), and variance \( \frac{1 - \pi}{\pi^2} \). Its MGF is 

\[
M_Y(t) = \frac{e^t \pi}{1 - (1 - \pi)e^t} \quad \text{(see Exercise 1.22 or Table 1.3).}
\]

Suppose the actuary is interested in the distribution of the number of months to the second claim. She assumes that the distribution arises as \( X = Y_1 + Y_2 \), where \( Y_1 \) and \( Y_2 \) are independent \( \text{Geom}_1(\pi) \) random variables. (This ignores the possibility of more than one claim in a month.) What is the distribution of \( X \)? From Lemma 1.3,

\[
M_X(t) = M_{Y_1}(t)M_{Y_2}(t) = \left( \frac{e^t \pi}{1 - (1 - \pi)e^t} \right)^2.
\]

This is the MGF of a negative-binomial random variable (again see Exercise 1.22 or Table 1.3) with parameters \( n = 2 \) and \( \pi \), i.e., \( X \sim \text{NegBin}(2, \pi) \). Table 1.3 gives the PMF of the negative-binomial distribution in general. With \( n = 2 \) and, say, \( \pi = 0.1 \), the first few numerical values of the PMF are given in Table 1.8.

# 1.9 GETTING IT DONE IN R

In later chapters of this book we have to compute PDFs, PMFs, and CDFs for a variety of distributions, such as those in Tables 1.3 and 1.4. R can compute these quantities for all commonly used distributions. 

( )
\[
f_X(x) = \frac{x - 1}{(1 - \pi)^{x - 2} \pi^2} \quad (x = 2, 3, \ldots)
\]
et cetera.

**Table 1.8:** Probability mass function of a negative-binomial random variable with \( n = 2 \) and \( \pi = 0.1 \)

| \( \text{Distribution} \) | \( \text{R function} \) | \( \text{Arguments and defaults} \) |
|-----------------|--------------------|--------------------|
| Discrete distributions |                     |                     |
| Binomial | `dbinom(x, size, prob)` | |
| Geometric | `dgeom(x, prob)` | |
| Negative binomial | `dnbinom(x, size, prob)` | |
| Poisson | `dpois(x, lambda)` | |
| Continuous distributions |                     |                     |
| Beta | `dbeta(x, shape1, shape2)` | |
| \( \chi^2 \) | `dchisq(x, df)` | |
| Exponential | `dexp(x, rate = 1)` | |
| Fisher’s F | `df(x, df1, df2)` | |
| Gamma | `dgamma(x, shape, rate = 1)` | |
| Normal | `dnorm(x, mean = 1, sd = 1)` | |
| Student’s t | `dt(x, df)` | |
| Uniform | `dunif(x, min = 0, max = 1)` | |

**Translation into our notation**

| Distribution | R function | Translation |
|--------------|------------|-------------|
| Binomial (n = size, π = prob) | Bin (n = size, π = prob) | 
| Geometric | Geom0 (π = prob) | See text |
| Negative binomial | | |
| Poisson | Pois (µ = lambda) | |
| Beta | Beta (a = shape1, b = shape2) | |
| \( \chi^2 \) | \( \chi^2(d = df) \) | |
| Exponential | Expon (λ = rate) | |
| Fisher’s F | F(d1 = df1, d2 = df2) | |
| Gamma | Gamma (ν = shape, λ = rate) | |
| Normal | N (µ = mean, σ² = sd²) | |
| Student’s t | t(d = df) | |
| Uniform | Unif (a = min, b = max) | |

**Table 1.9:** R functions for the PMF or PDF of some common distributions

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

Table 1.9 lists the R functions to compute the PMF or PDF of the distributions in Tables 1.3 and 1.4. In all cases, the argument \( x \) is the value of a random variable \( X \). The table also translates the R arguments into our notation for a particular distribution and its parameter(s). In most cases, R’s syntax and our notation agree well, and \( X \) in Table 1.9 has the same distribution as the random variable \( Y \) in Table 1.3 or 1.4. There are a few exceptions, however. 

1. R has no function corresponding to the \( \text{Geom}_1(\pi) \) distribution, the version of the geometric distribution with range \( y = 1, 2, \ldots, \infty \). If \( X \) is a \( \text{Geom}_0(\pi) \) random variable, then \( Y = X + 1 \) is \( \text{Geom}_1(\pi) \) random variable, however, and hence the PMF of \( Y \) is given by `dgeom(x = y - 1, prob)`, which could be called for values \( y \geq 1 \). 

2. R’s negative-binomial distribution for \( X \) is defined by the PMF 

\[
f_X(x) = \frac{x+n−1}{(1−\pi)^x \pi^n} \quad (x = 0, 1, \ldots, \infty),
\]

whereas \( Y \) in Table 1.3 has PMF 

\[
f_Y(y) = (1−\pi)^{y−n} \pi^n \quad (y = n, n + 1, \ldots, \infty).
\]

Again, there is a simple relationship, and \( Y \) and \( n + X \) have the same distribution. Thus, `dnbinom(x = y - n, size, prob)` for \( y \geq n \) gives our negative-binomial PMF for \( Y \).

In addition, there is no R function for the Bernoulli distribution; it is a special case of the binomial with \( n = 1 \) (or size = 1). The functions in Table 1.9 are useful for sketching a PMF or PDF. For instance, the following R code plots \( f_Y(y) \) against \( y \) when \( Y \) has the t distribution with \( d = 10 \) degrees of freedom, to produce Figure 1.4.

```r
# Values of y at which to plot the PDF, namely -5, -4.99, ... , 5
y <- seq(-5, 5, by = 0.01)
# PDF for t distribution with 10 degrees of freedom
fy <- dt(y, df = 10)
# Plot fy against y using type = "l" to join the points with lines
plot(y, fy, xlab = "y", ylab = expression(f[Y](y)), type = "l")
```

The last line is perhaps more complicated than necessary, with `expression` and `[Y]` generating the subscript \( Y \) in the y-axis label. The simpler syntax 

```r
plot(y, fy, xlab = "y", ylab = "f(y)", type = "l")
```

would often suffice. (Type `demo(plotmath)` to demonstrate R’s capabilities to format mathematical expressions in text of plots.)

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 1.10 LEARNING OUTCOMES

The functions in Table 1.9 give a PMF or PDF, \( f_Y(y) \), but statistical calculations often require the CDF, \( F_Y(y) = Pr(Y ≤ y) \). For each PMF or PDF function, which has a name starting with `d`, there is a corresponding CDF function, which has a name starting with `p`. For instance, `ppois(y, lambda)` computes the CDF, \( Pr(Y ≤ y) \), of the Poisson distribution. 

```
> ppois(1, lambda = 2)
[1] 0.4060058
```

Here, `>` is the R prompt, and recall that \( \lambda \) is \( \mu \) in the \( \text{Pois} (\mu) \) distribution of Table 1.3. The calculation is easily verified:

\[
Pr(Y \leq 1) = Pr(Y = 0) + Pr(Y = 1) = \frac{e^{-\mu} \mu^0}{0!} + \frac{e^{-\mu} \mu^1}{1!} = e^{-\mu} (1 + \mu) = e^{-2} (1 + 2) = 0.4060058.
\]

Similarly, analogous to `dnorm(x, mean, sd)`, there is `pnorm(x, mean, sd)`, etc. 

# 1.11 EXERCISES

On completion of this chapter you should be able to demonstrate the following skills. They relate to the probability mass function (PMF) or probability density function (PDF), \( f_Y(y) \), of a random variable, \( Y \). 

1. Understand the relationship between a PMF or PDF and its CDF, including the interpretation of a PDF \( f_Y(y) \) as proportional to the probability that \( Y \) is in a small interval around \( y \).

2. From a given PMF or PDF of the random variable \( Y \), write down the definition of \( E(Y) \) and \( \text{Var}(Y) \). Simplify to a closed-form expression when readily available. 

3. From the PMF or PDF of \( Y \), write down the definition of the expectation of \( g(Y) \). Simplify to a closed-form expression when readily available. 

4. From the mean and variance of \( Y \), apply Chebyshev’s inequality to bound how far \( Y \) can deviate from its mean in a probabilistic sense. 

5. From the PDF of a random variable \( Y \), find the PDF of a monotonic function (transformation) of \( Y \). 

6. From the PMF or PDF of a random variable \( Y \), find the expectation of a function \( g(Y) \). 

7. From the joint distribution of two random variables, find their marginal and conditional distributions. 

8. Check whether two random variables are independent or not from their joint distribution. 

9. Find the covariance and correlation between two random variables. Interpret the correlation. 

10. Understand the relationship between covariance and independence. 

11. Find the expectation of a linear combination of several random variables from their individual expectations. As a special case, find the expectation of a linear function of a random variable from its expectation. 

12. Find the variance of a linear combination of several random variables from their individual variances and their pair-wise covariances. As a special case, find the variance of a linear function of a random variable from its variance. 

13. From the PMF or PDF of \( Y \), find its moment generating function (MGF). 

14. Check whether the MGF exists. 

15. From the MGF of a random variable, find the mean and variance. 

16. From the MGF of a random variable, \( Y \), find the MGF of \( a + bY \). 

17. From the (common) MGF of several independent random variables, find the MGF of their sum. 

18. Use the MGF of a random variable to identify its distribution.

19. Explain your reasoning. When using a result such as the expectation or variance of a linear function of a random variable or a linear combination of random variables as part of a longer derivation, briefly state the result you are using. If the result depends on an assumption such as statistical independence of random variables, remind the reader that you are using the assumption. 

Perhaps just as important in practice is a list of the tasks that would not be tested on the quizzes and final exam, or at least will receive less emphasis in grading. 

1. There is no doubt that facility with calculus, summation, and algebra is helpful for the mathematical manipulations in STAT 305. Nonetheless, STAT 305 is a course in probability and statistical inference, not mathematical manipulation. Thus, the formulation of, say, an expectation, is at least as important as the subsequent calculations to implement the final answer. 

2. Long proofs involving many steps will not be tested. On the other hand, simple derivations that can be done in a few lines may appear. Again, it is the demonstration of the use of appropriate probability and statistics tools to carry out the derivation that is most important. 

3. You are not expected to memorize specific PMFs, PDFs, and MGFs. You may put them on your formula sheet. If a PMF, PDF, or MGF is required to compute properties stemming from it, it will be given in the question. Similarly, you will not be asked, e.g., “find the mean of an exponential random variable” if the mean is required for subsequent calculations. You will be asked “to show that the mean is \( \frac{1}{\lambda} \)”.

## Exercise 1.1

Let \( Y \) be a normal random variable with mean 100 and variance \( 5^2 \) (i.e., standard deviation 5). 

1. Use `pnorm` in R to compute the following probabilities: \( Pr(90.0 < Y < 90.1) \), \( Pr(95.0 < Y < 95.1) \), and \( Pr(100.0 < Y < 100.1) \).
2. Use `dnorm` in R to compute the PDF of \( Y \) at the following values: \( y = 90.05 \), \( y = 95.05 \), and \( y = 100.05 \). (Note that these values are the midpoints of the intervals in part 1.)
3. Multiply each of the PDF values in part 2 by the width of the intervals used in part 1. What do you get? Hence, draw a picture illustrating the assertion, “For a given value of \( y \), the probability that \( Y \) falls in a small interval around \( y \) is approximately the PDF computed at \( y \) multiplied by the width of the interval.”

## Exercise 1.2

Let \( Y \) be an indicator random variable, i.e., with possible values 0 and 1. Show \( E(Y) = Pr(Y = 1) \). (Interchanging expectation and probability like this is a frequently used trick for indicator variables.)

## Exercise 1.3

In Section 1.3, two definitions were given for the variance of a random variable \( Y \):

\[
\text{Var}(Y) = E(Y - E(Y))^2
\]

and 

\[
\text{Var}(Y) = E(Y^2) - (E(Y))^2.
\]

Show that these two expressions are equivalent. 

## Exercise 1.4

Let \( Y \sim \text{Pois}(\mu) \). 

1. Show that \( E(Y) = \mu \). Hint: You can rewrite the sum in the expectation to include the factor 

\[
\sum_{y=0}^{\infty} \frac{\mu^y}{y!} = e^\mu.
\]

This factor will cancel. 
2. Show that \( \text{Var}(Y) = \mu \). 

## Exercise 1.5

Let \( Y \sim \text{Geom}_1(\pi) \). 

1. From the definition of expectation, show that \( E(Y) = \frac{1}{\pi} \). 
2. From the definition of variance, show that \( \text{Var}(Y) = \frac{1 - \pi}{\pi^2} \). 
3. Show that the CDF of \( Y \) is 

\[
Pr(Y \leq y) = 1 - (1 - \pi)^y. 
\]
4. Hence, find the survival function, \( Pr(Y > y) \), i.e., the probability that \( Y \) exceeds or “survives” \( y \) trials. 
5. Suppose it is given that \( Y \) exceeds a value \( y_0 \). Show that 

\[
Pr(Y > y_0 + y | Y > y_0) = Pr(Y > y),
\]

i.e., the probability of surviving at least another \( y \) trials does not depend on the number of trials already survived. (Such a random variable is said to have a “memoryless” property.)

## Exercise 1.6

Let \( Y \sim \text{Geom}_0(\pi) \). 

1. Find \( Pr(Y \geq 1) \). 
2. Suppose it is given that \( Y \geq 1 \). Show that 

\[
Pr(Y = y | Y \geq 1) = (1 - \pi)^{y-1} \pi \quad (y = 1, 2, \ldots).
\]
3. What is the distribution of \( Y \) conditional on \( Y \geq 1 \)?

## Exercise 1.7

Let \( Y \) have an \( \text{Expon}(\lambda) \) distribution. 

1. What is \( E(Y) \)? 
2. What is \( E(Y^2) \) and hence what is \( \text{Var}(Y) \)? 

## Exercise 1.8

Show the following properties of the normalizing factor (1.2) of the gamma PDF.

1. \( \Gamma(1) = 1 \).
2. \( \Gamma\left(\frac{1}{2}\right) = \sqrt{\pi} \). (Manipulation of an integrand to make it have the same form as a well-known PDF is a tactic much used in Section 1.8 to evaluate moment generating functions.)

## Exercise 1.9

Let \( Y \) have a \( \Gamma(\nu, \lambda) \) distribution, i.e., 

\[
f_Y(y) = \frac{1}{\lambda} \frac{(\lambda y)^{\nu - 1} e^{-\lambda y}}{\Gamma(\nu)} \quad (0 < y < \infty; \, \nu > 0; \, \lambda > 0),
\]

where \( \nu \) and \( \lambda \) are shape and rate parameters. Use the result in (1.3) to show that the PDF of \( Z = \frac{1}{Y} \) is 

\[
f_Z(z) = \frac{1}{\Gamma(\nu)} \frac{1}{z^{\nu + 1}} \lambda^y e^{-\frac{\lambda}{z}} \quad (0 < z < \infty; \, \nu > 0; \, \lambda > 0).
\]

This is called an inverse-gamma distribution with shape parameter \( \nu \) and scale parameter \( \lambda \).

## Exercise 1.10

Let \( Y \) be the lifetime of an item. It has an \( \text{Expon}(\lambda) \) distribution. 

1. Find the survival function, \( S_Y(y) = Pr(Y > y) \). 
2. Suppose at time \( y_0 \) the item is still alive, and we want to condition on the fact that \( Y > y_0 \). Find \( Pr(Y > y_0 + y | Y > y_0) \), the probability of surviving an additional time \( y \) given survival to time \( y_0 \). 
3. Hence, given that \( Y > y_0 \), what is the distribution of the additional lifetime?

## Exercise 1.11

Let \( Y \sim \text{logN}(\mu, \sigma^2) \), i.e., \( Z = \ln(Y) \) has a \( N(\mu, \sigma^2) \) distribution. Using properties of the normal distribution, show that the median of \( Y \) is \( e^\mu \).

## Exercise 1.12

A mail-order company sends an offer to its population of customers. Let \( B_1 \) be a random variable taking the values 0 (does not buy) or 1 (buys) for a randomly chosen customer. At a later date the company sends out another offer; let \( B_2 \) be the analogous 0/1 random variable for the second offering. The probabilities for the joint distribution of \( B_1 \) and \( B_2 \) are given in the following table.

| \( B_1 \) | \( B_2 \) |
|-----------|-----------|
| 0         | 1         |
| 0.3       | 0.0       |
| 0.1       | 0.6       |

1. Compute \( E(B_1) \) and \( E(B_2) \). 
2. Compute \( \text{Var}(B_1) \) and \( \text{Var}(B_2) \). 
3. Compute \( \text{Cov}(B_1, B_2) \). 
4. Let \( B = B_1 + B_2 \) be the total number of purchases by a randomly selected customer. Compute \( E(B) \) and \( \text{Var}(B) \):
   - (a) by first enumerating the distribution of \( B \) (i.e., computing \( f_B(b) \) for all values \( b \) of \( B \)); and
   - (b) by using results on linear combinations of random variables.
```
