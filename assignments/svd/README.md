# Singular Value Decomposition 
Why do we use SVD, when PCA might be a bit more intuitive?  The reason is that design matrices can be very large in the case when the number of features is large (i.e. when we want to do dimensionality reduction).  SVD can avoid this memory intensive intermediate step, so is often thought of as being computationally superior.  Given that the aim of the two techniques is the same (with often very similar results), SVD is the more widely used method.

## Applications of SVD
<ol>
<li>Determining range, null space and rank (also numerical rank).</li>
<li>Matrix approximation</li>
<li>Inverse and pseudo-inverse (useful for <a href="https://math.stackexchange.com/questions/772039/how-does-the-svd-solve-the-least-squares-problem/2173715#2173715">least-squared problems</a> )</li>
<li>Denoising - small singular values typically correspond to noise.</li>
<li>Compression</li>

## When are PCA/SVD not a good option?
At some point, they are computationally intractable O(m^3)

## Further Reading
* [Dimensionality Reduction](http://infolab.stanford.edu/~ullman/mmds/ch11.pdf)
* [SVD](http://www.math.iit.edu/~fass/477577_Chapter_12.pdf)
* [Computing SVD](http://www.cs.utexas.edu/users/inderjit/public_papers/HLA_SVD.pdf)