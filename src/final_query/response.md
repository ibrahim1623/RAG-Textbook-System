To address the problem concerning the Poisson estimator \( \tilde{\mu} = \bar{Y} \), we can follow the questions one by one:

**1. Show that \( \tilde{\mu} \) is unbiased.**

An estimator \( \tilde{\mu} \) is unbiased if \( E(\tilde{\mu}) = \mu \). Since \( Y_i \) follows a Poisson distribution with parameter \( \mu \), we have:

\[
E(Y_i) = \mu.
\]

The sample mean is given by:

\[
\tilde{\mu} = \bar{Y} = \frac{1}{n} \sum_{i=1}^{n} Y_i.
\]

Applying the linearity of expectation:

\[
E(\tilde{\mu}) = E\left(\frac{1}{n} \sum_{i=1}^{n} Y_i\right) = \frac{1}{n} \sum_{i=1}^{n} E(Y_i) = \frac{1}{n} \sum_{i=1}^{n} \mu = \mu.
\]

Thus, \( \tilde{\mu} \) is an unbiased estimator of \( \mu \).

---

**2. Find \( Var(\tilde{\mu}) \).**

Using the properties of variance, the variance of the sample mean is:

\[
Var(\tilde{\mu}) = Var\left(\frac{1}{n} \sum_{i=1}^{n} Y_i\right) = \frac{1}{n^2} \sum_{i=1}^{n} Var(Y_i).
\]

Since \( Y_i \) follows a Poisson distribution with \( Var(Y_i) = \mu \), we have:

\[
Var(Y_i) = \mu \text{ for each } i.
\]

Thus,

\[
Var(\tilde{\mu}) = \frac{1}{n^2} \sum_{i=1}^{n} \mu = \frac{1}{n^2} \cdot n \mu = \frac{\mu}{n}.
\]

---

**3. Is \( \tilde{\mu} \) a consistent estimator of \( \mu \)?**

An estimator is consistent if it converges in probability to the true value as \( n \to \infty \). The sample mean \( \tilde{\mu} = \bar{Y} \) is a consistent estimator of \( \mu \) if:

\[
Var(\tilde{\mu}) \to 0 \text{ as } n \to \infty.
\]

From the previous part, we found \( Var(\tilde{\mu}) = \frac{\mu}{n} \). As \( n \to \infty \), \( \frac{\mu}{n} \to 0 \).

Thus, \( \tilde{\mu} \) converges in probability to \( \mu \), meaning it is a consistent estimator of \( \mu \).

---

**4. Consider \( \tilde{Var}(\tilde{\mu}) = \frac{\tilde{\mu}}{n} \) as an estimator of \( Var(\tilde{\mu}) \).**

(a) **Show that \( \tilde{Var}(\tilde{\mu}) \) is an unbiased estimator of \( Var(\tilde{\mu}) \).**

To determine whether \( \tilde{Var}(\tilde{\mu}) \) is unbiased, we want to check:

\[
E\left(\tilde{Var}(\tilde{\mu})\right) = E\left(\frac{\tilde{\mu}}{n}\right) = \frac{1}{n} E(\tilde{\mu}) = \frac{1}{n} \mu.
\]

Since \( Var(\tilde{\mu}) = \frac{\mu}{n} \), we indeed find:

\[
E\left(\tilde{Var}(\tilde{\mu})\right) = Var(\tilde{\mu}).
\]

Thus, \( \tilde{Var}(\tilde{\mu}) \) is an unbiased estimator of \( Var(\tilde{\mu}) \).

(b) **What is the variance of \( \tilde{Var}(\tilde{\mu}) \)?**

To find the variance of \( \tilde{Var}(\tilde{\mu}) = \frac{\tilde{\mu}}{n} \), we first need to recall that \( \tilde{\mu} \) has variance \( \frac{\mu}{n} \), so:

\[
Var(\tilde{Var}(\tilde{\mu})) = Var\left(\frac{\tilde{\mu}}{n}\right) = \frac{1}{n^2} Var(\tilde{\mu}) = \frac{1}{n^2} \cdot \frac{\mu}{n} = \frac{\mu}{n^3}.
\]

(c) **Is \( \tilde{Var}(\tilde{\mu}) \) a consistent estimator of \( Var(\tilde{\mu}) \)?**

An estimator is consistent if it converges in probability to the parameter it estimates. As \( n \to \infty \):

\[
Var(\tilde{Var}(\tilde{\mu})) = \frac{\mu}{n^3} \to 0.
\]

Therefore, \( \tilde{Var}(\tilde{\mu}) \) is a consistent estimator of \( Var(\tilde{\mu}) \).

---

This concludes the proofs and answers to the given problem.