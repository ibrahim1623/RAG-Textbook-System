```markdown
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 1.11. EXERCISES

## 1-49

### Exercise 1.13
For a specific type of property insurance claim, an actuary models the customer’s loss by the random variable \( X \sim \text{Expon}(\lambda) \). But the particular policy has a limit \( k \) on the amount that the insurance company has to pay. Thus, when a claim is made, the company pays out \( Y = \min(X, k) \). What is \( E(Y) \)? 

### Exercise 1.14
Let \( X \) and \( Y \) be continuous random variables with finite expectations, and let \( a, b, \) and \( c \) be finite constants. From the definition of expectation, prove the following results.
1. \( E(a + X) = a + E(X) \).
2. \( E(bX) = bE(X) \).
3. \( E(a + bX) = a + bE(X) \).
4. \( E(X + Y) = E(X) + E(Y) \).
5. \( E(a + bX + cY) = a + bE(X) + cE(Y) \).
6. If \( X \) and \( Y \) are discrete random variables, how are these proofs changed? 

### Exercise 1.15
Let \( X \) and \( Y \) be random variables with finite covariance, and let \( a \) and \( b \) be finite constants. From the definition of covariance, prove the result 
\[
\text{Cov}(a + bY, c + dZ) = bd \, \text{Cov}(Y, Z)
\]
in (1.11). 

### Exercise 1.16
Let \( X \) and \( Y \) be random variables with finite variances, and let \( a, b, \) and \( c \) be finite constants. Starting from the definition of variance, i.e.,
\[
\text{Var}(X) = E(X^2) - (E(X))^2,
\]
prove the following results. (Hint: The definition of variance is in terms of expectations; use the results of Exercise 1.14.)
1. \( \text{Var}(a + X) = \text{Var}(X) \).
2. \( \text{Var}(bX) = b^2 \text{Var}(X) \).
3. \( \text{Var}(a + bX) = b^2 \text{Var}(X) \).
4. \( \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y) \).
5. \( \text{Var}(a + bX + cY) = b^2 \text{Var}(X) + c^2 \text{Var}(Y) + 2bc \text{Cov}(X, Y) \). (This is a special case of the more general result in Section 1.7.7.)

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 1-50

### CHAPTER 1. PROBABILITY TOOLS

### Exercise 1.17
Let \( Y_1, \ldots, Y_n \) be independent random variables, each taking the values 0 or 1 with probabilities \( 1 - \pi \) and \( \pi \), respectively. Here \( \pi \), the probability that \( Y = 1 \), is an unknown parameter to be estimated. 
1. Show that \( E(Y_i) = \pi \) and \( \text{Var}(Y_i) = \pi(1 - \pi) \).
2. Consider the estimator \( \tilde{\pi} = \frac{1}{n} \sum_{i=1}^n Y_i \) of \( \pi \). (This is simply the proportion of 1’s amongst \( Y_1, \ldots, Y_n \). It is a random variable because the \( Y_i \) are random.)
   (a) Show that \( E(\tilde{\pi}) = \pi \), i.e., \( \tilde{\pi} \) is an unbiased estimator of \( \pi \). 
   (b) Show that \( \text{Var}(\tilde{\pi}) = \frac{\pi(1 - \pi)}{n} \). 

### Exercise 1.18
[Quiz #1, 2009-10, Term 1] Let \( B \) be a Bernoulli random variable taking values \( b = 0, 1 \). Its PMF is given by \( f_B(0) = \Pr(B = 0) = 1 - \pi \) and \( f_B(1) = \Pr(B = 1) = \pi \). Thus, \( B \sim \text{Bern}(\pi) \). Show each of the following results. For full marks you need to be explicit about the mathematical definition of the quantity involved (\( E(), \text{Var()} \) or MGF) and how the definition is used for this specific problem. 
1. Show \( E(B) = \pi \). 
2. Find \( E(10B) \). 
3. Show \( \text{Var}(B) = \pi(1 - \pi) \). 
4. Show that the moment generating function (MGF) of \( B \) is \( M_B(t) = 1 - \pi + \pi e^t \). 
5. Check that the MGF exists for \( t \) in an open neighbourhood of zero. 
6. Use the MGF to find \( E(B) \).

### Exercise 1.19
[Quiz #1, 2009-10, Term 1] Let \( Y = B_1 + \cdots + B_n \), where the random variables \( B_1, \ldots, B_n \) are independent and each has a \( \text{Bern}(\pi) \) distribution. You may use the results in Exercise 1.18 that \( B_i \) has mean \( \pi \), variance \( \pi(1 - \pi) \), and MGF \( 1 - \pi + \pi e^t \). Also, \( n \) is some fixed number. 
1. Find \( E(Y) \). 
2. Find \( \text{Var}(Y) \). 
3. Find the moment generating function of \( Y \). 
4. Hence, what is the distribution of \( Y \)? 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 1-51

### Exercise 1.20
Let \( Y \sim \text{Pois}(\mu) \). Thus, the PMF of \( Y \) is
\[
f_Y(y) = \frac{e^{-\mu} \mu^y}{y!} \quad (y = 0, 1, \ldots, \infty; \mu > 0). 
\]
1. Show that \( Y \) has the MGF 
\[
M_Y(t) = \frac{e^{\mu(e^{-1})}}{t}.
\]

2. Let \( Y_1, \ldots, Y_n \) be independent Poisson random variables, where \( Y_i \) has mean \( \mu_i \), i.e., \( Y_i \sim \text{Pois}(\mu_i) \). Thus, the random variables may have different means and are not necessarily identically distributed. What is the MGF of \( \sum_{i=1}^n Y_i \)?

3. Hence, what is the distribution of \( \sum_{i=1}^n Y_i \)?

### Exercise 1.21
Let \( Y \sim \text{Unif}(a, b) \). Use the expansion of its MGF in Example 1.29 to show the following properties:
1. \( E(Y) = \frac{(a + b)}{2} \); and
2. \( \text{Var}(Y) = \frac{(b - a)^2}{12}. \)

### Exercise 1.22
Let \( Y \sim \text{Geom}_1(\pi) \). Thus, the PMF of \( Y \) is
\[
f_Y(y) = (1 - \pi)^{y - 1} \pi \quad (y = 1, 2, \ldots, \infty; 0 < \pi < 1). 
\]
1. Show that \( Y \) has the MGF
\[
M_Y(t) = \frac{e^{t} \pi}{1 - (1 - \pi)e^{t}}.
\]
2. From the MGF show that \( E(Y) = \frac{1}{\pi} \) and \( \text{Var}(Y) = \frac{1 - \pi}{\pi^2}. \)
3. Let \( Y_1, \ldots, Y_n \) be IID \( \text{Geom}_1(\pi) \) random variables. What is the distribution of \( \sum_{i=1}^n Y_i \)?

4. Hence, what is the distribution of \( \sum_{i=1}^n Y_i \)? 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 1-52

### CHAPTER 1. PROBABILITY TOOLS

### Exercise 1.23
Let \( Y \sim N(\mu, \sigma^2) \), i.e., the normal distribution with mean \( \mu \) and variance \( \sigma^2 \). This exercise shows in two ways that the MGF of \( Y \) is
\[
M_Y(t) = e^{\mu t + \frac{1}{2} \sigma^2 t^2}. 
\]
1. Apply the definition of the MGF in Definition 1.7 directly to the \( N(\mu, \sigma^2) \) PDF to find the MGF of \( Y \).
2. Let \( Z \) have a standard normal distribution, i.e., \( N(0, 1) \). Its MGF is
\[
M_Z(t) = e^{\frac{1}{2}t^2} \quad \text{(see Example 1.24)}. 
\]
Now let \( Y = \mu + \sigma Z \).
   (a) Verify that \( E(Y) = \mu \) and \( \text{Var}(Y) = \sigma^2 \) as required. 
   (b) Find the MGF of \( Y \) from the MGF of \( Z \).

### Exercise 1.24
Let \( Y \sim N(\mu, \sigma^2) \). Starting from the MGF of \( Y \), i.e.,
\[
M_Y(t) = e^{\mu t + \frac{1}{2} \sigma^2 t^2},
\]
this exercise verifies the first two moments. 
1. Use the MGF to show that \( E(Y) = \mu \). 
2. Use the MGF to show that \( E(Y^2) = \mu^2 + \sigma^2 \), and hence that \( \text{Var}(Y) = \sigma^2 \). 

### Exercise 1.25
Let \( Y \sim \text{Expon}(\lambda) \). Consider multiplying \( Y \) by a constant to give a new random variable, \( Z = bY \), where \( b > 0 \). 
1. Table 1.4 says the MGF of \( Y \) is \( \frac{\lambda}{\lambda - t} \). What is the MGF of \( Z \)?
2. What is the distribution of \( Z \)?
3. Apply the same argument to the gamma distribution to show that if \( Y \sim \text{Gamma}(\nu, \lambda) \), then \( Z = bY \sim \text{Gamma}(\nu, \lambda/b) \).

### Exercise 1.26
A random variable \( Y \), taking positive values, is said to have a log-normal distribution if \( Z = \ln(Y) \) has a \( N(\mu, \sigma^2) \) distribution. This exercise finds the expectation of \( Y \) from the MGF of \( Z \).
1. The definition of the MGF of \( Z \) is \( E(e^{tZ}) \). What expression do we get if we put \( t = 1 \) in this definition? 
2. Look up the MGF of \( Z \) (see Table 1.4 or Exercise 1.23), and put \( t = 1 \) in it. Hence, what is \( E(Y) \)?

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 2-1

## Chapter 2
## The Normal Distribution in Statistics

### 2.1 Introduction

The normal distribution, sometimes called the Gaussian distribution after Gauss, is ubiquitous in statistical analysis. It will arise in this book in several ways, including the following. 
- Based on a random sample from a \( N(\mu, \sigma^2) \) distribution, the sample mean is often used to estimate \( \mu \). Exact properties of the normal distribution lead to a confidence interval for \( \mu \) that accounts for the uncertainty in estimation, even if \( \sigma^2 \) is unknown. This analysis based on the \( t \) distribution is common in applications, as typified by Example 2.1. 
- If a random sample is taken from a distribution with mean \( \mu \) and variance \( \sigma^2 \), but the distribution is only approximately normal, use of the \( t \) distribution to provide a confidence interval for \( \mu \) is often still approximately valid. 
- For a large sample size, the normal distribution serves as an approximation to other distributions. For instance, the binomial distribution is a commonly used model for applications where estimating a population proportion is the focus. The error in using the sample proportion as an estimate is again quantified in a confidence interval, this time based on a normal approximation to the binomial distribution. More generally, under certain conditions, sample means, proportions, and totals have approximate normal distributions for a large enough sample size via the central limit theorem (Section 2.5.3).
- The method of maximum likelihood in Chapter 4 is a powerful generic method to estimate parameters for a wide range of probability models. An approximate confidence interval for the parameter is often available from an approximate normal distribution.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

### 2.2 Some Properties of the Normal Distribution

Let \( Y \) be a normal random variable with mean \( \mu \) and variance \( \sigma^2 \). We write \( Y \sim N(\mu, \sigma^2) \). The following properties were established using MGFs in Section 1.8 or in related exercises.
- The expected value (mean) of \( Y \) is \( E(Y) = \mu \), and the variance is \( \text{Var}(Y) = \sigma^2 \) (Exercise 1.24).
- A linear function of \( Y \) is also normal: \( a + bY \sim N(a + b\mu, b^2 \sigma^2) \) (Example 1.30). In particular,
\[
Z = \frac{Y - \mu}{\sigma} \sim N(0, 1]
\]
has the standard normal distribution \( N(0, 1) \), i.e., with mean 0 and variance 1 (Exercise 2.1). Also, for \( n \) normally distributed random variables, we have the following properties.
- If the \( n \) random variables are independent (but not necessarily identically distributed), Example 1.32 showed that a linear combination of them also has a normal distribution.
- If the \( n \) random variables are correlated but follow a multivariate normal distribution, a linear combination of them still has a normal distribution. The covariances between the \( n \) variables affect only the variance of the linear combination, via (1.10).
- If the \( n \) random variables follow a multivariate normal distribution and all the pairwise covariances between them are zero, then they are mutually independent. This result is a generalization of Lemma 1.1, which said that if \( Y \) and \( Z \) are bivariate normal with \( \text{Cov}(Y, Z) = 0 \), then \( Y \) and \( Z \) are independent.

### 2.3 Distributions Derived From the Normal

The normal distribution is important in itself and because other important distributions arise from it. The relationships among these distributions are summarized in Figure 2.1. We next give some details about these distributions. 

#### 2.3.1 The \( \chi^2 \) distribution

A \( \chi^2 \) (“chi-squared”) random variable is generated by the sum of squares of independent standard normal random variables.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

### 2.3. DISTRIBUTIONS DERIVED FROM THE NORMAL

(Additional content for subsequent sections continues here...) 
```
