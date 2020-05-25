import matplotlib.pyplot as plt
from fenics import *
from mshr import *

# Load mesh from file
channel = Rectangle(Point(0, 0), Point(16, 8))
cylinder = Circle(Point(4,4), 0.5)
domain = channel - cylinder
mesh = generate_mesh(domain, 64)

# Define function spaces (P2-P1)
V = VectorFunctionSpace(mesh, "Lagrange", 1)
Q = FunctionSpace(mesh, "Lagrange", 1)

# Define trial and test functions
u = TrialFunction(V)
p = TrialFunction(Q)
v = TestFunction(V)
q = TestFunction(Q)

# Set parameter values
dt = 0.005
re = 100

# Define boundary conditions
inflow = DirichletBC(V, Constant((1,0)), 'near(x[0], 0)')
walls  = DirichletBC(V, (0, 0), "near(x[1], 0) || near(x[1],8)")
cylinder = DirichletBC(V, Constant((0,0)), 'on_boundary && x[0]>2 && x[0]<15 && x[1]>2 && x[1]<15')

bcu = [inflow, walls,cylinder]

outflow = DirichletBC(Q, 0, "near(x[0], 16)")
bcp = [outflow]

# Create functions
u_    = Function(V)
u_n = Function(V) 
p_    = Function(Q)
p_n  = Function(Q)
# Define coefficients
k = Constant(dt)
f = Constant((0, 0))

# Tentative velocity step
F1 =  -dot((u-u_n)/k, v)*dx - dot(dot(u_n,nabla_grad(u_n)),v)*dx - 1/re*inner(nabla_grad(u_n),nabla_grad(v))*dx + k/2*dot(dot(u_n,nabla_grad(u_n)),dot(u_n,nabla_grad(v)))*dx
a1 = lhs(F1)
L1 = rhs(F1)

# Pressure update
theta1 = Constant(0.75)
theta2 = Constant(0.75)

def grad_p(p_n, p, theta2):
    return ((1-theta2)*nabla_grad(p_n)+theta2*nabla_grad(p))
# F2 = dot(nabla_grad(p),nabla_grad(q))*dx+dot(u_,nabla_grad(q))/k*dx
F2 = div(theta1*u_ + (1-theta1)*u_n)*q*dx + k*theta1*dot(grad_p(p_n,p,theta2),nabla_grad(q))*dx
a2 = lhs(F2)
L2 = rhs(F2)

# Velocity update
# F3 = - dot((u-u_)/k,v)*dx - dot(nabla_grad(p_),v)*dx
F3 = -dot((u-u_)/k,v)*dx - dot(grad_p(p_n,p_,theta2),v)*dx - k/2*dot(nabla_grad(p_n),dot(u_n,nabla_grad(v)))*dx    
a3 = lhs(F3)
L3 = rhs(F3)

# Assemble matrices
A1 = assemble(a1)
A2 = assemble(a2)
A3 = assemble(a3)

# Use amg preconditioner if available
prec = "amg" if has_krylov_solver_preconditioner("amg") else "default"

# Use nonzero guesses - essential for CG with non-symmetric BC
parameters['krylov_solver']['nonzero_initial_guess'] = True

# Create files for storing solution
ufile = File("results/velocity.pvd")
pfile = File("results/pressure.pvd")

# Time-stepping
t = dt
n=0
while n < 4000:
    # Compute tentative velocity step
    b1 = assemble(L1)
    [bc.apply(A1, b1) for bc in bcu]
    solve(A1, u_.vector(), b1, "bicgstab", "default")

    # Pressure correction
    b2 = assemble(L2)
    [bc.apply(A2,b2) for bc in bcp]
    [bc.apply(p_.vector()) for bc in bcp]
    solve(A2, p_.vector(), b2, "bicgstab", prec)

    # Velocity correction
    b3 = assemble(L3)
    [bc.apply(A3, b3) for bc in bcu]
    solve(A3, u_.vector(), b3, "bicgstab", "default")
    t += dt
    n += 1
    # Save to file
    if(n%100 == 0):
        ufile << u_
        print(t)
        print(n)
        print(u_.vector().max())
        pfile << p_

    # Move to next time step
    p_n.assign(p_)
    u_n.assign(u_)

plt.figure()
plot(p_n)

plt.figure()
plot(u_n)
plt.show()
