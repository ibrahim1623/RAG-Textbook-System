```markdown
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 1.1. DISCRETE AND CONTINUOUS RANDOM VARIABLES

## Example 1.3 (Normal distribution: symmetry)
A random variable with a normal distribution has PDF

$$
f_Y(y) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(y-\mu)^2}{2\sigma^2}}
$$

over possible values $-\infty < y < \infty$, for given constants $\mu$ and $\sigma^2 > 0$. The PDF satisfies

$$
f_Y(\mu - x) = f_Y(\mu + x)  \quad (0 \leq x < \infty)
$$

and hence is symmetric around $\mu$ for any value of $\sigma^2$. 

### 1.1.2 Cumulative distribution function

For either a continuous or a discrete random variable, $Y$, the cumulative distribution function (CDF) is defined as 

$$
F_Y(y) = \Pr(Y \leq y).
$$ 

For a particular value $y$, the probability will be evaluated by summation (discrete $Y$) or integration (continuous $Y$) over values up to $y$. For a continuous random variable, it does not matter whether the CDF is defined as $\Pr(Y \leq y)$ or $\Pr(Y < y)$. For a discrete random variable, there is usually little choice but to sum the PDF explicitly to compute the CDF. For instance, the Poisson CDF evaluated at, say, $y = 3$ is 

$$
F_Y(3) = \Pr(Y \leq 3) = \sum_{y=0}^{3} \frac{e^{-\mu} \mu^y}{y!}
$$ 

and not much simplification is possible. For some commonly met continuous distributions, however, simple expressions for the CDF are available by integrating the PDF. Conversely, the PDF is obtained by differentiating the CDF. 

## Example 1.4 (Exponential distribution: CDF)
Let $Y$ have an $\text{Expon}(\lambda)$ distribution. From the definition of the CDF,

$$
F_Y(y) = \Pr(Y \leq y) = \int_0^y f_Y(t) dt = \int_0^y \lambda e^{-\lambda t} dt = -e^{-\lambda t}\bigg|_{t=0}^{t=y} = -e^{-\lambda y} - (-1) = 1 - e^{-\lambda y}.
$$

(Here, $t$ is a dummy variable as we want to integrate over all values $t$ of $Y$ up to $y.)$

Similarly, we can go from the CDF to the PDF:

$$
\frac{dF_Y(y)}{dy} = \lambda e^{-\lambda y} = f_Y(y).
$$

♢♢♢

Statisticians sometimes find it convenient to work in terms of the survival function or survivor function,

$$
S_Y(y) = \Pr(Y > y) = 1 - F_Y(y).
$$ 

It is just the complement of the CDF.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## Table 1.1: Probability mass function for the final-exam grade of a randomly chosen student in a given section of a statistics course

| Grade on final (y) | 60 | 90 |
|---------------------|----|----|
| $f_Y(y)$           | 0.2 | 0.8 |

### 1.2 Mean, Median, and Mode

Much statistical analysis is concerned with estimating an average or typical value to represent a distribution of possible values. There are several definitions of “average”. 

#### 1.2.1 Mean or expectation

The mean or expected value of a random variable $Y$ is just a weighted average over the possible values, $y$, with the weights given by $f_Y(y)$.

**Definition 1.1 (Expectation (mean))** The expected value or mean of a random variable $Y$ is given by the sum 

$$
E(Y) = \sum_{y} y f_Y(y)
$$ 

if $Y$ takes discrete values, or by the integral 

$$
E(Y) = \int y f_Y(y) dy
$$ 

if $Y$ takes continuous values. The integral or sum is over all possible values $y$. 

## Example 1.5 (Final-exam grade: expectation)

As a simple illustration of expectation of a discrete random variable, let $Y$ represent the grade on the final exam of a randomly chosen student from a given section of a statistics course. For simplicity, let us say $Y$ can take only two values, 60% and 90%. The probability mass function, $f_Y(y)$, for $Y$ is given in Table 1.1. Definition 1.1 immediately gives 

$$
E(Y) = 60 \cdot 0.2 + 90 \cdot 0.8 = 84,
$$ 

i.e., the mean grade of students is 84%. This example shows that the so-called expected value does not have to be a possible value of the random variable.

♢♢♢

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 1.2. MEAN, MEDIAN, AND MODE

## Example 1.6 (Uniform distribution: expectation)
If $Y$ has a uniform distribution, it has possible values $a < y < b$, for given constants $a$ and $b$, and PDF

$$
f_Y(y) = \frac{1}{b-a} \quad (a < y < b; a < b).
$$ 

The distribution is denoted by $\text{Unif}(a, b)$. From Definition 1.1, the expectation or mean of $Y$ is

$$
E(Y) = \int_a^b y f_Y(y) dy = \int_a^b \frac{1}{b-a} y dy = \frac{(b-a)}{2(b-a)} \bigg|_{y=a}^{y=b} = \frac{a+b}{2}.
$$

♢♢♢

In later probability and statistical results we will often have a condition that a property, like expectation, of a random variable has to exist. The condition is just requiring that the expectation is defined, that is, if and only if 

$$
\sum_{y}|y|f_Y(y) \text{ (discrete)} \quad \text{or} \quad \int |y|f_Y(y) dy \text{ (continuous) is finite.}
$$

To illustrate this technicality, consider the Poisson distribution,

$$
f_Y(y) = \frac{e^{-\mu} \mu^y}{y!} \quad (y = 0, 1, \ldots, \infty; \mu > 0),
$$

where $\mu$ is a parameter controlling the shape of the distribution. The expectation is 

$$
E(Y) = \sum_{y=0}^{\infty} y \frac{e^{-\mu} \mu^y}{y!}.
$$ 

It may look like this sum diverges because the infinite sum averages $y$ values tending to infinity. But the growth in $y$ (and possibly $\mu^y$) is dominated by $\frac{1}{y!}$, which decreases much more rapidly. Thus, the sum converges to a finite quantity, and the expectation is $\mu$ (Exercise 1.4). The notation $\mu$ is often used for the mean of a random variable in general. 

In contrast, take the distribution 

$$
f_Y(y) = \frac{6}{\pi^2} \cdot \frac{1}{y^2} \quad \text{for } y = 1, 2, \ldots, \infty,
$$

where $\pi \approx 3.14159$ (not a parameter). This is a valid PMF because its values are positive and sum to 1. If we try to calculate 

$$
E(Y) = \sum_{y=1}^{\infty} y \cdot \frac{6}{\pi^2} \cdot \frac{1}{y^2},
$$ 

however, the sum does not converge ($\sum_{y=1}^{\infty} \frac{1}{y}$ is divergent). Here, the PMF does not decay fast enough to offset the growth in the value of $y$; the expectation is infinite. This simple illustration shows that not every PMF or PDF yields an expected value. A constant $a$ has expectation $a$. This is seen by applying Definition 1.1 to the degenerate discrete random variable $A$ that takes value $a$ with probability 1.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## Table 1.2: Binomial PMF and CDF for $n = 3$ trials and probability of success $\pi = \frac{1}{4}$

| $y$ | PMF       | CDF         |
|-----|-----------|-------------|
| 0   | 0.421875  | 0.421875    |
| 1   | 0.421875  | 0.843750    |
| 2   | 0.140625  | 0.984375    |
| 3   | 0.015625  | 1.000000    |

### 1.2.2 Median

The median $m$ of a random variable $Y$ essentially divides its range such that the total probability of 1 is divided equally left and right of $m$. Thus, from the CDF, $m$ satisfies 

$$
F_Y(m) = \Pr(Y \leq m) = \frac{1}{2} \quad \text{or} \quad F_Y(m) \simeq \frac{1}{2}.
$$ 

The latter approximation arises because there may be no solution $m$ exactly satisfying $F_Y(m) = \frac{1}{2}$ when $Y$ is discrete. The definition of the median has to accommodate such cases. 

**Definition 1.2 (Median of a distribution)** The median $m$ of a random variable $Y$ is the smallest possible value of $Y$ such that 

$$
F_Y(m) = \Pr(Y \leq m) \geq \frac{1}{2}.
$$ 

For a continuous random variable with continuous CDF, $m$ is the solution of $F_Y(m) = \frac{1}{2}$. The definition is thus straightforward for continuous distributions. 

## Example 1.7 (Exponential distribution: median)

As $F_Y(y) = 1 - e^{-\lambda y}$, the median $m$ satisfies 

$$
1 - e^{-\lambda m} = \frac{1}{2}.
$$ 

Rearrangement gives 

$$
e^{-\lambda m} = \frac{1}{2}, \quad \text{then } -\lambda m = -\ln(2), \quad \text{and finally } m = \frac{\ln(2)}{\lambda}.
$$ 

♢♢♢

For a discrete random variable, there are rules for some special cases, but $m$ is usually found by enumeration. 

## Example 1.8 (Binomial distribution: median)
The binomial distribution with $n$ trials and probability of “success” $\pi$ has PMF 

$$
f_Y(y) = {n \choose y} \pi^y (1 - \pi)^{n-y} \quad (y = 0, 1, \ldots, n).
$$ 

Suppose $n = 3$ and $\pi = \frac{1}{4}$, for which the PMF and CDF are given computed in Table 1.2. It is seen that $y = 1$ is the smallest value such that $F_Y(y) \geq \frac{1}{2}$, and the median is $m = 1$. Also note that 

$$
F_Y(1) = \Pr(Y \leq 1) \geq \frac{1}{2} \quad \text{and} \quad \Pr(Y \geq 1) = 1 - 0.421875 \geq \frac{1}{2},
$$ 

and in this sense $m = 1$ divides the total probability of 1 into 2 halves. 

♢♢♢

### 1.2.3 Mode

The mode of a distribution is a value maximizing the PMF or PDF. It may not be unique. 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 1.3 Variance

### 1.3.1 Computation

The variance of $Y$ is the expected (mean) of the squared deviation of $Y$ around its mean. 

**Definition 1.3 (Variance)** The variance of $Y$ is 

$$
\text{Var}(Y) = E(Y - E(Y))^2,
$$ 

where the expectation on the right is with respect to the distribution of $Y$. An equivalent definition, often used, is 

$$
\text{Var}(Y) = E(Y^2) - (E(Y))^2.
$$ 

The definition of variance requires computation of expectations, which are handled by referring back to Definition 1.1. 

For a discrete random variable, expectation and hence variance are computed by summation over all the possible values $y$:

$$
\text{Var}(Y) = E(Y - E(Y))^2 = E(Y - \mu)^2 = \sum_{y} (y - \mu)^2 f_Y(y)
$$ 

or, equivalently, 

$$
\text{Var}(Y) = E(Y^2) - (E(Y))^2 = E(Y^2) - \mu^2 = \sum_{y} y^2 f_Y(y) - \mu^2,
$$ 

where $\mu = E(Y)$. 

## Example 1.10 (Final-exam grade: variance)

For the distribution $f_Y(y)$ of final grades in Table 1.1, we already computed $E(Y) = \mu = 84$. Hence,

$$
\text{Var}(Y) = E(Y - \mu)^2 = (60 - 84)^2 \cdot 0.2 + (90 - 84)^2 \cdot 0.8 = 144.
$$ 

Alternatively, using the second definition of variance,

$$
\text{Var}(Y) = E(Y^2) - \mu^2 = (60)^2 \cdot 0.2 + (90)^2 \cdot 0.8 - (84)^2 = 144.
$$ 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

To see the equivalence of the definition in general for discrete random variables, we just expand the square in the first definition and rearrange the sum for the expectation:

$$
E(Y - \mu)^2 = \sum_{y} (y - \mu)^2 f_Y(y) = \sum_{y} (y^2 - 2\mu y + \mu^2) f_Y(y) = \sum_{y} y^2 f_Y(y) - 2\mu \sum_{y} y f_Y(y) + \mu^2 
$$

$$
= E(Y^2) - 2\mu E(Y) + \mu^2 = E(Y^2) - \mu^2.
$$ 

For a continuous random variable, summation is again replaced by integration, and 

$$
\text{Var}(Y) = E\left(Y - \mu\right)^2 = \int (y - \mu)^2 f_Y(y) dy 
$$ 

or, equivalently, 

$$
\text{Var}(Y) = E(Y^2) - \mu^2 = \int y^2 f_Y(y) dy - \mu^2.
$$ 

The equivalence is shown in the same way as for a discrete random variable. 

## Example 1.11 (Uniform distribution: variance)

Let $Y$ have a $\text{Unif}(a, b)$ distribution, i.e., it has PDF 

$$
f_Y(y) = \frac{1}{b-a} \quad (a < y < b; a < b).
$$ 

From Example 1.6 we already know that $E(Y) = \frac{a+b}{2}$. To use the second expression for the variance in Definition 1.3, we also need 

$$
E(Y^2) = \int_a^b y^2 f_Y(y) dy = \int_a^b \frac{y^2}{b-a} dy = \frac{1}{b-a} \cdot \frac{b^3-a^3}{3} = \frac{(b^2 + ab + a^2)}{3(b - a)}.
$$ 

Hence,

$$
\text{Var}(Y) = E(Y^2) - (E(Y))^2 = \frac{(b^2 + ab + a^2)}{3(b - a)} - \left(\frac{(a+b)}{2}\right)^2 = \frac{(b-a)^2}{12}.
$$ 

♢♢♢

The variance exists only if the sum or integral converges. The expectation must exist for the variance to exist. A constant $a$ has variance 0. This is seen by applying Definition 1.3 to the degenerate discrete random variable $A$ that takes value $a$ with probability 1: 

$$
\text{Var}(A) = E(A - E(A))^2 = (a - a)^2 \cdot 1 = 0.
$$ 

Often, $\sigma^2$ is used as notation for a variance.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 1.3.2 Standard deviation

The standard deviation, often denoted by $\sigma$, is 

$$
\text{sd}(Y) = \sqrt{\text{Var}(Y)}.
$$ 

As the variance and standard deviation of a random variable are trivially related, we can use either. For mathematical manipulation, it is often easier to work with variances. For example, variances, not standard deviations, add for independent random variables (Section 1.7.7). On the other hand, when reporting results the standard deviation is easier to interpret because it has the same physical units as $Y$ and not the square of the original units. For instance, the variance of the exam grade in Example 1.10 is 144%² and having units of %² is bizarre. We could also say that the standard deviation of $Y$ is 

$$
\text{sd}(Y) = \sqrt{\text{Var}(Y)} = 12\%,
$$ 

which is much easier to interpret. Hence, we will switch back and forth between variance and standard deviation. 

### 1.3.3 Chebyshev’s inequality

Chebyshev’s inequality uses the variance to bound how far a random variable, $Y$, can deviate from its mean in the following probabilistic sense. 

**Theorem 1.1 (Chebyshev’s inequality)** Let the random variable $Y$ have a distribution such that the mean and variance, $\mu$ and $\sigma^2$, exist. Then 

$$
\Pr(|Y - \mu| > t) \leq \frac{\sigma^2}{t^2},
$$ 

for any $t > 0$. The result holds for any distribution for $Y$, and hence the probability bound on the right can be weak. Nonetheless, if $Y$ has a small enough variance then there is only a small probability that $Y$ is more than an arbitrary distance from its mean, an argument used to prove the law of large numbers in Theorem 3.1, for instance.

## 1.4 Commonly Used Discrete Distributions

Table 1.3 summarizes some commonly used discrete distributions, along with their expectations and variances. It also gives their moment generating functions (to be developed in Section 1.8). In the table, parameters of the distributions (e.g., the parameter $\pi$ of the Bernoulli distribution) are denoted by lower-case Greek letters if they are usually unknown in practice (and hence estimated in statistical inference) or by Roman lower-case letters if they are usually known quantities. (The Greek alphabet, with pronunciations, is given on page xxi.)

The distributions in Table 1.3 are now briefly described. 

### 1.4.1 Bernoulli distribution

A Bernoulli random variable has only two possible outcomes, coded as 0 (“no”, “absent”, “failure”, etc.) or 1 (“yes”, “present”, “success”, etc.), with probabilities $1 - \pi$ and $\pi$, respectively. Thus, the PMF can be represented as 

$$
f_B(b) = \pi^b (1 - \pi)^{1-b} \quad (b = 0, 1; 0 < \pi < 1).
$$ 

The Bernoulli distribution $\text{Bern}(\pi)$ is the building block for the remaining discrete distributions, which can all be thought of as counting the number of “successes” ($B = 1$) observed from independent Bernoulli events. (We will refer to the event $B = 1$ generically as a “success” when outlining the remaining distributions.)

### 1.4.2 Binomial distribution

The binomial distribution counts the number of “successes” among a fixed number, $n$, of independent and identically distributed (IID) Bernoulli trials, each of which is a success or not. Thus, $Y \sim \text{Bin}(n, \pi)$ is $\sum_{i=1}^n B_i$, where the $B_i$ are independent $\text{Bern}(\pi)$. The binomial distribution is perhaps the most important discrete distribution because $Y/n$ is the sample proportion, of interest in numerous applications. For instance, the efficacy of an experimental drug might be assessed by the proportion of patients in a clinical trial of $n$ patients who respond positively to the drug.

### 1.4.3 Geometric distribution

A random variable with a geometric distribution arises from a sequence of IID Bernoulli trials. It counts the number of trials until one success is observed. There are two equivalent versions of the geometric distribution; the one used is just a matter of convenience for the application. The difference is whether the terminating trial with a success outcome is counted. A $\text{Geom}_0(\pi)$ random variable does not count the terminating successful trial, and hence takes values $0, 1, 2, \ldots$ for the number of failures observed. The $\text{Geom}_1(\pi)$ version does count the terminating trial, so there must be at least one trial, and the random variable takes values $1, 2, \ldots$. Thus, the $\text{Geom}_0(\pi)$ versus $\text{Geom}_1(\pi)$ notation indicates whether the support of the random variable starts at 0 or 1.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 1.4.4 Negative-binomial distribution

A negative-binomial random variable $Y \sim \text{NegBin}(n, \pi)$ arises as the sum of $n$ independent $\text{Geom}_1(\pi)$ random variables. Thus it counts the number of Bernoulli trials until $n$ successes have occurred. The $\text{Geom}_1(\pi)$ distribution is the special case of the $\text{NegBin}(n, \pi)$ distribution with $n = 1$. The negative-binomial distribution is also related to the binomial in the following sense. If $Y \sim \text{NegBin}(n, \pi)$, then $Y$ represents a random sample size to achieve a fixed number, $n$, of successes. The binomial switches what is random and what is fixed: $Y \sim \text{Bin}(n, \pi)$ represents a random number of successes for a fixed sample size, $n$.

### 1.4.5 Poisson distribution

A Poisson random variable can be thought of as a limiting case of the binomial. If $Y \sim \text{Bin}(n, \pi)$, and we take the limits $n \to \infty$ and $\pi \to 0$ such that $\mu = n\pi$ tends to a constant, then $Y \sim \text{Pois}(\mu)$ is the limiting distribution. Thus, the Poisson distribution is called the law of rare events: the probability of a success is vanishingly small, but a proper distribution arises because there are many such potential events. The parameter $\mu$ is the mean and variance, which can be restrictive for applications. Often empirical data suggest that the variance is larger than the mean, so-called “over-dispersion”. Thus, even when first principles suggest a Poisson probability model, a distribution with more flexibility in the mean-variance relationship, such as the negative-binomial, might be substituted. 

### 1.5 Commonly Used Continuous Distributions

Table 1.4 summarizes some commonly used continuous distributions, which we now describe briefly. 

#### 1.5.1 Beta distribution

The beta distribution takes values on $(0, 1)$ and hence is useful for modelling quantities that must lie on that interval. It finds particular utility in Chapter 6 on Bayesian inference, where uncertainty about a parameter representing a probability is often treated as a beta random variable. In that chapter we shall see that the parameters $a$ and $b$ of the $\text{Beta}(a, b)$ distribution make the shape of its PDF fairly flexible. The beta function,

$$
B(a, b) = \int_0^1 y^{a-1} (1 - y)^{b-1} dy,
$$ 

is the normalizing factor of the beta distribution.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## Table 1.3: Some commonly used discrete distributions, along with their expectations, variances, and moment generating functions (MGFs)

| Distribution       | PMF, $f_Y(y)$                                   | $E(Y)$          | $\text{Var}(Y)$                      | MGF, $M_Y(t)$                               |
|--------------------|--------------------------------------------------|-----------------|--------------------------------------|----------------------------------------------|
| Bernoulli         | $f_Y(0) = 1 - \pi, f_Y(1) = \pi$                 | $\pi$           | $\pi(1 - \pi)$                       | $1 - \pi + \pi e^t$                         |
| Binomial          | $f_Y(y) = \binom{n}{y} \pi^y (1 - \pi)^{n-y}, y = 0, 1, \ldots, n$ | $n\pi$         | $n\pi(1 - \pi)$                      | $(1 - \pi + \pi e^t)^n$                     |
| Geometric         | $f_Y(y) = (1 - \pi)^y \pi$                       | $\frac{1 - \pi}{\pi}$ | $\frac{1 - \pi}{\pi^2}$             | $\frac{\pi}{1 - (1 - \pi)e^t}$             |
| Negative binomial | $f_Y(y) = \binom{y-1}{n-1} (1 - \pi)^y \pi^n$ | $n(1 - \pi)/\pi$ | $\frac{n(1 - \pi)}{\pi^2}$           | $(\frac{\pi}{1 - (1 - \pi)e^t})^n$         |
| Poisson           | $f_Y(y) = \frac{e^{-\mu} \mu^y}{y!}, y = 0, 1, \ldots, \infty$  | $\mu$           | $\mu$                               | $e^{\mu(e^t - 1)}$                          |

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

### 1.5.2 Exponential distribution

The PDF of the exponential distribution has a parameter $\lambda$ called the rate, and we denote the PDF by $\text{Expon}(\lambda)$. As its name suggests, the PDF is exponentially decreasing, as illustrated in Figure 1.1. As the rate increases, the distribution has more mass to the left. For instance, if $Y$ is an exponential distribution representing the time to occurrence of an event, then a larger value of $\lambda$ says that the rate at which the event occurs is faster and $Y$ tends to take smaller values. Mathematically, 

$$
E(Y) = \frac{1}{\lambda}
$$ 

for the exponential distribution, i.e., the mean decreases with increasing rate (Exercise 1.7), which is summarized in Table 1.4 along with other properties. Hence, if $Y$ is measured in days say, $E(Y)$ also has units of days, and $\lambda = \frac{1}{E(Y)}$ has units $1/\text{day}$, a rate per day. That is why $\lambda$ is often called the “rate” parameter.

### 1.5.3 Gamma distribution

The gamma PDF is a generalization of the exponential PDF: putting $\nu = 1$ in $\text{Gamma}(\nu, \lambda)$ gives $\text{Expon}(\lambda)$. As with the exponential distribution, $\lambda$ is interpreted as a rate, but the extra parameter $\nu$ controls the shape of the distribution. Figure 1.2 shows that the gamma PDF is skewed like the exponential but approaches a symmetric, bell-shape as $\nu$ increases. A further connection between the exponential and gamma distributions is that a sum of $\nu$ IID $\text{Expon}(\lambda)$ random variables has a $\text{Gamma}(\nu, \lambda)$ distribution, a result demonstrated in Example 1.31.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14
```