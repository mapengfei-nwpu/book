//STARTWHOLE
static char help[] = "Solve a tridiagonal system of arbitrary size.\n"
"Option prefix = tri_.\n";

#include <petsc.h>

int main(int argc,char **args) {
    PetscErrorCode ierr;
    Vec    x, b, xexact;
    Mat    A;
    KSP    aksp;
    PC     pc;
    int    m = 4, i, Istart, Iend, j[3];
    double v[3], xval, errnorm;

    PetscInitialize(&argc,&args,NULL,help);

    ierr = VecCreate(PETSC_COMM_WORLD,&x); CHKERRQ(ierr);
    ierr = VecSetSizes(x,PETSC_DECIDE,m); CHKERRQ(ierr);
    ierr = VecSetFromOptions(x); CHKERRQ(ierr);
    ierr = VecDuplicate(x,&b); CHKERRQ(ierr);
    ierr = VecDuplicate(x,&xexact); CHKERRQ(ierr);

    ierr = MatCreate(PETSC_COMM_WORLD,&A); CHKERRQ(ierr);
    ierr = MatSetSizes(A,PETSC_DECIDE,PETSC_DECIDE,m,m); CHKERRQ(ierr);
    ierr = MatSetOptionsPrefix(A,"a_"); CHKERRQ(ierr);
    ierr = MatSetFromOptions(A); CHKERRQ(ierr);
    ierr = MatSetUp(A); CHKERRQ(ierr);
    ierr = MatGetOwnershipRange(A,&Istart,&Iend); CHKERRQ(ierr);
    for (i=Istart; i<Iend; i++) {
        if (i == 0) {
            v[0] = 3.0;  v[1] = -1.0;
            j[0] = 0;    j[1] = 1;
            ierr = MatSetValues(A,1,&i,2,j,v,INSERT_VALUES); CHKERRQ(ierr);
        } else {
            v[0] = -1.0;  v[1] = 3.0;  v[2] = -1.0;
            j[0] = i-1;   j[1] = i;    j[2] = i+1;
            if (i == m-1) {
                ierr = MatSetValues(A,1,&i,2,j,v,INSERT_VALUES); CHKERRQ(ierr);
            } else {
                ierr = MatSetValues(A,1,&i,3,j,v,INSERT_VALUES); CHKERRQ(ierr);
            }
        }
        xval = exp(cos(i));
        ierr = VecSetValues(xexact,1,&i,&xval,INSERT_VALUES); CHKERRQ(ierr);
    }
    ierr = MatAssemblyBegin(A,MAT_FINAL_ASSEMBLY); CHKERRQ(ierr);
    ierr = MatAssemblyEnd(A,MAT_FINAL_ASSEMBLY); CHKERRQ(ierr);
    ierr = VecAssemblyBegin(xexact); CHKERRQ(ierr);
    ierr = VecAssemblyEnd(xexact); CHKERRQ(ierr);
    ierr = MatMult(A,xexact,b); CHKERRQ(ierr);

    ierr = KSPCreate(PETSC_COMM_WORLD,&aksp); CHKERRQ(ierr);
    ierr = KSPSetOperators(aksp,A,A); CHKERRQ(ierr);
    ierr = KSPSetType(aksp, KSPPREONLY); CHKERRQ(ierr);
    
    ierr = KSPGetPC(aksp, &pc); CHKERRQ(ierr);
    ierr = PCSetType(pc, PCLU); CHKERRQ(ierr);
    
    ierr = KSPSolve(aksp,b,x); CHKERRQ(ierr);

    ierr = VecAXPY(x,-1.0,xexact); CHKERRQ(ierr);
    ierr = VecNorm(x,NORM_2,&errnorm); CHKERRQ(ierr);
    ierr = PetscPrintf(PETSC_COMM_WORLD,
    "error for m = %d system is |x-xexact|_2 = %.1e\n",m,errnorm); CHKERRQ(ierr);

    KSPDestroy(&aksp);  MatDestroy(&A);
    VecDestroy(&x);  VecDestroy(&b);  VecDestroy(&xexact);
    return PetscFinalize();
}
//ENDWHOLE
