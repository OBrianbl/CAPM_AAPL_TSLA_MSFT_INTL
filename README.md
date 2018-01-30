# Capital Asset Pricing Model (CAPM)

Harry Markowitz met Bob Sharp in 1960 and offered Sharp the opportunity to continue his work on how various stocks function together. Sharp discovered the CAPM.
<br>

Like the Markowitz, Sharp develops the CAPM under the following assumptions:

* Investors are risk adverse.
* Investors prefer higher returns.
* Investors are willing to buy the optimal portfolio, in terms of both risk and returns.
<br>
Sharpe then introduces the market portfolio concept. This market portfolio is constructed as a combination of all possible investments in the world (bonds and stocks). This allows for bundling of securities in such a way that maximizes risk-return, while optimizing (minimizing) risk due to being diversified. Thus, this portfolio will lie on some point on the efficient frontier and is the most efficient portfolio.
<br>
The different between the CAPM and the Markowitz optimized portfolio, is that the CAMP assumes that a risk-free asset exists (an investment with zero risk: zero standard deviation, while producing a positive return). This will produce a lower expected return, but people will buy into it due to the associated zero risk. This assumption can be expressed as: 
<br>

 * Markets are efficient, and when operating in an efficient market, investors are only compensated for the added risk they are willing to bear. 
 
  <br>
This means that investors cannot arbitrage the market and get a higher return, while still obtaining zero risk. Therefore, if the investor wants a higher expected return, the investor must be willing to take on more risk, while if they want zero risk they must be willing to accept the low level of expected return. 

  <br>
  
The risk-free investment offers the ability for investors to invest in a market portfolio with higher returns, while diversifying this investment with a risk-free portfolio, but then the question is how much to invest in each. The Capital Market Line, a straight line emanating from the risk-free point, <a href="https://www.codecogs.com/eqnedit.php?latex=r_f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_f" title="r_f" /></a>, and projected in such a manner that it lies tangent to a point on the efficient frontier. The point in which the Capital Market Line is tangent with the efficient frontier is the market portfolio. This line explains the relation between the risk of return (measured by the standard deviation) for portfolios of assets or efficient assets. The way we can interpret the line is that as risk increases, the corresponding expected rate of return will also increase. We can express this mathematically as:

<br>

 <a href="https://www.codecogs.com/eqnedit.php?latex=$$\overline{r}=&space;r_f&space;&plus;&space;\frac{\overline{r}_M&space;-&space;r_f}{\sigma_M}\sigma&space;$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$\overline{r}=&space;r_f&space;&plus;&space;\frac{\overline{r}_M&space;-&space;r_f}{\sigma_M}\sigma&space;$$" title="$$\overline{r}= r_f + \frac{\overline{r}_M - r_f}{\sigma_M}\sigma $$" /></a>
 
 <br>
 
where the expected value  of the market rate or return is <a href="https://www.codecogs.com/eqnedit.php?latex=$$\overline{r}_M$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$\overline{r}_M$$" title="$$\overline{r}_M$$" /></a>  and <a href="https://www.codecogs.com/eqnedit.php?latex=$$\overline{r}$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$\overline{r}$$" title="$$\overline{r}$$" /></a>  is the expected value of the rate of the return of an arbitrary efficient asset. The standard deviation of the market rate of return is <a href="https://www.codecogs.com/eqnedit.php?latex=$$\sigma_M$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$\sigma_M$$" title="$$\sigma_M$$" /></a> and the standard deviation of the rate of the return of an arbitrary efficient asset is <a href="https://www.codecogs.com/eqnedit.php?latex=$$\sigma$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$\sigma$$" title="$$\sigma$$" /></a>.
 
 <br>
 
 The slope of the capital market line, often referred to as the price of risk, explains how much the portfolios expected rate of return must increase if the standard deviation of the rate increases by one unit. We can express the slope of the capital market line as:
 
 <br> 
 <a href="https://www.codecogs.com/eqnedit.php?latex=K=&space;\frac{\overline{r}_M-r_f}{\sigma_M}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K=&space;\frac{\overline{r}_M-r_f}{\sigma_M}" title="K= \frac{\overline{r}_M-r_f}{\sigma_M}" /></a>
 <br> 
 
One of the main concepts of the CAPM we need to understand is Beta. The beta allows us to quantify the relationship between the overall market portfolio and a security. If systemic risk exists (i.e. a recession) then the market portfolio, no matter how you choose it can suffer from a negative percent rate of return. There are some assets in the market portfolio that are less risky (have a lower standard deviation) and will decrease less than the market.

<br>

For example, if a recession hits causing the expected rate of return for the market portfolio to decrease by 5%, there can still exist a stock, lets call it stock A, which has a decreases in value 3%. Since the stock A's value is -3% and this is a less  than the market portfolios -5% rate of return, we then can describe stock A as less volatile. Now, if there exist a stock be in the market portfolio and it experiences a value that decreases by 7%, since this is more of a decrease than the market portfolio, we refer to stock B as more volatile.
 
<br>

If the economy is doing well and the market portfolio is producing a 9% rate of return stock A, a low risk low return investment, might only earn its investors 5%, while stock B, the higher risk higher return investment, will earn 12%.

<br> 

