Here's the converted text formatted in precise Markdown code:

```markdown
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

1-16

# CHAPTER 1. PROBABILITY TOOLS

### (b) Log base 10 of PDF

```
0.0

−3.0

0.1

−2.5

0.2

fY(y)
0.3
0.4

0.5

Log base 10 of fY(y)
−2.0
−1.5
−1.0

0.6

Laplace
Standard normal

−0.5

0.7
```

### (a) PDF
```
−4

−2

0
y

2

4

−4

−2

0
y

2

4
```

**Figure 1.3**: PDFs of the Laplace and normal distributions: Lap \( \mu = 0, \phi = 1/ 2 \) (solid line) versus \( N (\mu = 0, \sigma^2 = 1) \) (dashed line). The two distributions have the same variance: \( 2\phi^2 = \sigma^2 = 1 \). *(a) PDF and (b) log base 10 of the PDF*

### 1.5.4 Laplace distribution

The Laplace distribution is also known as the double-exponential, because the PDF decays exponentially on the left and on the right of the location parameter \( \mu \). Note that the decay, \( \exp(−|y − \mu|/\phi) \), is a function of the absolute distance from \( \mu \), in contrast to the normal distribution’s decay with squared distance, \( \exp(− \frac{1}{2\sigma^2} (y − \mu)^2 ) \). Thus, even if the two distributions have the same variance \( (2\phi^2 = \sigma^2) \), the Laplace distribution has fatter tails, as illustrated in **Figure 1.3**. The use of log scale for the PDFs in **Figure 1.3(b)** emphasizes that the Laplace PDF is relatively much larger in the tails. The Laplace distribution is therefore useful in statistics for modeling data with outlying observations. 

### 1.5.5 Normal distribution

The normal distribution has great importance in statistical work, and Chapter 2 is devoted to it. 

### 1.5.6 Log-normal distribution

By definition, \( Y \) has a log-normal distribution denoted \( \text{logN} (\mu, \sigma^2) \) distribution if \( Z = \ln(Y) \) has a \( N(\mu, \sigma^2) \) distribution. Note that in the definition, \( \mu \) and \( \sigma^2 \) are the mean and variance after applying the log transformation, and not the mean and variance of \( Y \). Having positive support, the log-normal distribution is useful for modeling quantities such as losses in actuarial science, precipitation over a period of time, etc. 

### 1.5.7 \( \chi^2, F, \) and \( t \) distributions

These distributions arise from IID normal random variables, particularly through their sample mean and sample variance. Properties of the \( \chi^2, F, \) and \( t \) distributions are developed in Chapter 2. 

### 1.5.8 Uniform distribution

The uniform distribution is a special case of the beta distribution: a \( \text{Beta}(0, 0) \) random variable has a \( \text{Unif}(0, 1) \) distribution, and the latter can easily be rescaled to have range \( (a, b) \). Like the beta, the uniform finds most utility in this book for Bayesian inference (Chapter 6), where a uniform distribution on a parameter is often taken to represent no prior information about the value of the parameter. 

## 1.6 FUNCTION OF A RANDOM VARIABLE

### 1.6.1 PDF of a function of a continuous random variable

Suppose the PDF of a random variable \( Y \) is known, but we are interested in the function \( g(Y) \). It is easy to write down the PDF of the new random variable \( g(Y) \), if \( g(·) \) is a monotonic function. 

**Example 1.12** *(PDF of a scaled exponential random variable)*

Let \( Y \sim \text{Expon}(\lambda) \), where the notation “∼” stands for “is distributed as”. For instance, suppose \( Y \) is the time in years between earthquakes in a region. Then, as described in Section 1.5, \( \lambda \) is interpreted as the rate of occurrences per year. If we change the time scale to months, then \( Y \) becomes \( 12Y \), a simple function of \( Y \). 

What is the PDF of \( Z = 12Y \)? From the definition of the CDF,
\[
F_Z(z) = \Pr(Z < z) = \Pr(Z/12 < z/12) = \Pr(Y < z/12) = F_Y(z/12) = 1−e^{−\lambda z/12},
\]
where the last equality is obtained by evaluating the exponential CDF for \( Y \) at \( y = z/12 \). Then differentiating,
\[
f_Z(z) = \frac{d}{dz}F_Z(z) = (1 − e^{−\lambda z/12}) = \left(\frac{\lambda}{12}\right)e^{−(\lambda/12)z}. 
\]

This is seen to be the PDF of an exponential random variable, except that the original rate of occurrence \( \lambda \) per year becomes \( \lambda/12 \) per month, which is intuitive. ♢♢♢

The derivation in **Example 1.12** used an explicit expression for the exponential CDF, and it may be easier to see the argument that way, but closer inspection shows that the CDF could be used implicitly. Writing \( Z = g(Y) \), where \( g(Y) = 12Y \), and \( Y = g^{-1}(Z) \), where \( g^{-1}(Z) = Z/12 \), we see that the argument boils down to differentiating the CDF of \( Y \) as a function of \( z \) and applying the chain rule:
\[
f_Z(z) = \frac{dF_Z(z)}{dz} = \frac{dF_Y(g^{-1}(z))}{dz} \cdot \frac{dg^{-1}(z)}{dz} = f_Y(g^{-1}(z)).
\]
The CDF of \( Y \) is not explicitly required, as differentiating the CDF returns to the PDF, a handy feature for distributions like the normal with no closed form for the CDF. This type of computation can be done in general for transformations \( Z = g(Y) \), where \( g(·) \) is a differentiable, monotonic function:
\[
f_Z(z) = \frac{dg^{-1}(z)}{dz} f_Y(g^{-1}(z)),
\]
(1.3)

where the absolute value takes care of monotonic decreasing functions. 

**Example 1.13** *(PDF of the log-normal distribution from the normal)*

By definition, \( Z \) has a log-normal distribution denoted \( \text{logN}(\mu, \sigma^2) \) if \( Y = \ln(Z) \) has a \( N(\mu, \sigma^2) \) distribution. Thus, \( Y \) and \( Z \) are related by the monotonic functions \( Z = g(Y) = \exp(Y) \) and \( Y = g^{-1}(Z) = \ln(Z) \), and the log-normal PDF of \( Z \) may be obtained via (1.3) from the normal PDF of \( Y \) in Table 1.4:
\[
f_Z(z) = \frac{1}{z} \cdot f_Y(g^{-1}(z)) = \frac{1}{z} \cdot f_Y(\ln(z)) = \frac{1}{\sqrt{2\pi\sigma^2}} \cdot e^{-\frac{1}{2\sigma^2}(\ln(z)−\mu)^2} \cdot \frac{1}{z}.
\]
♢♢♢

### 1.6.2 Expectation of a function of a random variable

Suppose the random variable \( Y \) is transformed to \( Z = g(Y) \), where \( g(·) \) is a known function. Because \( Y \) is random, so is \( Z \), and the distribution of \( Z \) has properties such as expectation. An extension of Definition 1.1 gives \( E(g(Y)) \). 

### Definition 1.4 *(Expectation of a function of random variable)*

The expected value of \( g(Y) \) is given by the sum
\[
E(g(Y)) = \sum g(y)f_Y(y)
\]
if \( Y \) takes discrete values, or by the integral
\[
E(g(Y)) = \int g(y)f_Y(y) \, dy 
\]
if \( Y \) takes continuous values. The integral or sum is over all possible values \( y \). 

Again, the expectation is defined only if \( \int |g(y)|f_Y(y) \, dy \), respectively, is finite. Thus, depending on the function \( g(·) \), \( Z \) could have a well-defined (finite) expectation whether \( Y \) does or not. 

**Example 1.14** *(Expectation of log uniform)*

A chemist represents her uncertainty about the concentration of a chemical species by thinking of it as a random variable, \( Z \). Chemists often work on log scales for concentrations, and she thinks \( Y = \ln(Z) \) has a continuous uniform distribution, 
\[
\frac{1}{b−a} \quad (a < y < b),
\]
where \( a \) and \( b \) are known bounds. (Log base 10 would be used in practice by chemists, but it’s easier mathematically to work with natural logs.) But what is the expected value of the unlogged concentration, \( Z = g(Y) = e^Y \)? 

We have
\[
E(Z) = \int_a^b e^y f_Y(y) \, dy = \int_a^b \frac{1}{b-a} e^y \, dy = \frac{e^b - e^a}{b-a}.
\]

Suppose \( a = \ln(10^{-4}) \) and \( b = \ln(10^{-2}) \), for example, which correspond to unlogged concentrations from \( 10^{-4} \, M \) to \( 10^{-2} \, M \) (M = “mole”). Then the expected concentration is
\[
E(Z) = \frac{10^{-2} - 10^{-4}}{\ln(10^{-2}) - \ln(10^{-4})} = 0.0021 \, M.
\]

Note there is no need to compute the PDF of \( Z \) to obtain its mean here. Alternatively, if we do the work to find the PDF of \( Z \) first, applying the result (1.3) with \( g^{-1}(Z) = \ln(Z) \) we have
\[
f_Z(z) = \frac{d \ln(z)}{dz} f_Y(\ln(z)) = \frac{1}{z(b-a)} \quad (e^{a} < z < e^{b}).
\]

Then we can find \( E(Z) \) from its PDF:
\[
E(Z) = \int_{e^a}^{e^b} z f_Z(z) \, dz = \int_{e^a}^{e^b} z \cdot \frac{1}{(b-a) z} \, dz = \int_{e^a}^{e^b} \frac{1}{(b-a)} \, dz = \frac{(e^b - e^a)}{(b-a)}.
\]
This is the same result as before. 
♢♢♢

A well-known use of the expectation of a function of a random variable is computing the random variable’s variance. From Definition 1.3, we can write
\[
\text{Var}(Y) = E(Y^2) - (E(Y))^2.
\]
The term \( E(Y^2) \) is the expectation of the function \( g(Y) = Y^2 \), which is computed just as in Definition 1.4: see Example 1.11 for instance. 

### 1.7 Several Variables

### 1.7.1 Joint and marginal distributions

Data for statistical models are usually multiple observations, which are considered realizations of random variables for deriving statistical properties of quantities such as sample means and proportions. Thus, probability results for several random variables are of interest. For simplicity, we concentrate here mainly on properties of two random variables; extensions to more than two are fairly immediate. 

Suppose the two random variables are \( Y \) and \( Z \). If both are discrete, the joint PMF, written \( f_{Y,Z}(y, z) \), is the probability that \( Y \) takes the value \( y \) and \( Z \) takes the value \( z \). We could also write
\[
f_{Y,Z}(y, z) = \Pr(Y = y \cap Z = z,
\]
where the intersection symbol “∩” denotes “and”. The joint PMF sums to 1 over all possible \( y \) and \( z \) values. 

For continuous random random variables, the joint PDF \( f_{Y,Z}(y, z) \) integrates to 1 over the possible \( y \) and \( z \) values. The following rules also apply to one discrete and one continuous random variable with appropriate summation or integration. 

The marginal distribution of one of the variables is given by summing or integrating over the other variable. For example, the marginal distribution of \( Y \) is
\[
f_Y(y) =
\begin{cases}
\sum f_{Y,Z}(y, z) & \text{(Z is discrete)} \\
\int f_{Y,Z}(y, z) \, dz & \text{(Z is continuous)}.
\end{cases}
\]

where the summation or integration is over all possible values \( z \). The result here is just a version of the law of total probability, which is discussed further in Section 1.7.2. As one and only value of \( Z \) must occur, the marginal PMF or PDF of \( Y \) for any value \( y \) is obtained by totaling the joint distribution over all possible values of \( z \). Similarly, \( f_Z(z) \) is obtained by summing or integrating over the \( y \) values. 

**Example 1.15** *(HIV vaccination trial: joint and marginal probabilities)*

In recent years, studies like the one examined here have suggested that the search for an effective vaccine against HIV will eventually pay off. A trial in Thailand reported by Rerks-Ngarm et al. (2009) compared vaccination with ALVAC and AIDSVAX against a placebo (no vaccination) in a double-blind, randomized clinical trial involving about 16,000 volunteers. 

We will focus on the “modified intention to treat” data presented by the authors and summarized in Table 1.5. The data are arranged by two variables: whether a subject received a placebo (no treatment) or the vaccine, coded by \( x = 0, 1 \), respectively, and whether the subject is HIV positive at the end of the trial, coded by \( y = 0, 1 \) for no and yes, respectively. 

Thus, random variables \( X \) and \( Y \) take the values \( x = 0, 1 \) and \( y = 0, 1 \), respectively. As this chapter reviews probability, we think of the 16,395 subjects in Table 1.5 as the population of interest, from which the probabilities of various events involving \( X \) and \( Y \) can be calculated. 

Of course, the real problem, the statistical problem from Chapter 2 on, is to estimate such probabilities, regarding the data as a random sample from a bigger population. Considering the 16,395 subjects in the trial as the population of interest, suppose a subject is sampled at random from the 16,395. From the observed frequencies in Table 1.5, we can compute, for instance, the joint probability that \( X \) takes the value 0 and \( Y \) takes the value 1:
\[
f_{X,Y}(0, 1) = \Pr(X = 0 \cap Y = 1) = \frac{74}{16,395}.
\]

The probabilities for the other values of \( X \) and \( Y \) are analogous. Marginal probabilities, i.e., probabilities relating to only one variable, can be calculated directly or via (1.4). For a randomly chosen subject, for instance,
\[
f_Y(1) = \Pr(Y = 1) = \frac{125}{16,395}
\]

or equivalently by summing joint probabilities over the two possible values of \( X \),
\[
f_Y(1) = f_{X,Y}(0, 1) + f_{X,Y}(1, 1) = \frac{51}{16,395} + \frac{74}{16,395} = \frac{125}{16,395}.
\]
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

## 1.7.2 Conditional distributions

Conditioning allows the PMF or PDF of one or more random variables to depend on the value(s) of one or more other variables. For simplicity, we will again consider just two random variables, \( Y \) and \( Z \) say. Their joint PMF or PDF is related to their marginal and conditional distributions via
\[
f_{Y,Z}(y, z) = f_Y(y)f_{Z|Y}(z | y) = f_Z(z)f_{Y|Z}(y | z)
\]
(1.5)

for all \( y \) such that \( f_Y(y) > 0 \) and all \( z \) such that \( f_Z(z) > 0 \). The symbol “|” is read as “given” or “conditional on”. 

This result builds the joint distribution in two steps: the distribution of \( Y \), then the conditional distribution of \( Z \) given the value of \( Y \); or conversely the distribution of \( Z \), then the conditional distribution of \( Y \) given the value of \( Z \). 

The requirement “for all \( y \) such that \( f_Y(y) > 0 \)” is there as conditioning on the value \( y \) implies that the value has occurred, which in turn implies the value is possible, and similarly the condition \( f_Z(z) > 0 \). Hence, if \( Y \) and \( Z \) are continuous or discrete random variables with joint PMF or PDF \( f_{Y,Z}(y, z) \), by simple rearrangement the conditional distribution of \( Z \) given the value of \( Y \) is
\[
f_{Z|Y}(z | y) = \frac{f_{Y,Z}(y, z)}{f_Y(y)}.
\]
(1.6)
Here we assume \( f_Y(y) > 0 \), which is computed as in (1.4). The other conditional distribution, \( f_{Y|Z}(y | z) \), is analogous. 

**Example 1.16** *(HIV vaccination trial: conditional probability)*

In the context of **Example 1.15**, the random variable of interest is \( Y \), the HIV-infection status, particularly how it depends on \( X \). Technically, we will consider the probability that \( Y = 1 \) (HIV positive) conditional on or given the value of \( X \). For instance, “Is the probability of HIV infection smaller for the vaccine treatment?”

We can compute directly from Table 1.5, for example, the probability that \( Y \) takes the value 1 conditional on \( X \) taking the value 0 (no treatment):
\[
f_{Y|X}(1 | 0) = \Pr(Y = 1 | X = 0) = \frac{74}{8198} \approx 0.0090.
\]

Alternatively, to demonstrate the result in (1.6),
\[
f_{Y|X}(1 | 0) = \frac{\Pr(X = 0 \cap Y = 1)}{\Pr(X = 0)} = \frac{f_{Y,Z}(Y = 1, X = 0)}{f_Y(0)} = \frac{74/16,395}{8198/16,395} \approx 0.0090.
\]

A similar calculation shows that \( f_{Y|X}(1 | 1) = \Pr(Y = 1 | X = 1) \approx 0.0062 \). So, based on these calculations, the treatment reduces the probability of being HIV positive for these 16,395 subjects. The statistical question to be addressed in later chapters is whether the apparent efficacy of the vaccine can be explained by chance variation. ♢♢♢

As already noted, the rule in (1.4) for obtaining the marginal distribution of one random variable from its joint distribution with another is a version of the law of total probability. Another version follows by rewriting \( f_{Y,Z}(y, z) \) according to marginal and conditional distributions, as in (1.5). Thus, we have two ways of writing the law of total probability for two random variables. (The law is often written in terms of probabilities of events, which carries over immediately to discrete random variables. For continuous random variables, “probability” is interpreted as a PDF.)

### Theorem 1.2 *(Law of total probability)*

Let \( f_{Y,Z}(y, z) \) be the joint PMF or PDF of the random variables \( Y \) and \( Z \) with values \( y \) and \( z \), respectively. The marginal distribution of \( Y \) is given by
\[
f_Y(y) = 
\begin{cases}
\sum f_{Y,Z}(y, z) & \text{(Z is discrete)} \\
\int f_{Y,Z}(y, z) \, dz & \text{(Z is continuous)}.
\end{cases}
\]

or equivalently by
\[
f_Y(y) = 
\begin{cases}
\sum f_Z(z)f_{Y|Z}(y | z) & \text{(Z is discrete)} \\
\int f_Z(z)f_{Y|Z}(y | z) \, dz & \text{(Z is continuous)}.
\end{cases}
\]

where the summation or integration is over all values \( z \) with \( f_Z(z) > 0 \). 

### 1.7.3 Statistical independence

Independence of random variables is an assumption we will often, indeed nearly always, be making for the statistical models in later chapters. 

### Definition 1.5 *(Statistical independence)*

Two random variables \( Y \) and \( Z \) with joint PDF or PMF \( f_{Y,Z}(y, z) \) are statistically independent if and only if the following equivalent conditions hold. 
1. The joint distribution factorizes as the product of the two marginal distributions:
   \[
   f_{Y,Z}(y, z) = f_Y(y)f_Z(z)
   \]
   (for all \( y, z \)). 
2. The conditional distribution of \( Y \) does not depend on the value of \( Z \):
   \[
   f_{Y|Z}(y | z) = f_Y(y) \quad \text{(for all \( y \) and \( z \) such that \( f_Z(z) > 0 \))}. 
   \]
3. The conditional distribution of \( Z \) does not depend on the value of \( Y \):
   \[
   f_{Z|Y}(z | y) = f_Z(z) \quad \text{(for all \( y \) and \( z \) such that \( f_Y(y) > 0 \))}. 
   \]

As the conditions are equivalent, to demonstrate independence it is sufficient to verify just one of them; note it has to hold for all possible values \( y \) and \( z \). To show that two variables are not independent, i.e., dependent, it is sufficient to find one counterexample pair of \( y, z \) values in one condition. The conditions could also be equivalently expressed in terms of CDFs. For example, the first condition becomes
\[
F_{Y,Z}(y, z) = F_Y(y)F_Z(z) \quad \text{(for all \( y, z \))}. 
\]
In later chapters, however, we work more with PMFs and PDFs, hence the use of them in the above definition. 

With more than two random variables, they are pairwise independent if all pairs of them satisfy the above conditions. They are mutually independent if their joint distribution factorizes as a product of all their marginal distributions, with similar definitions for the other equivalent conditions. When authors say just “independent”, then “mutually independent” is usually assumed by default. 

### 1.7.4 Random sample

Mutual independence is also usually implied for a “random sample” of size \( n \) from some distribution. The sample of size \( n \) comprises \( n \) random variables over possible samples, and the random variables are independent in the sense that the distribution of the second draw from the distribution does not depend on the value of the first draw, etc. As the random variables are drawn from the same distribution, we also have the “identically distributed” part of “IID”. Hence, “random sample from a distribution” and “IID random variables” are usually taken as synonymous. In contrast, random sampling from a finite population without replacement would give at best approximate independence: the first draw changes the membership of the finite population, affecting the population available for the second draw, and so on. 

### 1.7.5 Covariance

Two random variables have a covariance, and several random variables have pairwise covariances. As well as being useful in their own right, covariances are sometimes necessary to compute the variance of a linear combination of random variables. 

In general, the covariance between two random variables \( Y \) and \( Z \)—discrete, continuous, or a mixture thereof—is defined as
\[
\text{Cov}(Y, Z) = E((Y − \mu_Y)(Z − \mu_Z)) = E(YZ) − \mu_Y \mu_Z.
\]
(1.7)

where \( \mu_Y \) and \( \mu_Z \) are \( E(Y) \) and \( E(Z) \), respectively. The equivalence of the definitions is easily verified by multiplying out the product and applying expectation of a linear combination. The computation of \( E(YZ) \) is again via a weighted average of possible values, with the weights now given by the joint distribution \( f_{Y,Z}(y, z) \). If \( Y \) and \( Z \) both take discrete values, for example, then
\[
E(YZ) = \sum\sum y z f_{Y,Z}(y, z)
\]
where the double sum is over the possible combinations of \( y \) and \( z \) values. If one or both of the random variables are continuous, then one or both of the sums becomes an integral. 

From the definition of covariance, we immediately have
\[
\text{Cov}(Y, Z) = \text{Cov}(Z, Y)
\]
and
\[
\text{Cov}(Y, Y) = \text{Var}(Y).
\]
These identities are much used in mathematical manipulations. 

Often, the correlation between \( Y \) and \( Z \),
\[
\rho(Y, Z) = \frac{\text{Cov}(Y, Z)}{\sqrt{\text{Var}(Y) \text{Var}(Z)}}
\]
(1.8)
is easier to interpret. It is on the scale \( -1 \leq \rho(Y, Z) \leq 1 \), and measures the strength of the linear relationship (negative or positive) between \( Y \) and \( Z \). 

**Example 1.17** *(Final-exam and quiz grades: covariance)*

For the joint distribution in Table 1.1, we have already computed \( \mu_Y = 84, \mu_Z = 71, \) and \( \text{Var}(Y) = 144 \). Similarly, \( \text{Var}(Z) = 189 \). Using (1.7) we find that
\[
\text{Cov}(Y, Z) = (60 − 84)(50 − 71)(0.1) + \cdots = 36.
\]
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

Hence, from (1.8),
\[
\rho(Y, Z) = \frac{36}{\sqrt{144 \cdot 189}} \approx 0.218.
\]
*(What features of Table 1.6 lead to a mildly positive correlation here?)*

♢♢♢

If \( Y \) and \( Z \) are independent, then \( E(YZ) = E(Y)E(Z) \) and \( \text{Cov}(Y, Z) = 0 \). The converse, that covariance of zero implies independence, is not true in general. 

**Example 1.18** *(Covariance of zero does not imply independence)*

As a simple counter-example to a claim that zero covariance always implies independence, let \( Y \sim \text{Unif}(-1, 1) \) and \( Z = Y^2 \). Clearly, the distribution of \( Z \) depends on the value taken by \( Y \), and from Definition 1.5 they are not independent. 

Their covariance is
\[
\text{Cov}(Y, Z) = E(YZ) − E(Y)E(Z) = E(Y^3) − E(Y)E(Z) = 0 − 0 \cdot E(Z) = 0,
\]
where \( E(Y) = 0 \) and \( E(Y^3) = 0 \) follow because \( Y \) is symmetric around 0. Thus, the covariance between \( Y \) and \( Z \) is zero but they are not independent. ♢♢♢

A covariance of zero does imply independence in the special case of the bivariate normal distribution. If \( Y \) and \( Z \) are bivariate normal with \( \text{Cov}(Y, Z) = 0 \), then \( Y \) and \( Z \) are independent normal random variables, a result shown in Section 1.7.9. 

### 1.7.6 Expectation of a linear combination of random variables

Linear combinations of random variables arise very frequently throughout statistical science. 

In general, suppose we have a linear combination,
\[
a_0 + \sum_{i=1}^{n} a_i Y_i,
\]
of \( n \) random variables, \( Y_1, \ldots , Y_n \). Here, \( a_0, \ldots , a_n \) are constants (not random). Then
\[
E\left(a_0 + \sum_{i=1}^{n} a_i Y_i\right) = a_0 + \sum_{i=1}^{n} a_i E(Y_i).
\]
(1.9)

All expectations must exist. Other than that requirement, there are no further conditions. In particular, the result holds whether the \( Y_i \) are independent or not. 

Important special cases of the general result (1.9) include the expectation of a linear function of a single random variable,
\[
E(a_0 + a_1 Y) = a_0 + a_1 E(Y)
\]

and the expectation of a sum of random variables,
\[
E(Y_1 + Y_2) = E(Y_1) + E(Y_2).
\]
These special cases are proved as Exercise 1.14. 

Note also that other definitions of “average” or “location of a distribution” such as the median or mode do not obey such rules. Expectation is a sum or integral and is therefore a linear operator. If expectation is combined with another linear operator, like a linear combination, the order of operations can be interchanged. When using this rule in deriving another result, it is helpful to include a statement such as “the expectation of a linear combination of random variables is the linear combination of their expectations” to explain the step in the argument. 

**Example 1.19** *(Course grade: expectation of a linear combination)*

Let \( Y \) be the final-grade random variable defined in Table 1.1. We now also have the random variable \( Z \), the grade from the quizzes, taking the value \( z \), which is either 50% or 80%. A randomly chosen student will have a value for \( Y \) and a value for \( Z \). Table 1.6 gives the joint distribution, \( f_{Y,Z}(y, z) \), for this situation. For example, the probability that \( Y \) takes the value 60 and \( Z \) takes the value 50 is 0.1. 

By summing across the rows of the table we obtain the probability mass function \( f_Y(y) \) in Table 1.1. Similarly, by summing down the columns we obtain \( f_Z(z) \). (We should really write \( f_Y(y) \) and \( f_Z(z) \), respectively, to distinguish the two functions. Often, the arguments are used to distinguish the functions, even though this is sloppy mathematically.) The probability distributions \( f_Y(y) \) and \( f_Z(z) \) are called marginal distributions, because they are derived from the margins of the \( f_{Y,Z}(y, z) \) table. It is easily verified that \( E(Z) = 71 \). 

The overall course grade, \( G \), is important. To simplify, let us ignore the lab component and say
\[
G = 0.55Y + 0.45Z.
\]
Note that the weights in the linear combination are non-random. From first principles, we could compute \( E(G) \) from the PMF, \( f_G(g) \), for \( G \). 

Using the joint distribution in Table 1.6, \( f_G(g) \) is given in Table 1.7. For example, \( G \).
© Copyright William J. Welch 2009–2019. All rights reserved.
```

This Markdown maintains the structure, mathematical notation, and emphasis as outlined in your instructions.