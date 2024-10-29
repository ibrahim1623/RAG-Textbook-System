```markdown
# Statistical Inference: A Primer on Likelihood and Bayesian Methods

## Introduction to Statistical Inference

Course Notes Prepared by  
William J. Welch  
Department of Statistics  
University of British Columbia  
3182 Earth Sciences Building  
2207 Main Mall  
Vancouver BC, Canada V6T 1Z4  

Version: August 14, 2019  

© Copyright William J. Welch 2009–2019  

All rights reserved. Contents  
1. Probability Tools  
   1.1 Discrete and Continuous Random Variables . . . . . . . . . . . .. . 1-1  
   1.1.1 Probability mass function and probability density function . . 1-2  
   1.1.2 Cumulative distribution function . . . . . . . . . . . . . . . . 1-3  
   Mean, Median, and Mode . . . . . . . . . . . . . . . . . . . . . . . . 1-4  
   1.2.1 Mean or expectation . . . . . . . . . . . . . . . . . . . . . . . 1-4  
   1.2.2 Median . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1-6  
   1.2.3 Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1-6  
   Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1-7  
   1.3.1 Computation . . . . . . . . . . . . . . . . . . . . . . . . . . 1-7  
   1.3.2 Standard deviation .. . . . . . . . . . . . . . . . . . . . . . . 1-9  
   1.3.3 Chebyshev’s inequality . . . . . . . . . . . . . . . . . . . .. . 1-9  
   Commonly Used Discrete Distributions .. . . . . . . . . . . . .. . 1-9  
   1.4.1 Bernoulli distribution .. . . . . . . . . . . . . . . . . . . . . 1-11  
   1.4.2 Binomial distribution .. . . . . . . . . . . . . . . . . . . . . . 1-11  
   1.4.3 Geometric distribution . . . . . . . . . . . . . . . . . . . . . . 1-11  
   1.4.4 Negative-binomial distribution . . . . . . . . . . . . . . . . . 1-12  
   1.4.5 Poisson distribution . . . . . . . . . . . . . . . . . . . . . . . 1-12  
   Commonly Used Continuous Distributions .. . . . . . . . . . . .. . 1-12  
   1.5.1 Beta distribution .. . . . . . . . . . . . . . . . . . . . . .. . 1-12  
   1.5.2 Exponential distribution .. . . . . . . . . . . . . . . . . . . . 1-14  
   1.5.3 Gamma distribution .. . . . . . . . . . . . . . . . . . . .. . 1-14  
   1.5.4 Laplace distribution .. . . . . . . . . . . . . . . . . . . .. . 1-16  
   1.5.5 Normal distribution .. . . . . . . . . . . . . . . . . . . .. . 1-16  
   1.5.6 Log-normal distribution .. . . . . . . . . . . . . . . . . .. . 1-16  
   1.5.7 χ², F, and t distributions .. . . . . . . . . . . . . . . . . . . 1-17  
   1.5.8 Uniform distribution .. . . . . . . . . . . . . . . . . . . .. . 1-17  
   Function of a Random Variable .. . . . . . . . . . . . . . . . . .. . 1-17  
   1.6.1 PDF of a function of a continuous random variable .. . .. . 1-17  
   1.6.2 Expectation of a function of a random variable .. . . . . . . 1-18  
   Several Variables . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 1-20  
   1.7.1 Joint and marginal distributions .. . . . . . . . . . . . .. . 1-20  
   1.7.2 Conditional distributions . . . . . . . . . . . . . . . . . . . . 1-22  
   1.7.3 Statistical independence .. . . . . . . . . . . . . . . . . . . . 1-23  
   1.7.4 Random sample .. . . . . . . . . . . . . . . . . . . . . . . . . 1-24  
   1.7.5 Covariance .. . . . . . . . . . . . . . . . . . . . . . . . .. . 1-25  
   1.7.6 Expectation of a linear combination of random variables . . . 1-26  
   1.7.7 Variance of a linear combination of random variables .. . . . 1-28  
   1.7.8 Covariance between linear functions or combinations of random variables .. . . . . . . . . . . . . . . . . . . . . . . . . .. . 1-29  
   1.7.9 Bivariate normal distribution .. . . . . . . . . . . . . . . . . 1-30  
   Moment Generating Functions .. . . . . . . . . . . . . . . . . . . 1-22  
   1.8.1 Uses of moment generating functions . . . . . . . . . . .. . 1-31  
   1.8.2 Definition of the moment generating function .. . . . . .. . 1-32  
   1.8.3 Finding moments from the MGF .. . . . . . . . . . . . .. . 1-35  
   1.8.4 MGF of a linear function or a sum .. . . . . . . . . . . .. . 1-38  
   1.8.5 The MGF identifies a distribution .. . . . . . . . . . . . . . 1-38  
   Getting It Done in R . . . . . . . . . . . . . . . . . . . . . . . . . . . 1-40  
   1.10 Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . . . . 1-43  
   1.11 Exercises .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 1-45  
   
## The Normal Distribution in Statistics  

1. Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 2-1  
2. Some Properties of the Normal Distribution .. . . . . . . . . . .. . 2-2  
3. Distributions Derived From the Normal .. . . . . . . . . . . . . . . . 2-2  
   3.1 The χ distribution . . . . . . . . . . . . . . . . . . . . . . . 2-2  
   3.2 The t distribution . . . . . . . . . . . . . . . . . . . . . . . . 2-4  
   3.3 The F distribution . . . . . . . . . . . . . . . . . . . . . .. . 2-7  
   3.4 Estimating the Parameters of the Normal .. . . . . . . . . . . . . . 2-8  
   © Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14  

4. Distribution of the sample mean (known variance) . . . .. . 2-9  
5. Distribution of the sample variance .. . . . . . . . . . . .. . 2-10  
6. Distribution of the standardized sample mean (unknown variance) .. . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 2-11  
7. Limiting Normal Distributions .. . . . . . . . . . . . . . . . . . .. . 2-14  
   7.1 Convergence in distribution .. . . . . . . . . . . . . . . .. . 2-14  
   7.2 Limiting distributions and large-sample approximations in statistics .. . . . . . . . . . . . . . . . . . . . . . . .. . 2-16  
   7.3 Central limit theorem .. . . . . . . . . . . . . . . . . . . . . 2-18  
8. Getting It Done in R . . . . . . . . . . . . . . . . . . . . . . . . .. . 2-19  
   8.1 Sample mean, standard deviation, and variance .. . . . .. . 2-19  
   8.2 Quantiles of the t distribution .. . . . . . . . . . . . . . .. . 2-19  
   8.3 Limiting normal distributions .. . . . . . . . . . . . . . .. . 2-20  
9. Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . .. . 2-20  
10. Exercises .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2-22  
11. Appendix: Proof of Lemma 2.2 . . . . . . . . . . . . . . . . . . .. . 2-31  
12. Appendix: Proof of the Central Limit Theorem .. . . . . . . . . . . 2-32  

## Statistical Estimation  

1. Statistical Models: The Role of Probability . . . . . . . . . . . . . . . 3-1  
2. The Frequentist Philosophy . . . . . . . . . . . . . . . . . . . . . . . 3-2  
3. Properties of an Estimator . . . . . . . . . . . . . . . . . . . . . . . 3-7  
4. Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3-7  
5. Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3-7  
6. Mean squared error . . . . . . . . . . . . . . . . . . . . . . . . 3-7  
7. Practical perspective . . . . . . . . . . . . . . . . . . . . . . . 3-9  
8. Consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3-10  
9. Relative Error . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3-12  
10. Comparing Estimators . . . . . . . . . . . . . . . . . . . . . . . . . . 3-14  
11. Getting It Done in R . . . . . . . . . . . . . . . . . . . . . . . . . . . 3-14  
12. Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . . . . 3-15  
13. Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 3-15  

## Maximum Likelihood Estimation  

1. Maximum Likelihood Estimation: Basic Ideas .. . . . . . . . . . . . 4-1  
2. What is a likelihood function and why maximize it? . . . .. . 4-1  
3. Maximum likelihood estimates in general .. . . . . . . . .. . 4-8  
4. Properties of Maximum Likelihood Estimators .. . . . . . . . . . . 4-11  
5. Consistency of the ML Estimator . . . . . . . . . . . . . . . . . .. . 4-11  
6. Regularity conditions . . . . . . . . . . . . . . . . . . . . . . . 4-13  
7. Large-Sample Variance of the ML Estimator . . . . . . . . . . . 4-14  
8. Observed information . . . . . . . . . . . . . . . . . . . . . . 4-15  
9. Fisher information .. . . . . . . . . . . . . . . . . . . . .. . 4-20  
10. Observed versus Fisher information .. . . . . . . . . . . . . . 4-24  
11. Large-sample normality of the maximum likelihood estimator .. 4-25  
12. Confidence Intervals From the ML Estimator .. . . . . . . . . . . 4-28  
13. Large-sample approximations . . . . . . . . . . . . . . . .. . 4-28  
14. Parameter transformation for better approximation .. . . . . 4-32  
15. Getting It Done in R . . . . . . . . . . . . . . . . . . . . . . . . .. . 4-34  
16. Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . . . . 4-35  
17. Exercises .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 4-36  
18. Appendix: Equivalence of Observed and Fisher Information .. . . 4-46  

## Maximum Likelihood Estimation: Several Parameters  

1. Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 5-1  
2. Maximum likelihood estimates .. . . . . . . . . . . . . . . . . . . 5-1  
3. Large-sample unbiasedness of ML estimators . . . . . . . . . . . . . 5-3  
4. Large-Sample Variances and Covariances of ML Estimators . . . .. . 5-4  
5. Confidence Intervals .. . . . . . . . . . . . . . . . . . . . . . . .. . 5-6  
6. Censored Data .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5-8  
7. Computation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5-11  
8. Getting It Done in R . . . . . . . . . . . . . . . . . . . . . . . . .. . 5-12  
9. Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . . . . 5-13  
10. Exercises .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5-14  

## Bayesian Estimation  

1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6-1  
2. Bayes’ Rule .. . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 6-2  
3. Bayesian Posterior Distribution of a Parameter .. . . . . . . . . . . 6-6  
4. Bayesian Credible Intervals . . . . . . . . . . . . . . . . . . . . .. . 6-14  
5. Normal Distribution .. . . . . . . . . . . . . . . . . . . . . . . . . . 6-16  
6. Priors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6-24  
7. Bayesian Predictive Distributions . . . . . . . . . . . . . . . . . . . . 6-25  
8. Computation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6-27  
9. Bayesian Versus Frequentist Paradigms . . . . . . . . . . . . . . . . . 6-30  
10. Getting It Done in R .. . . . . . . . . . . . . . . . . . . . . . . . . . 6-31  
    10.1 Monte Carlo predictive distribution . . . . . . . . . . . . .. . 6-31  
    10.2 Gibbs sampling from the posterior distribution .. . . . .. . 6-31  
11. Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . .. . 6-32  
12. Exercises .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 6-33  

## Hypothesis Testing  

1. Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 7-1  
2. What is a Hypothesis Test? . . . . . . . . . . . . . . . . . . . . .. . 7-1  
3. Formulation of a Hypothesis Test .. . . . . . . . . . . . . . . . .. . 7-4  
4. Tests Based on the Likelihood Ratio .. . . . . . . . . . . . . . . . . 7-10  
   4.1 Neyman-Pearson Lemma . . . . . . . . . . . . . . . . . . . . . 7-10  
   4.2 Composite hypotheses . . . . . . . . . . . . . . . . . . . .. . 7-17  
5. Generalized likelihood ratio tests .. . . . . . . . . . . . . . . . .. . 7-20  
6. Normal Distribution: Testing µ With σ² Unknown .. . . . . . .. . 7-25  
7. p-values .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 7-30  
8. Practical Significance Versus Statistical Significance . . . . . . . . . . 7-33  
9. Connection With Confidence Intervals .. . . . . . . . . . . . . . . . 7-34  
10. Getting It Done in R . . . . . . . . . . . . . . . . . . . . . . . . .. . 7-37  
11. Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . .. . 7-38  
12. Exercises .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7-40  
13. Appendix: Sketch proof of Wilks’ Theorem . . . . . . . . . . . . . . 7-52  

## Analysis of Categorical Data  

1. The Multinomial Distribution . . . . . . . . . . . . . . . . . . . .. . 8-1  
2. Maximum Likelihood Estimation .. . . . . . . . . . . . . . . . . . . 8-3  
3. Hypothesis Tests for the Multinomial . . . . . . . . . . . . . . . .. . 8-5  
   3.1 Generalized likelihood ratio tests .. . . . . . . . . . . . . . . 8-5  
   3.2 Pearson’s statistic . . . . . . . . . . . . . . . . . . . . . . . . 8-9  
4. Goodness of Fit Tests . . . . . . . . . . . . . . . . . . . . . . . . . . 8-10  
5. Getting It Done in R . . . . . . . . . . . . . . . . . . . . . . . . .. . 8-18  
6. Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . . . . 8-19  
7. Exercises .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 8-20  

## Comparative Studies  

1. Independent Versus Paired Samples .. . . . . . . . . . . . . . . .. . 9-1  
2. Two Independent Samples .. . . . . . . . . . . . . . . . . . . . .. . 9-2  
   2.1 Likelihood methods .. . . . . . . . . . . . . . . . . . . .. . 9-2  
   2.2 Methods for the normal distribution .. . . . . . . . . . . . . 9-9  
3. Several Independent Multinomial Samples .. . . . . . . . . . . . . 9-12  
4. Two-Way Contingency Tables . . . . . . . . . . . . . . . . . . . . . . 9-15  
5. Paired Samples .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9-17  
   5.1 Paired data .. . . . . . . . . . . . . . . . . . . . . . . . .. . 9-17  
   5.2 Model for difference data . . . . . . . . . . . . . . . . . . 9-18  
   5.3 Estimation and hypothesis testing .. . . . . . . . . . . . . . 9-19  
   5.4 Statistical advantages of paired data . . . . . . . . . . . . . . 9-22  
6. Getting It Done in R . . . . . . . . . . . . . . . . . . . . . . . . .. . 9-24  
   6.1 Several multinomial samples or a contingency table .. . . . 9-24  
   6.2 Paired data .. . . . . . . . . . . . . . . . . . . . . . . . .. . 9-25  
7. Learning Outcomes .. . . . . . . . . . . . . . . . . . . . . . . . . . . 9-25  
8. Exercises .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9-27  

## Solutions  

## Bibliography  

## List of Tables  

1. Probability mass function for the final-exam grade . . . . . . . . .. . 1-4  
2. Binomial PMF and CDF for n = 3 trials and probability of success π = 1/4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 1-6  
3. Some commonly used discrete distributions .. . . . . . . . . . . .. . 1-10  
4. Some commonly used continuous distributions .. . . . . . . . . .. . 1-13  
5. HIV vaccine: two-way frequency table by treatment and HIV-infection status .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . 1-21  
6. Joint probability function for the final-exam and quiz grades .. . . . 1-27  
7. Probability mass function for the course grade .. . . . . . . . . .. . 1-28  
8. PMF of a negative-binomial random variable with n = 2 and π = 0.1  
9. R functions for the PMF or PDF of some common distributions . . . 1-41  
10. Faults on data lines .. . . . . . . . . . . . . . . . . . . . . . . . .. . 3-2  
11. Sample size to estimate the binomial parameter π: nabs achieves sd(π̃) ≤ 0.015 and nrel achieves sd(π̃)/π ≤ 0.03 .. . . . . . . . . .. . 3-13  
12. R functions to return the PDF, CDF, quantile, or random numbers for the normal distribution .. . . . . . . . . . . . . . . . . . . . . . . . . 3-15  
13. Exponential distribution: approximate variance of λ̃ from observed information compared with the variance over repeated samples .. . 4-18  
14. Faults on data lines of length about 22 km .. . . . . . . . . . . .. . 4-37  
15. Number of expression events for a sample of 298 cell cycles .. . .. . 4-38  
16. Lung function: exact and ML confidence intervals for the normal mean . . . . . . . . . . . 5-7  
17. Conjugate priors for some distributions .. . . . . . . . . . . . . .. . 6-25  
18. Definitions of Type I and Type II errors .. . . . . . . . . . . . .. . 7-2  
19. Normal distribution: rejection regions for testing H0 : µ = µ0 .. . . . 7-26  

## List of Figures  

1. PDF of the exponential distribution . . . . . . . . . . . . . . . . .. . 1-14  
2. PDF of the gamma distribution .. . . . . . . . . . . . . . . . . .. . 1-15  
3. PDFs of the Laplace and normal distributions .. . . . . . . . . .. . 1-16  
4. PDF of the t distribution with 10 degrees of freedom .. . . . . .. . 1-43  
5. Relationships between distributions derived from the normal .. . . . 2-3  
6. PDF of the χ² distribution .. . . . . . . . . . . . . . . . . . . . .. . 2-4  
7. PDF of the t distribution .. . . . . . . . . . . . . . . . . . . . . .. . 2-5  
8. χ²₃ PDF and t₃ PDF as a mixture of normals .. . . . . . . . . . .. . 2-7  
9. PDF of the F distribution .  
```