This is were Beta comes in. Beta, as mentioned before, allows us to measure the relationship between the individual asset and the market portfolio. Mathematically we can express Beta as

<br>

<a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;=&space;\frac{cov(r_x,r_M)}{\sigma_{M}^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;\frac{cov(r_x,r_M)}{\sigma_{M}^2}" title="\beta = \frac{cov(r_x,r_M)}{\sigma_{M}^2}" /></a>

<br>

where <a href="https://www.codecogs.com/eqnedit.php?latex=r_x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_x" title="r_x" /></a> represents rate of the return of the assest, <a href="https://www.codecogs.com/eqnedit.php?latex=r_M" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_M" title="r_M" /></a> is rate of return for the market, and  <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma_{M}^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma_{M}^2" title="\sigma_{M}^2" /></a> is the variance of the market. 

<br>

The is measure of market risk is one that cannot be avoid through diversification. Depending on the value that Beta takes on we interpret the meaning differently:

<br>

* <a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;0" title="\beta = 0" /></a>, Asset is considered to have no relationship with the market. 
* <a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;<&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;<&space;1" title="\beta < 1" /></a>,  Asset is considered defensive since  these stocks will typically loose less. 
* <a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;=&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;1" title="\beta = 1" /></a>,  Asset is considered to perform the same as the market.
* <a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;>&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;>&space;1" title="\beta > 1" /></a>,  Asset is considered to be aggressive, since they are riskier than the market. These stocks perform better than the market when the economy is doing well and loose more when the market is not doing well.

## The Capital Asset Pricing Model

<a href="https://www.codecogs.com/eqnedit.php?latex=r_i&space;=&space;r_f&space;&plus;&space;\beta_{iM}(r_M&space;-&space;r_f)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_i&space;=&space;r_f&space;&plus;&space;\beta_{iM}(r_M&space;-&space;r_f)" title="r_i = r_f + \beta_{iM}(r_M - r_f)" /></a>
<br> 
where 

*  <a href="https://www.codecogs.com/eqnedit.php?latex=r_f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_f" title="r_f" /></a> risk-free rate or bare minimum that an investor is willing to take on
*  <a href="https://www.codecogs.com/eqnedit.php?latex=\beta_{iM}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta_{iM}" title="\beta_{iM}" /></a> beta between the asset and the market, the amount of risk the security bears regarding the market portfolio 
*  <a href="https://www.codecogs.com/eqnedit.php?latex=r_m" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_m" title="r_m" /></a> expected reutnr of the market portfolio
* <a href="https://www.codecogs.com/eqnedit.php?latex=r_M-r_f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_M-r_f" title="r_M-r_f" /></a> is the equity premium component, which is the expected return of the market portfolio minus the risk-free rate

## Applying the CAPM

In real life, there does not exist an actual risk-free asset. Every asset contains risk, though some have relatively small risk compared to others. The closest we can have to a risk-free rate is the yield of a 10-year US government bond at 2.5%. Since we are applying this to US companies, we will use the 2.5% for our risk free. Further, we will approximate the market portfolio with the S&P500, thus <a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;=&space;0.62" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;0.62" title="\beta = 0.62" /></a>. The equity risk premium has been historically between 4.5% and 5.5%, thus we will use 5% which is in-between. 
<br>

Therefore, we have the following model:
<br> 

<a href="https://www.codecogs.com/eqnedit.php?latex=r(i)&space;=&space;2.5\%&space;&plus;&space;0.62*5\%&space;=&space;5.6\%" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r(i)&space;=&space;2.5\%&space;&plus;&space;0.62*5\%&space;=&space;5.6\%" title="r(i) = 2.5\% + 0.62*5\% = 5.6\%" /></a>
<br>

This 5.6% is the expected return an investor should expect given the risk that they are taking on.

<br>

## Sharp Ratio

A rational investor considers both risk and return. They want to maximize their return and minimize their risk. Thus, investors would want to be able to compare stocks in terms of risk-return performance. This is how William Sharpe developed the Sharpe Ration. Mathematically the Sharpe ratio can be expressed as: 
<br>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{r_i-r_f}{\sigma_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{r_i-r_f}{\sigma_i}" title="\frac{r_i-r_f}{\sigma_i}" /></a>

* <a href="https://www.codecogs.com/eqnedit.php?latex=r_f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_f" title="r_f" /></a> - risk-free rate
* <a href="https://www.codecogs.com/eqnedit.php?latex=r_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_i" title="r_i" /></a> - rate of return of the stock "i"
* <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma_i" title="\sigma_i" /></a> - standard deviation of the stock "i"
* <a href="https://www.codecogs.com/eqnedit.php?latex=r_i-r_f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_i-r_f" title="r_i-r_f" /></a> - excess return of stock "i"

What this tells us is, that if we increase the increase the expected rate of return the stocks Sharpe ratio also increases. Further the stocks standard deviation and the Sharpe ratio have an inverse relationship, meaning that if the standard deviation increases the Sharpe ration decreases. This allows us to compare assets vs assets and investment portfolios vs portfolios quickly. Thus, we can produce the Sharpe Capital Market Line.



<br><br>
<a href="https://obrianbl.github.io/">Return to Main Page</a>
