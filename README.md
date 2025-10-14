Eigenvalues and Eigenvectors are fundamental concepts in linear algebra used to understand linear transformations and matrices.

🔹 Definition

For a square matrix 
𝐴
A, if there exists a non-zero vector 
𝑣
v and a scalar 
𝜆
λ such that:

𝐴
𝑣
=
𝜆
𝑣
Av=λv

then:

𝑣
v is called an eigenvector of 
𝐴
A, and

𝜆
λ is called the corresponding eigenvalue.

🔹 Meaning

This equation means that when the matrix 
𝐴
A acts on the vector 
𝑣
v, it stretches or shrinks it by the factor 
𝜆
λ, without changing its direction.

🔹 Finding Eigenvalues and Eigenvectors

Find Eigenvalues (
𝜆
λ):

det
⁡
(
𝐴
−
𝜆
𝐼
)
=
0
det(A−λI)=0

This is called the characteristic equation.

Find Eigenvectors (
𝑣
v):
Substitute each eigenvalue into:

(
𝐴
−
𝜆
𝐼
)
𝑣
=
0
(A−λI)v=0

and solve for 
𝑣
v.

🔹 Example

Let

𝐴
=
[
2
	
1


1
	
2
]
A=[
2
1
	​

1
2
	​

]

Step 1: Find eigenvalues

det
⁡
(
𝐴
−
𝜆
𝐼
)
=
∣
2
−
𝜆
	
1


1
	
2
−
𝜆
∣
=
(
2
−
𝜆
)
2
−
1
=
0
det(A−λI)=
	​

2−λ
1
	​

1
2−λ
	​

	​

=(2−λ)
2
−1=0
⇒
𝜆
2
−
4
𝜆
+
3
=
0
⇒
𝜆
=
3
,
1
⇒λ
2
−4λ+3=0⇒λ=3,1

Step 2: Find eigenvectors
For 
𝜆
=
3
λ=3:

(
𝐴
−
3
𝐼
)
𝑣
=
0
⇒
[
−
1
	
1


1
	
−
1
]
𝑣
=
0
(A−3I)v=0⇒[
−1
1
	​

1
−1
	​

]v=0
⇒
𝑣
=
[
1


1
]
⇒v=[
1
1
	​

]

For 
𝜆
=
1
λ=1:

(
𝐴
−
𝐼
)
𝑣
=
0
⇒
[
1
	
1


1
	
1
]
𝑣
=
0
(A−I)v=0⇒[
1
1
	​

1
1
	​

]v=0
⇒
𝑣
=
[
1


−
1
]
⇒v=[
1
−1
	​

]
🔹 Applications

Diagonalization of matrices

Solving systems of differential equations

Principal Component Analysis (PCA) in machine learning

Quantum mechanics and vibration analysis
