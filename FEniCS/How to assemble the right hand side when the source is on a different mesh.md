How to assemble the right hand side when the source is on a different mesh?

Hi everyone !

Domain $B$ is a sub domain of domain $\Omega$. $B_h$ and $\Omega_h$ are different triangulations which means $B_h$ is not the sub mesh of $\Omega$.  

Now, I want to assemble $\int_{B_h}f\cdot v $ as the right hand side where $f$ is a vector function and $v$ is a test function in $\Omega_h$. I have calculated the Gauss points and weights for every cell in $B_h$. Therefore, $\int_{B_h}f\cdot v=\Sigma w_i f_i v_i$ can be set as an item of `PETSCVector`. ( $i$ mean function evaluates at $i$th Gauss point)

I can find the cell contains a given gauss point. However, how to evaluate basis function on the cell and find its index in `PETSCVector` ?