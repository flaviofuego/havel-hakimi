# havel-hakimi
Small python3 program implementing the Havel-Hakimi algorithm (recursively) to decide if there exists a graph for a given degree sequence, for to use execute the line 
```python
pip install -r requirements.txt
```
and then the following line is executed
```python
python havel-hakimi.py
```
other option is This is the link to download an executable 
```
https://uninorte-my.sharepoint.com/:u:/g/personal/francocd_uninorte_edu_co/EeM4_rZofZhAsmcya6TRcgkBuJZgHahdBqT86VYwg5Irwg?e=tXtMVe
```

# Group: 
```
Cristian Gonzalez franco
Flavio Arregoces Mercado
Gabriel Palencia Cure
Camilo de la rosa
Carlos Molina
Nrc: 2672
```

# Usage
```python
havel_hakimi(sequence) # where sequence is a int array
```
# Examples
## Example 1
```python
havel_hakimi([1, 1, 2, 3, 4, 4, 5])
```
Result:
```
[1, 1, 2, 3, 4, 4, 5] --sort--> [1, 1, 2, 3, 4, 4, 5]
[1, 1, 2, 3, 4, 4, 5] --alg-->[1, 0, 1, 2, 3, 3]
[1, 0, 1, 2, 3, 3] --sort--> [0, 1, 1, 2, 3, 3]
[0, 1, 1, 2, 3, 3] --alg-->[0, 1, 0, 1, 2]
[0, 1, 0, 1, 2] --sort--> [0, 0, 1, 1, 2]
[0, 0, 1, 1, 2] --alg-->[0, 0, 0, 0]
Finished! Graph IS constructable with Havel Hakimi algorithm.
```
## Example 2
```python
havel_hakimi([2, 2, 2, 2, 3])
```
Result:
```
[2, 2, 2, 2, 3] --sort--> [2, 2, 2, 2, 3]
[2, 2, 2, 2, 3] --alg-->[2, 1, 1, 1]
[2, 1, 1, 1] --sort--> [1, 1, 1, 2]
[1, 1, 1, 2] --alg-->[1, 0, 0]
[1, 0, 0] --sort--> [0, 0, 1]
[0, 0, 1]
Failed! Graph is not constructable with Havel Hakimi algorithm
```
