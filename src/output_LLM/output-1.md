```markdown
. . . . . . . . . . . . . . . . . . . . .. . 2-8

2.6

Quantiles of the t distribution .. . . . . . . . . . . . . . . . . . .. . 2-14

3.1

Histograms of the faults data and Poisson samples (µ = 2.41) ... . 3-4

3.2

Histograms of the faults data and Poisson samples (µ = 5) .. . . . . 3-6

3.3

R code for Exercise 3.5 . . . . . . . . . . . . . . . . . . . . . . . .. . 3-17

4.1

Binomial PMF for various values of π .. . . . . . . . . . . . . . .. . 4-3

4.2

Likelihood plotted against the binomial parameter π .. . . . . .. . 4-4

4.3

Log likelihood plotted against the binomial parameter π .. . . .. . 4-5

4.4

Exponential distribution: likelihood and log likelihood functions . . . 4-7

4.5

Log likelihood plotted against the binomial parameter π .. . . .. . 4-10

4.6

Exponential distribution: ML estimate of λ versus sample size ... . 4-12

4.7

Exponential distribution: estimated distribution of λ̃ .. . . . . .. . 4-18

4.8

Exponential distribution: distribution of λ̃ and normal approximation 4-27

4.9

Quantiles of the standard normal distribution .. . . . . . . . . .. . 4-29

5.1

Censored insurance claims: Histograms of amount paid .. . . . .. . ix

5-9

x

LIST OF FIGURES
5.2

Censored insurance claims: contour plots of the log likelihood . .. . 5-11

6.1

Probability tree diagram for Example 6.1 .. . . . . . . . . . . . .. . 6-5

6.2

Beta priors, pΠ (π), for Π for various values of the shape parameters, a
and b .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 6-9

6.3

Beta (4, 8) posterior distribution for Π .. . . . . . . . . . . . . . .. . 6-11

6.4

Bayesian analysis of the vaccine treatment in the HIV example . .. . 6-13

6.5

Faults on data lines: likelihood and posterior .. . . . . . . . . . .. . 6-15

6.6

Prior for faults on data lines .. . . . . . . . . . . . . . . . . . . .. . 6-16

6.7

Normal distribution: likelihood as a function of µ and τ

6.8

Normal prior for the mean of the normal distribution .. . . . . .. . 6-23

6.9

Gamma prior for the precision parameter of the normal distribution . 6-24

. . . . .. . 6-22

6.10 Faults on data lines: posterior .. . . . . . . . . . . . . . . . . . .. . 6-27
7.1

Coin tossing: properties of a hypothesis test . . . . . . . . . . . .. . 7-9

7.2

Testing the parameter λ of the exponential distribution: distribution
of the test statistic under null and alternative hypotheses .. . . .. . 7-14

7.3

Exponential distribution: power curve .. . . . . . . . . . . . . .. . 7-18

7.4

Histogram of differences in rainfall .. . . . . . . . . . . . . . . .. . 7-27

7.5

Rainfall example: Rejection regions testing µ against 1-sided and 2sided alternatives .. . . . . . . . . . . . . . . . . . . . . . . . . .. . 7-27

7.6

Lung-function example: rejection region testing µ against a 1-sided
alternative .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 7-29

7.7

Lung-function example: p-value for testing µ against a 1-sided alternative7-31

8.1

Data from a TaqMan assay .. . . . . . . . . . . . . . . . . . . .. . 8-2

Difference in grapefruit solids: histogram and normal PDF .. . .. . 8-14

8.3

Difference in grapefruit solids: histogram and normal PDF (5 bins) . 8-15

8.4

Difference in grapefruit solids: histogram and normal PDF (overlaid)

8-16

9.1

Faults on data lines for two samples .. . . . . . . . . . . . . . . .. . 9-3

9.2

Rainfall data .. . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 9-20

9.3

Grapefruit data .. . . . . . . . . . . . . . . . . . . . . . . . . . .. . 9-23

8-2

10.1 Log-likelihood function for Exercise 4.2 .. . . . . . . . . . . . . . . . 10-13
10.2 R code for Exercise 4.12 . . . . . . . . . . . . . . . . . . . . . . . . . 10-16

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

LIST OF FIGURES

xi

List of Definitions
1.1

Expectation (mean) . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 1-4

1.2

Median of a distribution .. . . . . . . . . . . . . . . . . . . . . . . . . . 1-6

1.3

Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 1-7

1.4

Expectation of a function of random variable

1.5

Statistical independence .. . . . . . . . . . . . . . . . . . . . . . . .. . 1-24

1.6

Moments of a random variable .. . . . . . . . . . . . . . . . . . . . .. . 1-32

1.7

Moment generating function .. . . . . . . . . . . . . . . . . . . . . .. . 1-32

2.1

Convergence in distribution .. . . . . . . . . . . . . . . . . . . . . . . . 2-14

3.1

Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 3-7

3.2

Mean squared error (MSE) .. . . . . . . . . . . . . . . . . . . . . . . . . 3-8

3.3

Consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 3-10

4.1

Observed information

4.2

Fisher information .. . . . . . . . . . . . . . . . . . . . . . . . . . .. . 4-21

7.1

p-value .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7-30

. . . . . . . . . . . . . . . 1-19

. . . . . . . . . . . . . . . . . . . . . . . . . . . . 4-15

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

xii

LIST OF FIGURES

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

xiii

List of Lemmas and Theorems
Lemma 1.1

Bivariate normal: covariance of 0 implies independence . . . . . 1-30

Lemma 1.2

MGF of a linear function of a random variable . . . . . . . . . . 1-38

Lemma 1.3

MGF of a sum of independent random variables . . . . . . . . . 1-38

Lemma 2.1

χ² distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2-4

Lemma 2.2

t distribution (Student, 1908) . . . . . . . . . . . . . . . . . . . . 2-5

Lemma 2.3

F distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2-8

Lemma 7.1

Neyman-Pearson Lemma . . . . . . . . . . . . . . . . . . . . . . 7-11

Theorem 1.1

Chebyshev’s inequality . . . . . . . . . . . . . . . . . . . . . .

Theorem 1.2

Law of total probability . . . . . . . . . . . . . . . . . . . .. . 1-23

Theorem 1.3

The MGF identifies a distribution .. . . . . . . . . . . . . . . 1-38

Theorem 2.1

χ² corrected degrees of freedom . . . . . . . . . . . . . . . .. . 2-10

Theorem 2.2

Central limit theorem (CLT) .. . . . . . . . . . . . . . . .. . 2-18

Theorem 3.1

Weak law of large numbers (WLLN) .. . . . . . . . . . . . . . 3-11

Theorem 4.1

Consistency of the ML estimator . . . . . . . . . . . . . . . . . 4-13

Theorem 4.2

Asymptotic normality of the ML estimator . . . . . . . . .. . 4-26

Theorem 6.1

Bayes’ Rule (conditional probability) .. . . . . . . . . . . .. . 6-2

Theorem 6.2

Bayes’ Rule (statistical inference) .. . . . . . . . . . . . . . . . 6-7

Theorem 7.1

Distribution of Wilks’ statistic . . . . . . . . . . . . . . . . . . 7-23

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 1-9

2019.8.14

xiv

LIST OF FIGURES

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

xv

List of Examples
Example 1.1

Poisson PMF . . . . . . . . . . . . . . . . . . . . . . . . . .. . 1-2

Example 1.2

Exponential distribution: PDF .. . . . . . . . . . . . . . .. . 1-2

Example 1.3

Normal distribution: symmetry .. . . . . . . . . . . . . . .. . 1-3

Example 1.4

Exponential distribution: CDF .. . . . . . . . . . . . . . . . . 1-3

Example 1.5

Final-exam grade: expectation . . . . . . . . . . . . . . . .. . 1-4

Example 1.6

Uniform distribution: expectation .. . . . . . . . . . . . .. . 1-4

Example 1.7

Exponential distribution: median .. . . . . . . . . . . . . .. . 1-6

Example 1.8

Binomial distribution: median .. . . . . . . . . . . . . . .. . 1-6

Example 1.9

Binomial distribution: mode .. . . . . . . . . . . . . . . .. . 1-7

Example 1.10 Final-exam grade: variance . . . . . . . . . . . . . . . . . .. . 1-7

Example 1.11 Uniform distribution: variance .. . . . . . . . . . . . . . .. . 1-8

Example 1.12 PDF of a scaled exponential random variable .. . . . . . .. . 1-17
Example 1.13 PDF of the log-normal distribution from the normal .. . .. . 1-18
Example 1.14 Expectation of log uniform .. . . . . . . . . . . . . . . . .. . 1-19
Example 1.15 HIV vaccination trial: joint and marginal probabilities . . . . . 1-20
Example 1.16 HIV vaccination trial: conditional probability .. . . . . . .. . 1-22
Example 1.17 Final-exam and quiz grades: covariance . . . . . . . . . . .. . 1-25
Example 1.18 Covariance of zero does not imply independence .. . . . . .. . 1-26
Example 1.19 Course grade: expectation of a linear combination .. . . .. . 1-27
Example 1.20 Course grade: variance of a linear combination .. . . . . .. . 1-28
Example 1.21 Gamma distribution: mean and variance .. . . . . . . . . .. . 1-29
Example 1.22 Exponential distribution: MGF .. . . . . . . . . . . . . . .. . 1-32
Example 1.23 Gamma distribution: MGF .. . . . . . . . . . . . . . . . .. . 1-33
Example 1.24 Standard normal distribution: MGF .. . . . . . . . . . . .. . 1-34
Example 1.25 Binomial distribution: MGF .. . . . . . . . . . . . . . . . . . 1-34
Example 1.26 Exponential distribution: mean and variance via the MGF . . . 1-36
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

xvi

LIST OF FIGURES

Example 1.27 Gamma distribution: mean and variance via the MGF . . . . . 1-36
Example 1.28 Binomial distribution: mean and variance via the MGF ... . 1-37
Example 1.29 Uniform distribution: existence of the MGF .. . . . . . . .. . 1-37
Example 1.30 Normal distribution: linear function .. . . . . . . . . . . .. . 1-39
Example 1.31 Exponential distribution: sum of IID random variables .. . . . 1-39
Example 1.32 Normal distribution: sum of independent random variables . . . 1-39
Example 1.33 Casualty insurance: sum of IID geometric random variables . . 1-40
Example 2.1

Lung function: confidence interval for the normal mean . .. . 2-12

Example 2.2

Binomial distribution: normal approximation .. . . . . . .. . 2-14

Example 2.3

Opinion polls: margin of error (confidence interval) .. . . .. . 2-17

Example 2.4

Binomial distribution: normal approximation via CLT .. . . . 2-19

Example 3.1

Faults on data lines: estimating the Poisson mean .. . . .. . 3-3

Example 3.2

Faults on data lines: properties of the estimator of µ .. . .. . 3-8

Example 3.3

Sample variance: divisor of n − 1 or n? 3-9

Example 3.4

Opinion polls: weak law of large numbers . . . . . . . . . .. . 3-11

Example 3.5

Binomial distribution: sample size determination .. . . . . . . 3-13

Example 4.1

HIV vaccine: ML estimate of the binomial π parameter . .. . 4-1

Example 4.2

Binomial distribution: ML estimate of the parameter π .. . . . 4-4

Example 4.3

Exponential distribution: ML estimate of the rate

.. . . .. . 4-6

Example 4.4

Poisson distribution: ML estimate of the mean .. . . . . . . . 4-7

Example 4.5

HIV vaccine: sampling variance of the ML estimator . . . . . . 4-9

Example 4.6

HIV vaccine: consistency of the ML estimator . . . . . . . .. . 4-11

Example 4.7

Exponential distribution: consistency (simulation) .. . . .. . 4-11

Example 4.8

Exponential distribution: consistency (mathematical) .. . .. . 4-12

Example 4.9

Binomial distribution: observed information .. . . . . . . . . . 4-15

. . . . . . . . . . .. . Example 4.10 Exponential distribution: observed information .. . . . . . . . 4-16
Example 4.11 Exponential distribution: Var(λ̃) justification (simulation) . . . 4-17
Example 4.12 Exponential distribution: Var(λ̃) justification (mathematical) . 4-19
Example 4.13 Geometric distribution: Fisher information . . . . . . . . .. . 4-21
Example 4.14 Binomial distribution: Fisher information .. . . . . . . . .. . 4-23
Example 4.15 Exponential distribution: Fisher information .. . . . . . .. . 4-24
Example 4.16 Exponential distribution: asymptotic normality of λ̃ (simulation) 4-27
Example 4.17 Exponential distribution: asymptotic normality of λ̃ (mathematics)4-27

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

LIST OF FIGURES

xvii

Example 4.18 Faults on data lines: confidence interval for the mean . . . .. . 4-31
Example 4.19 Faults on data lines: confidence interval for Pr(Y = 0) .. . . . 4-31
Example 4.20 HIV vaccine: two confidence intervals for π .. . . . . . . .. . 4-32
Example 5.1

Normal distribution: ML estimates .. . . . . . . . . . . . . . . 5-1

Example 5.2

Normal distribution: unbiasedness of ML estimators . . . .. . 5-3

Example 5.3

Normal distribution: covariance matrix of ML estimators ... . 5-5

Example 5.4

Lung function: ML confidence interval for the normal mean . . 5-7

Example 5.5

Censored insurance claims . . . . . . . . . . . . . . . . . . .. . 5-8

Example 5.6

Censored insurance claims: maximum likelihood .. . . . .. . 5-10

Example 6.1

Quality control: Bayesian estimation of (discrete) π . . . . .. . 6-3

Example 6.2

Binomial distribution: Bayesian estimation of π .. . . . . .. . 6-7

Example 6.3

Quality control: Bayesian estimation of (continuous) π .. . . . 6-10

Example 6.4

HIV vaccine: Bayesian estimation of π . . . . . . . . . . . .. . 6-11

Example 6.5

Poisson distribution: Bayesian estimation of µ .. . . . . . .. . 6-12

Example 6.6

HIV vaccine: Bayesian credible interval for Π .. . . . . . .. . 6-14

Example 6.7

Faults on data lines: credible interval for the mean .. . . .. . 6-14

Example 6.8

Normal distribution: Bayesian estimation of µ (known σ²) . . . 6-17

Example 6.9

Normal distribution: Bayesian estimation of σ² (known µ) . . . 6-19

Example 6.10 Normal distribution: estimation of µ (unknown τ = 1/σ²) . . . 6-20
Example 6.11 Lung function: Bayesian credible interval for the mean .. . . . 6-21
Example 6.12 Faults on data lines: posterior Pr(Y = 0) .. . . . . . . . .. . 6-26
Example 6.13 Lung function: Credible interval (Gibbs sampling) .. . . .. . 6-28
Example 7.1

Quality control: Bayesian hypothesis test of π . . . . . . . .. . 7-2

Example 7.2

Is coin tossing fair? 7-7

Example 7.3

Exponential distribution: test of simple hypotheses . . . . .. . 7-12

Example 7.4

Normal distribution: test of the mean with known variance . . 7-15

Example 7.5

Exponential distribution: 1-sided test . . . . . . . . . . . .. . 7-17

Example 7.6

Exponential distribution: 2-sided test .. . . . . . . . . . .. . 7-19

Example 7.7

Lung function: formulation of a generalized LR test .. . .. . 7-20

Example 7.8

Normal distribution: GLR justification of the t statistic ... . 7-22

Example 7.9

Lung function: Wilks’ approximate test .. . . . . . . . . . . . 7-24

. . . . . . . . . . . . . . . . . . . . . .. . Example 7.10 Rainfall: hypothesis test of the normal mean .. . . . . . .. . 7-26
Example 7.11 Lung function: t test of the normal mean .. . . . . . . . . . . 7-28

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

xviii

LIST OF FIGURES

Example 7.12 Lung function: p-value of test of the normal mean . . . . .. . 7-30
Example 7.13 Rainfall: p-value of test of the normal mean .. . . . . . . .. . 7-30
Example 7.14 Lung function: p-value of test of the mean continued .. . .. . 7-32
Example 7.15 Rainfall: practical significance

.. . . . . . . . . . . . . . .. . 7-33

Example 7.16 Rainfall: hypothesis test versus confidence interval .. . . .. . 7-34
Example 7.17 Anaesthesia: binomial with no failures observed .. . . . . .. . 7-36
Example 8.1

Genotyping: multinomial distribution . . . . . . . . . . . .. . 8-2

Example 8.2

Genotyping: ML estimates of the multiomial parameters ... . 8-4

Example 8.3

Inheritance: test of Mendel’s ratios .. . . . . . . . . . . . . . . 8-6

Example 8.4

Genotyping: test of Hardy-Weinberg hypothesis . . . . . . .. . 8-8

Example 8.5

Faults on data lines: goodness of fit test .. . . . . . . . . .. . 8-10

Example 8.6

Solids in grapefruit: goodness of fit test .. . . . . . . . . .. . 8-13

Example 9.1

Faults on data lines: comparison of Poisson means .. . . .. . 9-2

Example 9.2

Faults on data lines: comparison of means per kilometre ... . 9-5

Example 9.3

Smoking cessation: comparison of binomial π parameters .. . . 9-7

Example 9.4

TV advertisements: comparison of normal means . . . . . .. . 9-11

Example 9.5

Rainfall: data before and after differencing .. . . . . . . . . . 9-19

Example 9.6

Protein constructs: estimation of mean difference . . . . . .. . 9-21

Example 9.7

Solids in grapefruit: data .. . . . . . . . . . . . . . . . . . . . 9-22

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

Abbreviations
Abbreviation
CLT
GLR
IID
LR
ML
MSE
PDF
PMF

Description
Central limit theorem
Generalized likelihood ratio
Independent and identically distributed
Likelihood ratio
Maximum likelihood
Mean squared error
Probability density function
Probability mass function

xix

xx

LIST OF FIGURES

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

Greek Symbols
The following Greek letters are used in the book. Pronunciations by statisticians vary
but are often close to those given here. Case
Lower Upper
α
A
β
B
γ
Γ
δ
∆
ϵ
E
ζ
Z
η
H
θ
Θ
ι
I
κ
K
λ
Λ
µ
M

Pronunciation
al-fah
bay-tah
gam-ah
del-tah
ep-si-lon
zay-tah
ay-tah
thay-tah
eye-oh-tah
kap-ah
lam-dah
mew

Case
Lower Upper
ν
N
ξ
Ξ
o
O
π
Π
ρ
R
σ
Σ
τ
T
υ
Υ
ϕ
Φ
χ
X
ψ
Ψ
ω
Ω

xxi

Pronunciation
new
zie (rhymes with pie)
oh-my-kron
pie
roe
sig-mah
tow (rhymes with now)
up-sigh-lon
fie (rhymes with pie)
kie (rhymes with pie)
sigh
oh-me-gah

xxii

LIST OF FIGURES

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

1-1

# Chapter 1
## Probability Tools
Statistical methods are strongly dependent on probability tools. Indeed, a statistical method typically starts and ends with probability models. The first step is to specify a probability model for the way the data were generated, and the last step often involves a calculation such as looking up a probability to compute a confidence interval or a Bayesian credible interval. In between, much of statistical inference is concerned with the unknown parameters of the probability model, which has possibly been refined along the way. Thus, statistics and probability are intertwined, and this chapter reviews the probability tools we will need for statistical inference. It starts with one random variable and general properties like expectation and variance. The specific properties of some common probability models—those we will use frequently in later chapters—are collected together as a resource. Most statistical work involves samples of more than one observation, and hence we also need to review results for several random variables, including their joint distribution and properties of their sum or arithmetic mean. Finally, the chapter outlines the use of moment generating functions as a relatively simple tool for obtaining properties, particularly those of sums and linear functions of random variables, as needed for statistical work involving sample totals or sample means. 

### 1.1 Discrete and Continuous Random Variables

In our journey through this book we will meet random variables that take either discrete values (e.g., integers) or continuous values (e.g., positive real numbers). In both instances we denote the random variable by an upper case letter like Y and its values by the corresponding lower case letter, y. 

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

1-2

# CHAPTER 1. PROBABILITY TOOLS

### 1.1.1 Probability mass function and probability density function

The distribution of Y over its possible values is denoted by \( f_Y(y) \). For a discrete random variable, \( f_Y(y) \) can be interpreted as \( \Pr(Y = y) \), the probability that \( Y \) takes the value \( y \), and \( f_Y(y) \) is called a probability mass function (PMF). The mass function is positive and sums to 1 over the possible \( y \) values. 

**Example 1.1 (Poisson PMF)**

If \( Y \) has a Poisson distribution, it has possible values \( y = 0, 1, \ldots, \infty \) and PMF 

\[
f_Y(y) = \frac{e^{-\mu} \mu^y}{y!}.
\] 

The Poisson distribution is actually a family of distributions depending on the value of the parameter \( \mu > 0 \), and we will use the notation \( \text{Pois} (\mu) \) to denote the family. (The properties of the Poisson and other commonly used distributions will be summarized in Sections 1.4 and 1.5.) In practice, the value of \( \mu \) is usually unknown for a specific application, and much of our statistical work will be about how to estimate the values of parameters like \( \mu \) from a sample of data. The Poisson PMF sums to 1, as required:

\[
\sum_{y=0}^{\infty} f_Y(y) = \sum_{y=0}^{\infty} \frac{e^{-\mu} \mu^y}{y!} = e^{-\mu} \sum_{y=0}^{\infty} \frac{\mu^y}{y!} = e^{-\mu} e^{\mu} = 1,
\]

because of the series representation \( 1 + \mu + \frac{\mu^2}{2!} + \cdots \) for \( e^{\mu} \). 

♢♢♢

(The end of an example is marked by a ♢♢♢ symbol.)

For a continuous random variable, \( f_Y(y) \) is called a probability density function (PDF), and \( f_Y(y) \) cannot be interpreted as a probability. It is, however, proportional to the probability that \( Y \) falls in a small interval around \( y \) (Exercise 1.1). The density function is positive and integrates to 1 over the range of possible \( y \) values. 

**Example 1.2 (Exponential distribution: PDF)**

If \( Y \) has an exponential distribution, it has possible values \( 0 < y < \infty \) and PDF 

\[
f_Y(y) = \lambda e^{-\lambda y}
\]

\((0 < y < \infty; \lambda > 0)\). The distribution, denoted \( \text{Expon} (\lambda) \), depends on the parameter \( \lambda > 0 \). The exponential PDF integrates to 1, as required:

\[
\int_{0}^{\infty} f_Y(y) dy = \int_{0}^{\infty} \lambda e^{-\lambda y} dy = -e^{-\lambda y} \big|_{y=0}^{y=\infty} = 0 - (-1) = 1.  
\] 

♢♢♢

A distribution is symmetric if there exists \( \mu \) such that its PMF or PDF can be written

\[
f_Y(\mu - x) = f_Y(\mu + x,
\]

for values \( x \) that generate all possible values \( y \).
```