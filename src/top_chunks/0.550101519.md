```markdown
© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 10-5
## Solution 1.12
1. 0.7 and 0.6, respectively  
2. 0.21 and 0.24, respectively  
3. 0.18  
4. \(E(B) = 1.3\) and \(Var(B) = 0.81\)  

## Solution 1.13
As \(Y = \min(X, k)\) is a function of the random variable \(X\), compute the expectation of a function of a random variable:  
\[
E(Y) = \int_0^{\infty} \min(x, k) \lambda e^{-\lambda x} \, dx.
\]

Then break the integral into two parts:  
\[
E(Y) = \int_0^{k} x \lambda e^{-\lambda x} \, dx + \int_k^{\infty} k \lambda e^{-\lambda x} \, dx. \tag{10.1}
\]

Using the result  
\[
\left( \int ax e^{ax} \, dx = e^{ax} \left( \frac{x}{a} - \frac{1}{a^2} \right) \right)
\]  
with \(a = -\lambda\), the first integral in (10.1) is  
\[
\int_0^{k} x \lambda e^{-\lambda x} \, dx = e^{-\lambda k} \left( \frac{k}{\lambda} - \frac{1}{\lambda^2} \right).
\]

The second integral in (10.1) is immediate from the exponential distribution’s survival function:  
\[
\int_k^{\infty} \lambda e^{-\lambda x} \, dx = \text{Pr}(X > k) = e^{-\lambda k}. 
\]

Putting these results together,  
\[
E(Y) = \lambda \left( e^{-\lambda k} \left( \frac{k}{\lambda} - \frac{1}{\lambda^2} \right) \right) + k e^{-\lambda k} = e^{-\lambda k} \left( 1 - e^{-\lambda k} \right) + k e^{-\lambda k} .
\]

## Solution 1.14
3. Use the two previous results rather than the definition of expectation.  
4. The proof should use \(f_{X,Y}(x, y)\), the joint PDF of \(X\) and \(Y\), without making any assumptions about the joint distribution such as independence.  
5. Use the previous results rather than the definition of expectation.

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 10-6

# CHAPTER 10. SOLUTIONS

## Solution 1.15
There is no need to manipulate integrals or sums. Instead, work with expectations and use the results of Exercise 1.14.  

## Solution 1.16
3. Use the two previous results rather than the definition of variance.  
5. Use the previous results and the result of Exercise 1.15 rather than the definition of variance.  

## Solution 1.19
1. Using the result for the expectation of a linear combination of random variables,  
\[
E(Y) = E(B_1 + \cdots + B_n) = E(B_1) + \cdots + E(B_n) = n\pi. 
\]  
2. Using the result for the variance of a linear combination of random variables,  
\[
Var(Y) = Var(B_1 + \cdots + B_n) = Var(B_1) + \cdots + Var(B_n) = n\pi(1 - \pi),
\]  
because the \(B_i\) are independent and hence all covariance terms are zero.  
3. Using the result for the MGF of a sum of independent random variables,  
\[
M_Y(t) = \prod_{i=1}^{n} M_{B_i}(t) = (1 - \pi + \pi e^t)^n. 
\]  
4. \(\text{Bin}(n, \pi)\), because the MGF identifies the distribution.  

## Solution 1.20
1. exp \(\left( \sum_{i=1}^{n} \mu_i (e^t - 1) \right)\)  
3. Poisson. Be sure to give the value of the Poisson parameter.  

## Solution 1.22
4. \(\text{NegBin}(n, \pi)\)  

## Solution 1.23
1. Follow the steps of Example 1.24.  
2. Note that \(Y\) is a linear function of \(Z\).  
   (a) Use the results on expectation and variance of a linear function of a random variable.  
   (b) Apply Lemma 1.2.  

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 10-7

## Solution 1.25
1. \(\frac{\lambda}{\lambda - bt}\)  
2. \(\text{Expon}(\frac{\lambda}{b})\)  

## Solution 1.26
1. \(E(Y)\)  
2. \(E(Y) = e^{\mu + \frac{\sigma}{2}}\); note that \(e^\mu\) is the median of \(Y\) (Exercise 1.11).  

## Solution 2.1
Write \(Z\) as a linear function of \(Y\), i.e., \(Z = a + bY\), then apply the method of Example 1.30 to establish the distribution of \(Z\).  

## Solution 2.2
1. The MGF of \(Y_i\) is \(\exp(\mu t + \frac{1}{2} \sigma^2 t^2)\) (\(-\infty < t < +\infty\)).  
2. Since we have a sum of independent random variables \(Y_i\) here, we can use the result on the MGF of a sum of independent random variables:  
\[
M_X(t) = \prod_{i=1}^{n} M_{Y_i}(t).
\]  
Then, substituting the MGF from part 1:  
\[
M_X(t) = \prod_{i=1}^{n} \exp \left( \mu t + \frac{1}{2} \sigma^2 t^2 \right) = \exp \left( n\mu t + \frac{n}{2} \sigma^2 t^2 \right) \quad (-\infty < t < +\infty).
\]  
3. In general, if the MGF of \(Y\) is \(M_Y(t)\), then \(Z = a + bY\) has MGF \(M_Z(t) = \exp(at)M_Y(bt)\). As \(\bar{Y} = \frac{X}{n}\), and we already have \(M_X(t)\) from part 1, we have  
\[
M_{\bar{Y}}(t) = M_X\left(\frac{t}{n}\right) = \exp \left( \mu t + \frac{\sigma^2 t^2}{2n} \right) \quad (-\infty < t < +\infty).
\]  
4. Apply the general result in part 3 again, this time to the linear function  
\[
Z = \frac{\bar{Y} - \mu}{\sigma / \sqrt{n}}.  
\]  
From \(M_{\bar{Y}}(t)\) in part 3, we have  
\[
M_Z(t) = \exp\left(-\frac{\mu}{\sigma/\sqrt{n}} t\right) M_{\bar{Y}}(t) = \exp\left(-\frac{\mu}{\sigma/\sqrt{n}} t\right) \exp\left(\mu t + \frac{\sigma^2 t^2}{2n}\right) = \exp\left(\frac{t^2}{2}\right) = \exp\left(\frac{t^2}{2}\right) \quad (-\infty < t < +\infty).
\]

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 10-8

# CHAPTER 10. SOLUTIONS
This is the MGF of a normal distribution (see part 1) with \(\mu = 0\) and \(\sigma^2 = 1\), and the MGF uniquely identifies a distribution. Thus, \(Z\) has a standard normal distribution.  

## Solution 2.3
The \(\chi^2_1\) PDF is obtained by putting \(d = 1\) in the \(\chi^2_d\) PDF given in Table 1.4. Rearrange the integral in the definition of the MGF so that it includes the integral of a gamma PDF.  

## Solution 2.5
The \(\chi^2_d\) PDF is given in Table 1.4. Rearrange the integral so that it includes the integral of a gamma PDF.  

## Solution 2.6
2. Do not start with an assumed PDF for \(Y\), or you will have a circular argument in part 3. No integration is required.  
3. Find this MGF in Table 1.4 or use the result of Exercise 2.5.  
4. \(d\)  
5. \(2d\)  

## Solution 2.7
Use the result of Exercise 2.6.  

## Solution 2.8
2. Yes  

## Solution 2.10
1. The widths are 8.53 percentage points for 90% confidence and 13.78 percentage points for 99% confidence.  
3. The widths are 8.29 percentage points for 90% confidence and 12.99 percentage points for 99% confidence.  
4. About 2.9% wider for 90% confidence and about 6.1% wider for 99% confidence.  

## Solution 2.11
2. (c) \([92.0, 100.2]\)

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 10-9

## Solution 2.12
4. 1 and 2, respectively  
5. \(\sigma^2\)  
6. \(2\sigma^4\)  
7. \(l = 0.000982\) and \(u = 5.02\)  

## Solution 2.13
1.1  
2. \(\frac{2}{n - 1}\)  
3. (a) 1  
(b) Find a relevant theorem or lemma and describe briefly how it applies to the random variable \(\frac{S^2}{\sigma^2}\).  
4. Consider the properties of \(\frac{S^2}{\sigma^2}\) as \(n \to \infty\).  
7. Don’t forget that parts 1 and 2 relate to the distribution of \(\frac{S^2}{\sigma^2}\).  

## Solution 2.14
Use the fact that a random variable with a \(\chi^2_d\) distribution arises as the sum of squares of \(d\) independent standard normal random variables, and apply the CLT.  

## Solution 2.16
1. (a) 0  
(b) \(\frac{1}{3}\)  
(c) \(\frac{e^t - e^{-t}}{2t}\)  
(d) 0 and \(\frac{1}{3}\)  
2. (a) 0  
(b) \(\frac{n}{3}\)  
(c) \(e^{-\frac{(t - t)^n}{2t}}\)  

3. (a) \(Z = n^{3/2} Y\)  
(b) \( \exp\left(\frac{t^3}{n} - \exp\left(-\frac{t^3}{n}\right)\right)\)  
(c) \(e^{\frac{t^2}{2}}\)  
(d) Standard normal  

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 10-10

# CHAPTER 10. SOLUTIONS

## Solution 2.17
Find an example where the normal approximation to the binomial is used. Argue that the use is compatible with Definition 2.1 on convergence in distribution. In particular, does Definition 2.1 mention a PMF or a PDF?  

## Solution 2.18
3. Less than or equal to 0.26  
5. 0.05  
6. (a) \(N\left(\mu, \frac{\sigma^2}{n}\right)\)  
(b) 0.05  
(c) No, it is an exact property of the normal distribution.  

## Solution 3.2
1. Applying the result for the expectation of a linear combination of random variables to \(\bar{Y}\) gives  
\[
E(\tilde{\mu}) = \mu. 
\]  
2. Applying the result for the variance of a linear combination of independent random variables to \(\bar{Y}\) gives  
\[
Var(\tilde{\mu}) = \frac{\mu}{n}.  
\]  
3. Yes, it is unbiased, and its variance goes to zero as \(n \to \infty\).  
4. (a) Using the result for the expectation of a linear function of a random variable,  
\[
E(Var(\tilde{\mu})) = E\left(\frac{\tilde{\mu}}{n}\right) = \frac{E(\tilde{\mu})}{n} = \frac{\mu}{n} = Var(\tilde{\mu}).
\]  
(b) Using the result for the variance of a linear function of a random variable,  
\[
Var(Var(\tilde{\mu})) = Var\left(\frac{\tilde{\mu}}{n}\right) = \frac{Var(\tilde{\mu})}{n^2} = \frac{\mu}{n}/n^2 = \frac{\mu}{n^3}.
\]  
(c) Yes, it is unbiased, and its variance goes to zero as \(n \to \infty\).  

## Solution 3.3
Yes. Use the results of Exercise 2.13.  

## Solution 3.4
3. The bias is \(-\frac{\sigma^2}{n}\). Hence,  
\[
MSE(\sigma) = Bias(\sigma) + Var(\sigma e^2) = -\frac{( \sigma^2 )^2}{2(n - 1)\sigma^4} = \frac{2(n - 1)\sigma^4}{n^2}.
\]  
4. Yes. The MSE goes to zero as \(n \to \infty\).  

© Copyright William J. Welch 2009–2019. All rights reserved. Not to be copied, used, or revised without explicit written permission from the copyright owner. 2019.8.14

# 10-11

5. \(S^2\) is an unbiased estimator of \(\sigma^2\), because \(E(S^2) = \sigma^2\), whereas \(\sigma e^2\) is biased. On the other hand,  
\[
Var(S^2) = \frac{2\sigma^4}{(n - 1)} \text{ is greater than } \frac{(1)(2(n - 1)\sigma^4)}{4n^2} \text{ for all } n \geq 2.
\]  
6. Compare the two MSEs:  
\[
MSE(S^2) = \frac{2\sigma^4}{(n - 1)}
\]  
Clearly,  
\[
MSE(\sigma e^2) < MSE(S^2) \text{ for all } n \geq 2, \text{ and } \sigma e^2 \text{ is more accurate in the sense of MSE.}  
```
